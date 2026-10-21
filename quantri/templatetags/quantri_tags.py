from django import template

from .. import demo

register = template.Library()


@register.filter
def ngay(d):
    """Ngày dạng dd/mm/yyyy (Phụ lục B.1)."""
    return d.strftime("%d/%m/%Y") if d else ""


@register.filter
def so(n):
    """Số có dấu chấm ngăn cách hàng nghìn: 12400 → 12.400."""
    if n is None:
        return "—"
    return f"{n:,}".replace(",", ".")


@register.filter
def con_lai(so_ngay):
    if so_ngay is None:
        return ""
    if so_ngay == 0:
        return "hôm nay"
    if so_ngay < 0:
        return f"đã qua {-so_ngay} ngày"
    return f"còn {so_ngay} ngày"


@register.filter
def ten_chu_de(ma):
    return demo.ten_chu_de(ma)


@register.filter
def lay(dct, key):
    return dct.get(key, "")
