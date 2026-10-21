from django.urls import path

from . import views

urlpatterns = [
    path("", views.hom_nay, name="hom_nay"),
    path("ban-tin/<str:ngay>/", views.ban_tin, name="ban_tin"),
    path("canh-bao/<str:ma>/", views.canh_bao, name="canh_bao"),
    path("goi-y/", views.goi_y, name="goi_y"),
    path("goi-y/<str:ma>/", views.goi_y, name="goi_y_the"),
    path("doi-thu/", views.doi_thu, {"tab": "bai-moi"}, name="doi_thu"),
    path("doi-thu/tong-hop/", views.doi_thu, {"tab": "tong-hop"}, name="doi_thu_tong_hop"),
    path("doi-thu/cau-hoi/", views.doi_thu, {"tab": "cau-hoi"}, name="doi_thu_cau_hoi"),
    path("doi-thu/khoang-trong/", views.doi_thu, {"tab": "khoang-trong"}, name="doi_thu_khoang_trong"),
    path("van-ban/", views.van_ban, {"tab": "tra-cuu"}, name="van_ban"),
    path("van-ban/lich/", views.van_ban, {"tab": "lich"}, name="van_ban_lich"),
    path("van-ban/can-xem/", views.van_ban, {"tab": "can-xem"}, name="van_ban_can_xem"),
    path("van-ban/<int:doc_id>/", views.van_ban_chi_tiet, name="van_ban_chi_tiet"),
    path("chu-de/", views.chu_de, {"tab": "danh-muc"}, name="chu_de"),
    path("chu-de/kho-bai/", views.chu_de, {"tab": "kho-bai"}, name="chu_de_kho_bai"),
    path("chu-de/tu-khoa/", views.chu_de, {"tab": "tu-khoa"}, name="chu_de_tu_khoa"),
    path("tin-hieu/", views.tin_hieu, name="tin_hieu"),
    path("dang-nhap/", views.dang_nhap, name="dang_nhap"),
    path("robots.txt", views.robots, name="robots"),
]
