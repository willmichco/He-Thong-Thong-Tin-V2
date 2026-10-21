"""Màn hình khu quản trị (Phụ lục C của Đặc tả 3.2).

Bản mẫu: mọi màn hình đọc dữ liệu minh họa từ demo.py. Nút thao tác chưa ghi dữ liệu;
static/quantri/app.js hiện thông báo nói rõ khi chạy thật thao tác sẽ ghi vào bảng nào.
"""

import re
from datetime import date

from django.http import Http404, HttpResponse
from django.shortcuts import render

from . import demo


def _han_dang(chu):
    """Đổi "đăng tốt nhất" của thẻ thành nhãn hạn ngắn và mức gấp: (nhãn đầy đủ, nhãn ngắn, mức)."""
    if "24 giờ" in chu:
        return "Đăng trong 24 giờ", "24 giờ", "gap"
    m = re.search(r"(\d{2})/(\d{2})/(\d{4})", chu)
    if not m:
        return chu, chu, "nhe"
    con = (date(int(m[3]), int(m[2]), int(m[1])) - demo.HOM_NAY).days
    muc = "gap" if con <= 3 else "thuong"
    return f"Đăng trước {m[1]}/{m[2]} · còn {con} ngày", f"còn {con} ngày", muc


def _the_hom_nay(c):
    """Thẻ kèm lý do ngắn (vì sao viết hôm nay), hạn đăng và tên nền tảng, cho trang Hôm nay."""
    han, han_ngan, han_muc = _han_dang(c["dang_tot_nhat"])
    ly_do = []
    if c["moc"]:
        ly_do.append(f"{c['moc']} (còn {c['moc_con_ngay']} ngày)" if c["moc_con_ngay"] else c["moc"])
    if c["quan_tam"]:
        ly_do.append(c["quan_tam"][0].upper() + c["quan_tam"][1:])
    ly_do.append(f"{c['n_bao']} báo, {c['n_doi_thu']} đối thủ đã viết")
    return dict(c, ly_do=ly_do, ten_nen_tang=[n for n, _ in c["nen_tang"]], han=han, han_ngan=han_ngan, han_muc=han_muc)


def hom_nay(request):
    the_pro = [_the_hom_nay(c) for c in demo.the_theo_luong("pro")]
    the_pub = [_the_hom_nay(c) for c in demo.the_theo_luong("public")]
    qua_han = [r for r in demo.REVIEW_ITEMS if r["qua_han"]]
    chu_de_nhieu = demo.CHU_DE_DOI_THU_7_NGAY[:4]
    nhieu_nhat = max(t["so_bai"] for t in chu_de_nhieu)
    bai_moi = [a for a in demo.COMPETITOR_ARTICLES if a["moi"]]
    return render(request, "quantri/hom_nay.html", {
        "trang": "hom_nay",
        "alerts": [a for a in demo.ALERTS if a["status"] != "acknowledged"],
        # Thẻ hạng 1 của mỗi luồng là việc nên viết trước; các thẻ còn lại xếp sau theo luồng và hạng.
        "leads": [l[0] for l in (the_pro, the_pub) if l],
        "tiep_theo": the_pro[1:] + the_pub[1:],
        "so_goi_y": len(the_pro) + len(the_pub),
        "van_ban_moi": [demo.van_ban(i) for i in demo.DIGEST["van_ban_moi_a"]],
        "sap_hieu_luc": [e for e in demo.CALENDAR if e["loai"] in ("Hiệu lực", "Hạn góp ý") and 0 <= e["con_ngay"] <= 30][:4],
        "so_bai_moi": 23,
        "chu_de_nhieu": [dict(t, pct=round(t["so_bai"] / nhieu_nhat * 100)) for t in chu_de_nhieu],
        "bai_tang": sorted([a for a in bai_moi if a["tang"]], key=lambda a: -a["tang"])[:4],
        "so_loi_thoi": sum(1 for a in demo.COMPETITOR_ARTICLES if a["loi_thoi"]),
        "review_items": demo.REVIEW_ITEMS,
        "qua_han": qua_han,
        "so_chua_qua_han": len(demo.REVIEW_ITEMS) - len(qua_han),
        "nguon_van_de": [s for s in demo.SOURCES if s["status"] != "ok"],
        "so_nguon": len(demo.SOURCES),
        "so_nguon_ok": sum(1 for s in demo.SOURCES if s["status"] == "ok"),
        "trang_thai_nguon": demo.TRANG_THAI_NGUON,
        "ai_hom_nay": demo.AI_7_NGAY[-1][1],
        "ai_pct": round(demo.AI_7_NGAY[-1][1] / demo.HAN_MUC_AI * 100),
        "han_muc_ai": demo.HAN_MUC_AI,
        "digest": demo.DIGEST,
        "telegram": demo.tom_tat_telegram(),
        "nhac_tu_khoa": [n for n in demo.LAN_NHAP_TU_KHOA if n[2] > 30],
    })


