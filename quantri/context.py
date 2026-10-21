from . import demo

NAV = [
    ("hom_nay", "Hôm nay", "today"),
    ("goi_y", "Gợi ý", "pen"),
    ("doi_thu", "Đối thủ", "eye"),
    ("van_ban", "Văn bản", "doc"),
    ("chu_de", "Chủ đề", "tag"),
]


def chung(request):
    """Dữ liệu dùng chung cho khung trang: điều hướng, số đếm việc cần làm, ngày giả định."""
    dem = {
        "hom_nay": sum(1 for a in demo.ALERTS if a["status"] != "acknowledged"),
        "goi_y": len(demo.the_theo_luong("pro")) + len(demo.the_theo_luong("public")),
        "van_ban": len(demo.REVIEW_ITEMS),
    }
    return {
        "nav": [{"name": n, "ten": t, "icon": i, "dem": dem.get(n, 0)} for n, t, i in NAV],
        "hom_nay": demo.HOM_NAY,
        "thu_hom_nay": demo.THU_HOM_NAY,
        "ten_mien_cho_phep": demo.TEN_MIEN_CHO_PHEP,
        "danh_sach_chu_de": [(c["ma"], c["ten"]) for lv in demo.danh_muc_a() for c in lv["chu_de"]] + [(m, t) for m, t, _ in demo.DANH_MUC_B],
    }
