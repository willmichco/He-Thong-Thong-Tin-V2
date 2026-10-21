"""Kiểm thử bản mẫu giao diện: mọi màn hình dựng được và bản xuất một tệp đủ màn hình."""

import re

from django.test import SimpleTestCase

from quantri import demo
from quantri.management.commands.xuat_ban_mau import duong_dan_xuat, dung_ban_mau, ma_man_hinh


class ManHinhTest(SimpleTestCase):
    def test_moi_dia_chi_tra_ve_200(self):
        for path in duong_dan_xuat():
            with self.subTest(path=path):
                r = self.client.get(path)
                self.assertEqual(r.status_code, 200)
                self.assertContains(r, "Bản mẫu giao diện")
                self.assertEqual(r["X-Robots-Tag"], "noindex, nofollow")

    def test_noi_dung_chinh(self):
        cases = {
            "/": ["Cần xử lý trước", "Hôm nay nên viết gì", "Có gì mới", "Đối thủ viết gì", "Tình trạng hệ thống"],
            "/goi-y/": ["Chuyên môn", "Đại chúng", "Chưa đủ căn cứ"],
            "/doi-thu/tong-hop/": ["Đơn vị × dạng bài, 7 ngày"],
            "/van-ban/can-xem/": ["Hai nguồn Tầng 1 ghi khác nhau"],
            "/chu-de/": ["A-DD-01"],
        }
        for path, texts in cases.items():
            r = self.client.get(path)
            for t in texts:
                with self.subTest(path=path, text=t):
                    self.assertContains(r, t)

    def test_the_chua_du_can_cu_khong_cho_chon(self):
        card = next(c for c in demo.CARDS if not c["basis_verified"])
        r = self.client.get(f"/goi-y/{card['ma']}/")
        html = r.content.decode()
        chon = re.search(r'<button[^>]*data-action="select"[^>]*>', html).group(0)
        self.assertIn("disabled", chon)

    def test_hoi_dap_luon_o_luong_dai_chung(self):
        for c in demo.CARDS:
            if c["card_type"] == "qa":
                self.assertEqual(c["stream"], "public", c["ma"])

    def test_toa_do_svg_dung_dau_cham(self):
        # Ngôn ngữ vi định dạng số thực bằng dấu phẩy; tọa độ SVG phải giữ dấu chấm.
        html = self.client.get("/").content.decode()
        self.assertEqual(re.findall(r'\s(?:x|y|width|height)="\d+,\d+"', html), [])

    def test_dia_chi_khong_co_tra_ve_404(self):
        self.assertEqual(self.client.get("/goi-y/T-00000000-00/").status_code, 404)
        self.assertEqual(self.client.get("/van-ban/999/").status_code, 404)
        self.assertEqual(self.client.get("/ban-tin/2026-10-20/").status_code, 404)

    def test_robots_chan_toan_bo(self):
        r = self.client.get("/robots.txt")
        self.assertContains(r, "Disallow: /")


class BanXuatTest(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.out, cls.thieu = dung_ban_mau()

    def test_du_man_hinh(self):
        views = re.findall(r'<section data-view="([^"]+)"', self.out)
        self.assertEqual(views, [ma_man_hinh(p) for p in duong_dan_xuat()])

    def test_khong_con_lien_ket_noi_bo_tuyet_doi(self):
        self.assertEqual(self.thieu, set())
        self.assertEqual(re.findall(r'href="/', self.out), [])
        targets = set(re.findall(r'href="#([^"]+)"', self.out))
        self.assertTrue(targets <= set(re.findall(r'<section data-view="([^"]+)"', self.out)))

    def test_khong_trung_id(self):
        ids = re.findall(r'(?<![\w-])id="([^"]+)"', self.out)
        self.assertEqual(len(ids), len(set(ids)))

    def test_dang_mot_tep(self):
        self.assertNotIn("<!doctype", self.out.lower())
        self.assertNotIn("<body", self.out)
        self.assertIn('data-mode="static"', self.out)
        self.assertNotIn("<script src=", self.out)
        self.assertNotIn('rel="stylesheet" href="/', self.out)