def ban_tin(request, ngay):
    if ngay != demo.HOM_NAY.isoformat():
        raise Http404("Bản mẫu chỉ có bản tin của ngày giả định 21/10/2026.")
    the_pro = demo.the_theo_luong("pro")
    the_pub = demo.the_theo_luong("public")
    return render(request, "quantri/ban_tin.html", {
        "trang": "hom_nay",
        "alerts": demo.ALERTS,
        "the_pro": the_pro,
        "the_pub": the_pub,
        "so_goi_y": len(the_pro) + len(the_pub),
        "van_ban_moi": [demo.van_ban(i) for i in demo.DIGEST["van_ban_moi_a"]],
        "sap_hieu_luc": [e for e in demo.CALENDAR if e["loai"] in ("Hiệu lực",) and 0 <= e["con_ngay"] <= 30],
        "du_thao": [demo.van_ban(103)],
        "digest": demo.DIGEST,
        "tong_hop": demo.TONG_HOP_7_NGAY,
        "chu_de_nhieu": demo.CHU_DE_DOI_THU_7_NGAY,
        "bai_tang": sorted([a for a in demo.COMPETITOR_ARTICLES if a["tang"]], key=lambda a: -a["tang"])[:5],
        "bai_loi_thoi": [a for a in demo.COMPETITOR_ARTICLES if a["loi_thoi"]],
        "cau_hoi_moi": demo.QUESTIONS[:5],
        "khoang_trong": demo.KHOANG_TRONG[:3],
        "review_items": demo.REVIEW_ITEMS,
        "nguon_van_de": [s for s in demo.SOURCES if s["status"] != "ok"],
        "trang_thai_nguon": demo.TRANG_THAI_NGUON,
        "telegram": demo.tom_tat_telegram(),
    })


def canh_bao(request, ma):
    alert = next((a for a in demo.ALERTS if a["ma"] == ma), None)
    if not alert:
        raise Http404("Không có tin Khẩn này.")
    return render(request, "quantri/canh_bao.html", {"trang": "hom_nay", "a": alert})


def goi_y(request, ma=None):
    chon = demo.the(ma) if ma else None
    if ma and not chon:
        raise Http404("Không có thẻ này.")
    return render(request, "quantri/goi_y.html", {
        "trang": "goi_y",
        "the_pro": demo.the_theo_luong("pro"),
        "the_pub": demo.the_theo_luong("public"),
        "the_chua_du": demo.the_chua_du_can_cu(),
        "chon": chon,
        "ho_so": demo.ho_so(chon) if chon else [],
        "ly_do_bo": demo.LY_DO_BO,
        "loai_the": demo.LOAI_THE,
        "trang_thai_the": demo.TRANG_THAI_THE,
    })


def doi_thu(request, tab):
    bai = demo.COMPETITOR_ARTICLES
    tong_hop = []
    for dv in demo.DON_VI_DOI_THU:
        so = demo.TONG_HOP_7_NGAY[dv]
        tong_hop.append({"don_vi": dv, "o": [so[k] for k in demo.COT_DANG_BAI], "tong": sum(so.values())})
    return render(request, "quantri/doi_thu.html", {
        "trang": "doi_thu",
        "tab": tab,
        "bai": sorted(bai, key=lambda a: (not a["moi"], a["don_vi"])),
        "tong_hop": tong_hop,
        "cot_dang_bai": [demo.DANG_BAI[k] for k in demo.COT_DANG_BAI],
        "chu_de_nhieu": demo.CHU_DE_DOI_THU_7_NGAY,
        "nguon_doi_thu": [s for s in demo.SOURCES if s["tier"] == "2b"],
        "trang_thai_nguon": demo.TRANG_THAI_NGUON,
        "cau_hoi": demo.QUESTIONS,
        "tinh_trang_can_cu": demo.TINH_TRANG_CAN_CU,
        "khoang_trong": demo.KHOANG_TRONG,
        "don_vi": demo.DON_VI_DOI_THU,
        "dang_bai": demo.DANG_BAI,
    })


def van_ban(request, tab):
    return render(request, "quantri/van_ban.html", {
        "trang": "van_ban",
        "tab": tab,
        "documents": demo.DOCUMENTS,
        "lich": demo.lich_theo_tuan(),
        "review_items": demo.REVIEW_ITEMS,
    })


def van_ban_chi_tiet(request, doc_id):
    d = demo.van_ban(doc_id)
    if not d:
        raise Http404("Không có văn bản này.")
    the_lien_quan = [c for c in demo.CARDS if c["document_id"] == doc_id]
    bai_lien_quan = [b for b in demo.FIRM_ARTICLES if any(d["number_normalized"] and d["number_normalized"] in v for v in b["vien_dan"])]
    moc = [e for e in demo.CALENDAR if e["document_id"] == doc_id]
    return render(request, "quantri/van_ban_chi_tiet.html", {
        "trang": "van_ban",
        "d": d,
        "the_lien_quan": the_lien_quan,
        "bai_lien_quan": bai_lien_quan,
        "moc": moc,
    })


def chu_de(request, tab):
    return render(request, "quantri/chu_de.html", {
        "trang": "chu_de",
        "tab": tab,
        "danh_muc_a": demo.danh_muc_a(),
        "danh_muc_b": demo.DANH_MUC_B,
        "tin_tuc": demo.CHU_DE_TIN_TUC,
        "kho_bai": demo.FIRM_ARTICLES,
        "tu_khoa": demo.KEYWORDS,
        "lan_nhap": demo.LAN_NHAP_TU_KHOA,
    })


def tin_hieu(request):
    return render(request, "quantri/tin_hieu.html", {"trang": "tin_hieu", "signals": demo.SIGNALS})


def dang_nhap(request):
    return render(request, "quantri/dang_nhap.html", {"trang": "dang_nhap"})


def robots(request):
    return HttpResponse("User-agent: *\nDisallow: /\n", content_type="text/plain")
