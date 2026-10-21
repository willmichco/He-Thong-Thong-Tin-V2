"""Xuất bản mẫu thành một tệp HTML để xem thử ở nơi không chạy được Django.

Mọi màn hình được dựng bằng chính các view và template của khu quản trị, rồi gộp vào một tệp:
mỗi màn hình là một <section data-view="...">, chuyển qua lại bằng #địa-chỉ (xem app.js).
CSS và JS được nhúng thẳng vào tệp. Tệp xuất không có <!doctype>, <html>, <head>, <body>
vì trang xem trước riêng tư tự bọc khung tài liệu.

Chạy: python manage.py xuat_ban_mau --out dist/ban-mau.html
"""

import html
import re
from pathlib import Path

from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.management.base import BaseCommand, CommandError
from django.test import Client
from django.test.utils import override_settings

from quantri import demo

FONTS = (
    "https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700"
    "&family=IBM+Plex+Mono:wght@400;500;600&family=Literata:opsz,wght@7..72,500;7..72,600&display=swap"
)

# Mục điều hướng được tô đậm theo đoạn đầu của địa chỉ.
NAV_THEO_DOAN = {
    "": "hom_nay",
    "ban-tin": "hom_nay",
    "canh-bao": "hom_nay",
    "goi-y": "goi_y",
    "doi-thu": "doi_thu",
    "van-ban": "van_ban",
    "chu-de": "chu_de",
}


def duong_dan_xuat():
    """Mọi địa chỉ có trong bản mẫu, theo thứ tự xuất."""
    paths = ["/", f"/ban-tin/{demo.HOM_NAY.isoformat()}/"]
    paths += [f"/canh-bao/{a['ma']}/" for a in demo.ALERTS]
    paths += ["/goi-y/"] + [f"/goi-y/{c['ma']}/" for c in demo.CARDS]
    paths += ["/doi-thu/", "/doi-thu/tong-hop/", "/doi-thu/cau-hoi/", "/doi-thu/khoang-trong/"]
    paths += ["/van-ban/", "/van-ban/lich/", "/van-ban/can-xem/"]
    paths += [f"/van-ban/{d['id']}/" for d in demo.DOCUMENTS]
    paths += ["/chu-de/", "/chu-de/kho-bai/", "/chu-de/tu-khoa/", "/tin-hieu/", "/dang-nhap/"]
    return paths


def ma_man_hinh(path):
    """'/goi-y/T-20261021-01/' -> 'goi-y.T-20261021-01'; '/' -> 'hom-nay'."""
    return path.strip("/").replace("/", ".") or "hom-nay"


def _cat(text, start, end):
    i = text.index(start) + len(start)
    return text[i:text.index(end, i)]


def _doi_lien_ket(fragment, tokens):
    """Đổi href nội bộ sang #mã-màn-hình; trả về (đoạn đã đổi, các địa chỉ không có trong bản xuất)."""
    thieu = set()

    def thay(m):
        path = m.group(1)
        if path in tokens:
            return f'href="#{tokens[path]}"'
        thieu.add(path)
        return m.group(0)

    return re.sub(r'href="(/[^"#?]*)(?:\?[^"#]*)?(?:#[^"]*)?"', thay, fragment), thieu


def _tach_id(fragment, token):
    """Thêm hậu tố vào id trong một màn hình để các màn hình gộp chung không trùng id."""
    hau_to = "--" + token.replace(".", "_")
    fragment = re.sub(r'(?<![\w-])(id|for|aria-labelledby|aria-describedby)="([^"]+)"',
                      lambda m: f'{m.group(1)}="{m.group(2)}{hau_to}"', fragment)
    return re.sub(r'data-target="#([^"]+)"', lambda m: f'data-target="#{m.group(1)}{hau_to}"', fragment)


def dung_ban_mau():
    """Trả về (nội dung tệp xuất, các địa chỉ nội bộ không có trong bản xuất)."""
    paths = duong_dan_xuat()
    tokens = {p: ma_man_hinh(p) for p in paths}
    client = Client()
    trang = {}
    with override_settings(ALLOWED_HOSTS=["testserver"]):
        for p in paths:
            r = client.get(p)
            if r.status_code != 200:
                raise CommandError(f"{p} trả về {r.status_code}")
            trang[p] = r.content.decode("utf-8")

    thieu = set()
    sections = []
    for p in paths:
        page = trang[p]
        main, t = _doi_lien_ket(_cat(page, "<!--MAIN-START-->", "<!--MAIN-END-->"), tokens)
        thieu |= t
        token = tokens[p]
        title = html.escape(html.unescape(_cat(page, "<title>", "</title>")), quote=True)
        nav = NAV_THEO_DOAN.get(p.strip("/").split("/")[0], "")
        hidden = "" if token == "hom-nay" else " hidden"
        sections.append(
            f'<section data-view="{token}" data-nav="{nav}" data-title="{title}"{hidden}>'
            f"{_tach_id(main, token)}</section>"
        )

    home = trang["/"]
    shell = _cat(home, "<!--SHELL-START-->", "<!--SHELL-END-->")
    head, rest = shell.split("<!--MAIN-START-->", 1)
    tail = rest.split("<!--MAIN-END-->", 1)[1]
    shell = head + "\n".join(sections) + tail
    shell = shell.replace('data-mode="server"', 'data-mode="static"', 1)
    shell, t = _doi_lien_ket(shell, tokens)
    thieu |= t

    css = Path(finders.find("quantri/app.css")).read_text(encoding="utf-8")
    js = Path(finders.find("quantri/app.js")).read_text(encoding="utf-8")
    out = (
        "<title>Thông tin pháp lý nóng</title>\n"
        '<meta name="claude:viewport-fit-sides" content="cover">\n'
        '<meta name="robots" content="noindex, nofollow">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        f'<link rel="stylesheet" href="{FONTS}">\n'
        f"<style>\n{css}</style>\n"
        f"{shell}\n"
        f"<script>\n{js}</script>\n"
    )
    return out, thieu


class Command(BaseCommand):
    help = "Xuất bản mẫu giao diện thành một tệp HTML để xem thử (chuyển màn hình bằng #địa-chỉ)."

    def add_arguments(self, parser):
        parser.add_argument("--out", default=str(Path(settings.BASE_DIR) / "dist" / "ban-mau.html"))

    def handle(self, *args, **opts):
        out, thieu = dung_ban_mau()
        if thieu:
            self.stderr.write("Liên kết nội bộ chưa có trong bản xuất: " + ", ".join(sorted(thieu)))
        target = Path(opts["out"])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(out, encoding="utf-8")
        self.stdout.write(f"Đã xuất {len(duong_dan_xuat())} màn hình vào {target} ({len(out) // 1024} KB).")
