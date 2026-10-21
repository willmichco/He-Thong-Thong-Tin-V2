"""Dữ liệu minh họa cho bản mẫu giao diện.

Tên trường theo Phụ lục A của Đặc tả 3.2, để khi nối cơ sở dữ liệu (Lát 1–3) chỉ cần
thay nguồn dữ liệu, giữ nguyên mẫu trang. Văn bản có số hiệu dạng "1xx/2026/…" là bịa
và luôn ghi "(minh họa)"; tên đối thủ và báo chí được ẩn danh vì tiêu đề bài là bịa.
Văn bản thật duy nhất ở đây là các bộ luật dùng làm căn cứ (Bộ luật Dân sự 2015,
Bộ luật Hình sự 2015, Luật Đất đai 2024).
"""

from datetime import date

HOM_NAY = date(2026, 10, 21)
THU_HOM_NAY = "Thứ Tư"


def con_ngay(d):
    return (d - HOM_NAY).days


MUC = {
    "urgent": {"ten": "Khẩn", "ky_hieu": "🔴", "lop": "urgent"},
    "important": {"ten": "Quan trọng", "ky_hieu": "🟠", "lop": "important"},
    "watch": {"ten": "Theo dõi", "ky_hieu": "🔵", "lop": "watch"},
    "reference": {"ten": "Tham khảo", "ky_hieu": "⚪", "lop": "reference"},
}
LOAI_THE = {"hot": "Tin nóng", "due": "Đến hạn", "gap": "Khoảng trống", "news": "Tin tức", "qa": "Hỏi đáp"}
LUONG = {"pro": "Chuyên môn", "public": "Đại chúng"}
TRANG_THAI_THE = {
    "proposed": "Đề xuất",
    "selected": "Đã chọn",
    "dropped": "Đã bỏ",
    "written": "Đã viết",
    "published": "Đã đăng",
}
TINH_TRANG_HIEU_LUC = {
    "draft": "Dự thảo",
    "not_yet_effective": "Chưa có hiệu lực",
    "in_force": "Còn hiệu lực",
    "partially_expired": "Hết hiệu lực một phần",
    "expired": "Hết hiệu lực",
    "suspended": "Ngưng hiệu lực",
    "partially_suspended": "Ngưng hiệu lực một phần",
    "unknown": "Chưa xác định",
}
DANG_BAI = {
    "qa": "Hỏi đáp",
    "new_doc": "Tin văn bản mới",
    "form": "Mẫu đơn",
    "procedure": "Hướng dẫn thủ tục",
    "commentary": "Bình luận",
    "other": "Khác",
}
LY_DO_BO = [
    ("duplicate", "Trùng"),
    ("off_practice", "Không hợp chuyên môn"),
    ("low_interest", "Ít người quan tâm"),
    ("insufficient_basis", "Chưa đủ căn cứ"),
    ("other", "Khác (ghi chú bắt buộc)"),
]

# Danh sách tên miền và danh sách trắng cho ô "+ Dán link" (mục 9).
TEN_MIEN_CHO_PHEP = [
    "facebook.com", "fb.watch", "tiktok.com", "youtube.com", "youtu.be",
    "congbao.chinhphu.vn", "vbpl.vn", "phapluat.gov.vn", "quochoi.vn", "chinhphu.vn",
    "vnexpress.net", "tuoitre.vn", "thanhnien.vn", "nld.com.vn", "plo.vn",
    "baochinhphu.vn", "daibieunhandan.vn", "baophapluat.vn", "thuvienphapluat.vn", "luatvietnam.vn",
]

# ---------------------------------------------------------------- Nguồn (sources)

SOURCES = [
    {"code": "congbao", "name": "Công báo", "tier": "1", "channel_kind": "static", "last_success": "08:31", "stability": 99, "coverage": None, "status": "ok", "note": ""},
    {"code": "vbpl", "name": "CSDL quốc gia về pháp luật (vbpl.vn)", "tier": "1", "channel_kind": "static", "last_success": "08:30", "stability": 98, "coverage": None, "status": "ok", "note": ""},
    {"code": "phapluat", "name": "Cổng Pháp luật quốc gia", "tier": "1", "channel_kind": "js", "last_success": "08:02", "stability": 95, "coverage": None, "status": "ok", "note": ""},
    {"code": "quochoi", "name": "quochoi.vn", "tier": "1", "channel_kind": "static", "last_success": "08:05", "stability": 97, "coverage": None, "status": "ok", "note": ""},
    {"code": "congbao-hcm", "name": "Công báo TP.HCM", "tier": "1", "channel_kind": "static", "last_success": "07:10", "stability": 88, "coverage": None, "status": "error", "note": "Lỗi 2 lượt liên tiếp từ 08:10: trang trả về trang bảo trì"},
    {"code": "bao-a", "name": "Báo pháp luật A", "tier": "2", "channel_kind": "rss", "last_success": "08:20", "stability": 100, "coverage": None, "status": "ok", "note": ""},
    {"code": "bao-b", "name": "Báo đại chúng B", "tier": "2", "channel_kind": "rss", "last_success": "08:15", "stability": 100, "coverage": None, "status": "ok", "note": ""},
    {"code": "doi-thu-a", "name": "Đối thủ A", "tier": "2b", "channel_kind": "sitemap", "last_success": "06:00", "stability": 100, "coverage": 94, "status": "ok", "note": ""},
    {"code": "doi-thu-b", "name": "Đối thủ B", "tier": "2b", "channel_kind": "sitemap", "last_success": "06:00", "stability": 96, "coverage": 76, "status": "low_coverage", "note": "Độ phủ 76%: sitemap thiếu bài chuyên mục Hỏi đáp"},
    {"code": "doi-thu-c", "name": "Đối thủ C", "tier": "2b", "channel_kind": "manual", "last_success": "19/10 06:00", "stability": 61, "coverage": None, "status": "manual", "note": "Đang dán link tay: trang chặn máy đọc từ 19/10"},
    {"code": "doi-thu-e", "name": "Đối thủ E", "tier": "2b", "channel_kind": "rss", "last_success": "06:00", "stability": 100, "coverage": 100, "status": "silent", "note": "Im lặng bất thường: 3 ngày không có bài mới (thường 1 bài/ngày)"},
    {"code": "du-lieu-1", "name": "Đơn vị dữ liệu 1", "tier": "2b", "channel_kind": "sitemap", "last_success": "06:00", "stability": 100, "coverage": 91, "status": "ok", "note": ""},
]

TRANG_THAI_NGUON = {
    "ok": "Bình thường",
    "error": "Lỗi",
    "silent": "Im lặng bất thường",
    "low_coverage": "Độ phủ thấp",
    "manual": "Đang dán link tay",
}
KENH = {"rss": "RSS", "sitemap": "Sitemap", "embedded": "Dữ liệu nhúng", "static": "Trang danh sách", "js": "Playwright", "manual": "Dán link tay"}

# ---------------------------------------------------------------- Văn bản (documents)

DOCUMENTS = [
    {
        "id": 101,
        "issuer_name": "Chính phủ",
        "number_normalized": "1xx/2026/NĐ-CP",
        "minh_hoa": True,
        "doc_type": "Nghị định",
        "is_draft": False,
        "signed_date": date(2026, 10, 1),
        "effective_date": date(2026, 11, 15),
        "comment_deadline": None,
        "title_summary": "Quy định chi tiết về đăng ký đất đai, cấp Giấy chứng nhận quyền sử dụng đất lần đầu",
        "fields": ["Đất đai"],
        "group_ab": "A",
        "legal_status": "not_yet_effective",
        "basis_label": "verified",
        "source": "Công báo",
        "collected": "09:05 02/10/2026",
        "relations": [
            {"relation": "Thay thế một phần", "other": "1yy/2024/NĐ-CP (minh họa)", "scope": "Chương II", "excerpt": "Bãi bỏ Chương II Nghị định số 1yy/2024/NĐ-CP…"},
        ],
        "excerpts": {
            "effective_date": "Nghị định này có hiệu lực thi hành từ ngày 15 tháng 11 năm 2026.",
            "signed_date": "Hà Nội, ngày 01 tháng 10 năm 2026",
            "number": "Số: 1xx/2026/NĐ-CP",
        },
        "ai_summary": [
            ("Bỏ yêu cầu nộp bản sao giấy tờ đã có trong cơ sở dữ liệu quốc gia về dân cư", "Điều 8"),
            ("Rút thời hạn cấp Giấy chứng nhận lần đầu xuống 15 ngày làm việc", "Điều 12"),
            ("Cho phép nộp hồ sơ trực tuyến toàn trình tại TP.HCM và Hà Nội", "Điều 20"),
        ],
        "files": [
            {"seq": 1, "reason": "Lần đầu", "source": "Công báo", "fetched": "09:05 02/10/2026", "sha": "9f2c…41ab", "method": "Chữ trong tệp"},
            {"seq": 2, "reason": "Cùng văn bản từ nguồn Tầng 1 thứ hai", "source": "vbpl.vn", "fetched": "14:30 02/10/2026", "sha": "77d0…c912", "method": "Chữ trong tệp"},
        ],
    },
    {
        "id": 102,
        "issuer_name": "Bộ Nội vụ",
        "number_normalized": "2xx/2026/TT-BNV",
        "minh_hoa": True,
        "doc_type": "Thông tư",
        "is_draft": False,
        "signed_date": date(2026, 10, 15),
        "effective_date": date(2026, 12, 1),
        "comment_deadline": None,
        "title_summary": "Hướng dẫn giao kết hợp đồng lao động bằng phương tiện điện tử",
        "fields": ["Lao động"],
        "group_ab": "A",
        "legal_status": "not_yet_effective",
        "basis_label": "verified",
        "source": "Công báo",
        "collected": "10:12 20/10/2026",
        "relations": [],
        "excerpts": {
            "effective_date": "Thông tư này có hiệu lực thi hành từ ngày 01 tháng 12 năm 2026.",
            "signed_date": "Hà Nội, ngày 15 tháng 10 năm 2026",
            "number": "Số: 2xx/2026/TT-BNV",
        },
        "ai_summary": [
            ("Hợp đồng điện tử phải ký bằng chữ ký số hoặc chữ ký điện tử có xác thực", "Điều 4"),
            ("Người sử dụng lao động phải lưu trữ hợp đồng ít nhất 10 năm", "Điều 7"),
            ("Người lao động được nhận bản hợp đồng qua thư điện tử hoặc ứng dụng", "Điều 9"),
        ],
        "files": [
            {"seq": 1, "reason": "Lần đầu", "source": "Công báo", "fetched": "10:12 20/10/2026", "sha": "1b8e…02fd", "method": "Chữ trong tệp"},
        ],
    },
    {
        "id": 103,
        "issuer_name": "Bộ Tài chính (cơ quan soạn thảo)",
        "number_normalized": "",
        "minh_hoa": True,
        "doc_type": "Dự thảo Nghị định",
        "is_draft": True,
        "signed_date": None,
        "effective_date": None,
        "comment_deadline": date(2026, 11, 5),
        "title_summary": "Dự thảo Nghị định về đăng ký hộ kinh doanh",
        "fields": ["Kinh doanh thương mại"],
        "group_ab": "A",
        "legal_status": "draft",
        "basis_label": "verified",
        "source": "Cổng Pháp luật quốc gia",
        "collected": "08:02 21/10/2026",
        "relations": [],
        "excerpts": {"comment_deadline": "Thời hạn lấy ý kiến: đến hết ngày 05/11/2026."},
        "ai_summary": [
            ("Hộ kinh doanh đăng ký trực tuyến không cần nộp bản giấy", "Điều 6"),
            ("Bỏ giới hạn một hộ kinh doanh chỉ đăng ký một địa điểm", "Điều 10"),
        ],
        "files": [
            {"seq": 1, "reason": "Lần đầu", "source": "Cổng Pháp luật quốc gia", "fetched": "08:02 21/10/2026", "sha": "c4a1…9e07", "method": "Chữ trong tệp"},
        ],
    },
    {
        "id": 104,
        "issuer_name": "UBND TP.HCM",
        "number_normalized": "xx/2026/QĐ-UBND",
        "minh_hoa": True,
        "doc_type": "Quyết định",
        "is_draft": False,
        "signed_date": date(2026, 10, 16),
        "effective_date": None,
        "comment_deadline": None,
        "title_summary": "Điều chỉnh bảng giá đất trên địa bàn Thành phố Hồ Chí Minh",
        "fields": ["Đất đai"],
        "group_ab": "A",
        "legal_status": "unknown",
        "basis_label": "unverified",
        "basis_note": "Công báo TP.HCM ghi hiệu lực 01/11/2026, vbpl.vn ghi 15/11/2026",
        "source": "Công báo TP.HCM",
        "collected": "16:40 20/10/2026",
        "relations": [],
        "excerpts": {},
        "ai_summary": [],
        "files": [
            {"seq": 1, "reason": "Lần đầu", "source": "Công báo TP.HCM", "fetched": "16:40 20/10/2026", "sha": "5e3b…aa10", "method": "OCR (điểm dấu 91)"},
            {"seq": 2, "reason": "Cùng văn bản từ nguồn Tầng 1 thứ hai", "source": "vbpl.vn", "fetched": "07:30 21/10/2026", "sha": "0c62…7f44", "method": "Chữ trong tệp"},
        ],
    },
    {
        "id": 105,
        "issuer_name": "Bộ Công an",
        "number_normalized": "4xx/2026/TT-BCA",
        "minh_hoa": True,
        "doc_type": "Thông tư",
        "is_draft": False,
        "signed_date": date(2026, 10, 10),
        "effective_date": date(2026, 12, 1),
        "comment_deadline": None,
        "title_summary": "Quy định về cấp, đổi, thu hồi giấy phép lái xe",
        "fields": ["Giao thông"],
        "group_ab": "B",
        "legal_status": "not_yet_effective",
        "basis_label": "unverified",
        "basis_note": "Bản PDF scan, không tìm thấy câu hiệu lực khớp (OCR 82 điểm)",
        "source": "Công báo",
        "collected": "15:00 19/10/2026",
        "relations": [],
        "excerpts": {},
        "ai_summary": [],
        "files": [
            {"seq": 1, "reason": "Lần đầu", "source": "Công báo", "fetched": "15:00 19/10/2026", "sha": "a91d…3c58", "method": "OCR (điểm dấu 82)"},
        ],
    },
    {
        "id": 106,
        "issuer_name": "Chính phủ",
        "number_normalized": "3xx/2025/NĐ-CP",
        "minh_hoa": True,
        "doc_type": "Nghị định",
        "is_draft": False,
        "signed_date": date(2025, 12, 20),
        "effective_date": date(2026, 2, 1),
        "comment_deadline": None,
        "title_summary": "Quy định về hồ sơ đăng ký đất đai",
        "fields": ["Đất đai"],
        "group_ab": "A",
        "legal_status": "in_force",
        "basis_label": "verified",
        "source": "Công báo",
        "collected": "10:00 22/12/2025",
        "relations": [
            {"relation": "Bị đính chính", "other": "Văn bản đính chính (minh họa) ngày 20/10/2026", "scope": "khoản 2 Điều 9", "excerpt": "Đính chính khoản 2 Điều 9: thay cụm từ \"bản sao có chứng thực\" bằng \"bản sao\"…"},
        ],
        "excerpts": {"effective_date": "Nghị định này có hiệu lực thi hành từ ngày 01 tháng 02 năm 2026."},
        "ai_summary": [],
        "files": [
            {"seq": 1, "reason": "Lần đầu", "source": "Công báo", "fetched": "10:00 22/12/2025", "sha": "2d77…b001", "method": "Chữ trong tệp"},
            {"seq": 2, "reason": "Bản đính chính", "source": "Công báo", "fetched": "09:40 20/10/2026", "sha": "8e10…d6c3", "method": "Chữ trong tệp"},
        ],
    },
    {
        "id": 201,
        "issuer_name": "Quốc hội",
        "number_normalized": "91/2015/QH13",
        "minh_hoa": False,
        "doc_type": "Bộ luật",
        "is_draft": False,
        "signed_date": date(2015, 11, 24),
        "effective_date": date(2017, 1, 1),
        "comment_deadline": None,
        "title_summary": "Bộ luật Dân sự",
        "fields": ["Dân sự"],
        "group_ab": "A",
        "legal_status": "in_force",
        "basis_label": "verified",
        "source": "vbpl.vn",
        "collected": "Tra theo số hiệu, 07:00 20/10/2026",
        "relations": [
            {"relation": "Thay thế", "other": "Bộ luật Dân sự 33/2005/QH11", "scope": "", "excerpt": "Bộ luật Dân sự số 33/2005/QH11 hết hiệu lực kể từ ngày Bộ luật này có hiệu lực."},
        ],
        "excerpts": {"effective_date": "Bộ luật này có hiệu lực thi hành từ ngày 01 tháng 01 năm 2017."},
        "ai_summary": [],
        "files": [
            {"seq": 1, "reason": "Lần đầu", "source": "vbpl.vn", "fetched": "07:00 20/10/2026", "sha": "f1e2…8a90", "method": "Chữ trong tệp"},
        ],
    },
    {
        "id": 202,
        "issuer_name": "Quốc hội",
        "number_normalized": "31/2024/QH15",
        "minh_hoa": False,
        "doc_type": "Luật",
        "is_draft": False,
        "signed_date": date(2024, 1, 18),
        "effective_date": date(2024, 8, 1),
        "comment_deadline": None,
        "title_summary": "Luật Đất đai",
        "fields": ["Đất đai"],
        "group_ab": "A",
        "legal_status": "in_force",
        "basis_label": "verified",
        "source": "vbpl.vn",
        "collected": "Tra theo số hiệu, 07:00 20/10/2026",
        "has_partial_effect": True,
        "partial_effects": [("Điều 190 và Điều 248", date(2024, 4, 1))],
        "relations": [],
        "excerpts": {},
        "ai_summary": [],
        "files": [
            {"seq": 1, "reason": "Lần đầu", "source": "vbpl.vn", "fetched": "07:00 20/10/2026", "sha": "3b9a…11ce", "method": "Chữ trong tệp"},
        ],
    },
    {
        "id": 203,
        "issuer_name": "Quốc hội",
        "number_normalized": "100/2015/QH13",
        "minh_hoa": False,
        "doc_type": "Bộ luật",
        "is_draft": False,
        "signed_date": date(2015, 11, 27),
        "effective_date": date(2018, 1, 1),
        "comment_deadline": None,
        "title_summary": "Bộ luật Hình sự",
        "fields": ["Hình sự"],
        "group_ab": "A",
        "legal_status": "in_force",
        "basis_label": "verified",
        "source": "vbpl.vn",
        "collected": "Tra theo số hiệu, 07:00 20/10/2026",
        "relations": [],
        "excerpts": {},
        "ai_summary": [],
        "files": [
            {"seq": 1, "reason": "Lần đầu", "source": "vbpl.vn", "fetched": "07:00 20/10/2026", "sha": "6c40…e2a7", "method": "Chữ trong tệp"},
        ],
    },
]


def van_ban(doc_id):
    for d in DOCUMENTS:
        if d["id"] == doc_id:
            return d
    return None


def so_hieu(d):
    if d["is_draft"]:
        return "Dự thảo"
    return d["number_normalized"] + (" (minh họa)" if d["minh_hoa"] else "")


for _d in DOCUMENTS:
    _d["so_hieu"] = so_hieu(_d)
    _d["tinh_trang"] = TINH_TRANG_HIEU_LUC[_d["legal_status"]]
    _d.setdefault("has_partial_effect", False)
    _d.setdefault("partial_effects", [])
    _d.setdefault("basis_note", "")
    if _d["effective_date"]:
        _d["con_ngay_hieu_luc"] = con_ngay(_d["effective_date"])

# ---------------------------------------------------------------- Thẻ gợi ý (suggestion_cards + card_facts)

CARDS = [
    {
        "ma": "T-20261021-01",
        "card_type": "due",
        "stream": "pro",
        "alert_level": "important",
        "rank_in_stream": 1,
        "basis_verified": True,
        "status": "proposed",
        "document_id": 101,
        "topic_code": "A-DD-01",
        "title_options": [
            "Từ 15/11/2026, thủ tục cấp sổ đỏ lần đầu thay đổi thế nào?",
            "Cấp sổ đỏ lần đầu: 3 điểm mới người dân cần biết",
            "Chuẩn bị hồ sơ cấp sổ đỏ lần đầu trước ngày 15/11/2026",
        ],
        "angle": "Ai bị ảnh hưởng – cần làm gì – trước ngày nào",
        "moc": "Hiệu lực 15/11/2026",
        "moc_date": date(2026, 11, 15),
        "n_bao": 4,
        "n_doi_thu": 2,
        "quan_tam": "\"cấp sổ đỏ lần đầu\" tăng 35% trên Google Trends",
        "seo_primary": "thủ tục cấp sổ đỏ lần đầu",
        "seo_secondary": ["hồ sơ cấp sổ đỏ lần đầu", "lệ phí cấp sổ đỏ", "cấp sổ đỏ lần đầu mất bao lâu"],
        "fb_hook": "Đất ông bà để lại chưa có sổ, từ tháng 11 làm sổ lần đầu có gì khác?",
        "fb_hook_sources": 5,
        "doi_thu": [
            {"don_vi": "Đối thủ A", "dang": "Hỏi đáp", "ngay": "20/10/2026", "loi_thoi": False},
            {"don_vi": "Đối thủ B", "dang": "Hướng dẫn thủ tục", "ngay": "02/2025", "loi_thoi": True},
        ],
        "nen_tang": [
            ("Website", "Bài chính chuẩn SEO theo từ khóa chính"),
            ("Facebook", "Bài dẫn kèm câu mồi; link ở bình luận đầu"),
            ("Video ngắn", "\"Trước 15/11 cần chuẩn bị gì để làm sổ lần đầu?\""),
        ],
        "dang_tot_nhat": "Trước 08/11/2026",
        "case_in_progress": False,
        "cau_hoi": [("Làm sổ đỏ lần đầu cần giấy tờ gì?", 5), ("Đất chưa có sổ có bán được không?", 5)],
        "lich_su": [],
    },
    {
        "ma": "T-20261021-02",
        "card_type": "hot",
        "stream": "pro",
        "alert_level": "important",
        "rank_in_stream": 2,
        "basis_verified": True,
        "status": "proposed",
        "document_id": 102,
        "topic_code": "A-LD-01",
        "title_options": [
            "Hợp đồng lao động điện tử: 3 điểm mới người lao động cần biết",
            "Ký hợp đồng lao động qua điện thoại có hợp pháp không?",
            "Từ 01/12/2026, hợp đồng lao động điện tử phải ký thế nào?",
        ],
        "angle": "Điểm mới – ai bị ảnh hưởng – áp dụng từ khi nào",
        "moc": "Hiệu lực 01/12/2026",
        "moc_date": date(2026, 12, 1),
        "n_bao": 3,
        "n_doi_thu": 2,
        "quan_tam": "",
        "seo_primary": "hợp đồng lao động điện tử",
        "seo_secondary": ["ký hợp đồng lao động online", "chữ ký số hợp đồng lao động", "lưu trữ hợp đồng lao động"],
        "fb_hook": "Công ty gửi hợp đồng qua Zalo bảo bấm đồng ý là xong, có đúng luật không?",
        "fb_hook_sources": 3,
        "doi_thu": [
            {"don_vi": "Đối thủ D", "dang": "Hỏi đáp", "ngay": "19/10/2026", "loi_thoi": False},
            {"don_vi": "Đơn vị dữ liệu 2", "dang": "Tin văn bản mới", "ngay": "20/10/2026", "loi_thoi": False},
        ],
        "nen_tang": [
            ("Website", "Bài chính"),
            ("Facebook", "Bài dẫn"),
            ("Video ngắn", "Khi ảnh hưởng nhiều người: \"3 điều cần kiểm tra trước khi bấm ký\""),
        ],
        "dang_tot_nhat": "Trước 23/10/2026",
        "case_in_progress": False,
        "cau_hoi": [("Hợp đồng lao động điện tử có cần ký tay không?", 3)],
        "lich_su": [],
    },
    {
        "ma": "T-20261021-03",
        "card_type": "due",
        "stream": "pro",
        "alert_level": "watch",
        "rank_in_stream": 3,
        "basis_verified": True,
        "status": "selected",
        "document_id": 103,
        "topic_code": "A-KD-01",
        "title_options": [
            "Dự thảo mới về hộ kinh doanh: góp ý trước 05/11/2026, những gì sẽ thay đổi?",
            "Dự thảo mới về hộ kinh doanh: 2 điểm chủ hộ cần biết",
            "Hộ kinh doanh sắp được đăng ký nhiều địa điểm?",
        ],
        "angle": "Ai bị ảnh hưởng – cần làm gì – trước ngày nào",
        "moc": "Hạn góp ý 05/11/2026",
        "moc_date": date(2026, 11, 5),
        "n_bao": 2,
        "n_doi_thu": 1,
        "quan_tam": "",
        "seo_primary": "đăng ký hộ kinh doanh",
        "seo_secondary": ["thủ tục đăng ký hộ kinh doanh", "hộ kinh doanh nhiều địa điểm", "dự thảo hộ kinh doanh"],
        "fb_hook": "Bán hàng online có phải đăng ký hộ kinh doanh không?",
        "fb_hook_sources": 4,
        "doi_thu": [
            {"don_vi": "Đối thủ E", "dang": "Hướng dẫn thủ tục", "ngay": "18/10/2026", "loi_thoi": False},
        ],
        "nen_tang": [
            ("Website", "Bài chính"),
            ("Facebook", "Bài dẫn"),
            ("Video ngắn", "\"Trước 05/11 chủ hộ kinh doanh nên góp ý điều gì?\""),
        ],
        "dang_tot_nhat": "Trước 29/10/2026",
        "case_in_progress": False,
        "cau_hoi": [("Bán hàng online có phải đăng ký hộ kinh doanh không?", 4)],
        "lich_su": [("Đã chọn", "08:12 21/10", "")],
    },
    {
        "ma": "T-20261021-04",
        "card_type": "gap",
        "stream": "pro",
        "alert_level": "reference",
        "rank_in_stream": 4,
        "basis_verified": True,
        "status": "proposed",
        "document_id": 201,
        "topic_code": "A-DD-04",
        "title_options": [
            "Tranh chấp lối đi chung: hướng dẫn theo quy định hiện hành",
            "Bị hàng xóm bịt lối đi: làm gì để giữ quyền đi qua?",
            "Quyền về lối đi qua: khi nào được yêu cầu mở lối đi?",
        ],
        "angle": "Quy định hiện hành – thủ tục tại TP.HCM – kinh nghiệm thực tế",
        "moc": "",
        "moc_date": None,
        "n_bao": 1,
        "n_doi_thu": 3,
        "quan_tam": "3 đối thủ đã viết trong 30 ngày, văn phòng chưa có bài",
        "seo_primary": "tranh chấp lối đi chung",
        "seo_secondary": ["quyền về lối đi qua", "hàng xóm bịt lối đi", "khởi kiện tranh chấp lối đi"],
        "fb_hook": "Hàng xóm xây tường bịt lối đi duy nhất ra đường, nhà tôi phải làm sao?",
        "fb_hook_sources": 3,
        "doi_thu": [
            {"don_vi": "Đối thủ F", "dang": "Hỏi đáp", "ngay": "15/10/2026", "loi_thoi": False},
            {"don_vi": "Đối thủ A", "dang": "Hỏi đáp", "ngay": "02/10/2026", "loi_thoi": False},
        ],
        "nen_tang": [
            ("Website", "Bài nền chuẩn SEO"),
            ("Facebook", "Dẫn về bài website"),
        ],
        "dang_tot_nhat": "Không gấp",
        "case_in_progress": False,
        "cau_hoi": [("Tranh chấp lối đi chung kiện ở đâu?", 3)],
        "lich_su": [],
    },
    {
        "ma": "T-20261021-05",
        "card_type": "qa",
        "stream": "public",
        "alert_level": "reference",
        "rank_in_stream": 1,
        "basis_verified": True,
        "status": "proposed",
        "document_id": 201,
        "topic_code": "A-DD-02",
        "title_options": [
            "Bị bùng cọc khi mua đất: lấy lại tiền cọc thế nào?",
            "Bên bán bùng cọc mua đất, người mua được bồi thường bao nhiêu?",
            "Mất cọc, bùng cọc khi mua đất: quy định hiện hành và cách xử lý",
        ],
        "angle": "Trả lời ngắn – căn cứ hiện hành – điểm khác với bài đã có",
        "moc": "",
        "moc_date": None,
        "n_bao": 1,
        "n_doi_thu": 3,
        "quan_tam": "6 nguồn cùng hỏi · bài đối thủ xem nhiều nhất tăng 28% trong 24 giờ",
        "seo_primary": "bùng cọc mua đất",
        "seo_secondary": ["mất cọc mua đất", "phạt cọc mua đất", "đòi lại tiền cọc"],
        "fb_hook": "Đặt cọc 200 triệu mua đất, bên bán đổi ý không bán nữa thì sao?",
        "fb_hook_sources": 6,
        "doi_thu": [
            {"don_vi": "Đối thủ A", "dang": "Hỏi đáp", "ngay": "20/10/2026", "loi_thoi": False},
            {"don_vi": "Đối thủ C", "dang": "Hỏi đáp", "ngay": "11/2023", "loi_thoi": True},
        ],
        "nen_tang": [
            ("Website", "Bài chính"),
            ("Facebook", "Bài dẫn"),
            ("Video ngắn", "Hỏi–đáp 60 giây"),
        ],
        "dang_tot_nhat": "Không gấp",
        "goc_khac_biet": "Quy định hiện hành · thực tế giải quyết tại TP.HCM · kinh nghiệm của văn phòng",
        "case_in_progress": False,
        "cau_hoi": [("Bị bùng cọc khi mua đất có lấy lại được tiền không?", 6)],
        "lich_su": [],
    },
    {
        "ma": "T-20261021-06",
        "card_type": "news",
        "stream": "public",
        "alert_level": "reference",
        "rank_in_stream": 2,
        "basis_verified": True,
        "status": "proposed",
        "document_id": 203,
        "topic_code": "A-HS-01",
        "title_options": [
            "Giả danh cán bộ thuế gọi điện lừa đảo: pháp luật xử lý thế nào?",
            "Nhận cuộc gọi \"cán bộ thuế\" yêu cầu chuyển tiền: làm gì để không mất tiền?",
            "Lừa đảo giả danh cơ quan nhà nước bị phạt tù bao nhiêu năm?",
        ],
        "angle": "Sự kiện – quy định áp dụng – giới hạn bình luận",
        "moc": "",
        "moc_date": None,
        "n_bao": 3,
        "n_doi_thu": 1,
        "quan_tam": "3 báo đưa tin trong 24 giờ (minh họa)",
        "seo_primary": "lừa đảo giả danh cán bộ thuế",
        "seo_secondary": ["lừa đảo qua điện thoại", "tội lừa đảo chiếm đoạt tài sản", "báo công an khi bị lừa"],
        "fb_hook": "Có người tự xưng cán bộ thuế gọi bảo cài ứng dụng để \"hoàn thuế\", có nên làm theo?",
        "fb_hook_sources": 4,
        "doi_thu": [
            {"don_vi": "Đối thủ D", "dang": "Hỏi đáp", "ngay": "20/10/2026", "loi_thoi": False},
        ],
        "nen_tang": [
            ("Facebook", "Đăng trước, câu mồi cảnh báo"),
            ("Website", "Bài chính sau"),
            ("Video ngắn", "Khi sự kiện nóng: \"3 dấu hiệu cuộc gọi lừa đảo\""),
        ],
        "dang_tot_nhat": "Trong 24 giờ (trước 22/10/2026)",
        "case_in_progress": True,
        "cau_hoi": [("Bị lừa đảo qua mạng báo ai?", 4)],
        "lich_su": [],
        "su_kien": "Nhiều người dân nhận cuộc gọi giả danh cán bộ thuế, yêu cầu cài ứng dụng để \"hoàn thuế\" (minh họa).",
        "bai_bao": [("Báo đại chúng B", "21/10/2026"), ("Báo pháp luật A", "20/10/2026"), ("Báo đại chúng D", "20/10/2026")],
    },
    {
        "ma": "T-20261021-07",
        "card_type": "hot",
        "stream": "public",
        "alert_level": "reference",
        "rank_in_stream": None,
        "basis_verified": False,
        "basis_note": "Chưa có văn bản gốc: mới thấy trên 2 báo, chưa có trên Tầng 1",
        "status": "proposed",
        "document_id": None,
        "topic_code": "B-GT",
        "title_options": [
            "Đề xuất tăng mức phạt vi phạm nồng độ cồn (minh họa): những gì đã biết",
            "Phạt nồng độ cồn sắp tăng? Quy định hiện hành ra sao",
            "Đề xuất mới về xử phạt nồng độ cồn (minh họa)",
        ],
        "angle": "Điểm mới – ai bị ảnh hưởng – áp dụng từ khi nào",
        "moc": "",
        "moc_date": None,
        "n_bao": 2,
        "n_doi_thu": 0,
        "quan_tam": "",
        "seo_primary": "phạt nồng độ cồn",
        "seo_secondary": [],
        "fb_hook": "",
        "fb_hook_sources": 0,
        "doi_thu": [],
        "nen_tang": [("Website", "Bài chính"), ("Facebook", "Bài dẫn")],
        "dang_tot_nhat": "Trong 48 giờ",
        "case_in_progress": False,
        "cau_hoi": [],
        "lich_su": [],
        "can_xem": None,
    },
    {
        "ma": "T-20261021-08",
        "card_type": "due",
        "stream": "pro",
        "alert_level": "important",
        "rank_in_stream": None,
        "basis_verified": False,
        "basis_note": "Hai nguồn Tầng 1 ghi khác ngày hiệu lực (01/11 và 15/11/2026)",
        "status": "proposed",
        "document_id": 104,
        "topic_code": "A-DD-06",
        "title_options": [
            "Bảng giá đất TP.HCM điều chỉnh (minh họa): tiền thuế khi sang tên thay đổi thế nào?",
            "Bảng giá đất mới tại TP.HCM: ai phải nộp nhiều hơn?",
            "Sang tên nhà đất ở TP.HCM sau khi điều chỉnh bảng giá đất",
        ],
        "angle": "Ai bị ảnh hưởng – cần làm gì – trước ngày nào",
        "moc": "Hiệu lực chưa rõ",
        "moc_date": None,
        "n_bao": 5,
        "n_doi_thu": 2,
        "quan_tam": "",
        "seo_primary": "bảng giá đất TP.HCM",
        "seo_secondary": ["thuế sang tên nhà đất", "bảng giá đất mới"],
        "fb_hook": "",
        "fb_hook_sources": 0,
        "doi_thu": [],
        "nen_tang": [("Website", "Bài chính"), ("Facebook", "Bài dẫn")],
        "dang_tot_nhat": "—",
        "case_in_progress": False,
        "cau_hoi": [],
        "lich_su": [],
        "can_xem": "R-1",
    },
]

for _c in CARDS:
    _c["loai"] = LOAI_THE[_c["card_type"]]
    _c["luong"] = LUONG[_c["stream"]]
    _c["muc"] = MUC[_c["alert_level"]]
    _c["trang_thai"] = TRANG_THAI_THE[_c["status"]]
    _c["tieu_de"] = _c["title_options"][0]
    _c.setdefault("basis_note", "")
    _c.setdefault("goc_khac_biet", "")
    _c["van_ban"] = van_ban(_c["document_id"]) if _c["document_id"] else None
    if _c["moc_date"]:
        _c["moc_con_ngay"] = con_ngay(_c["moc_date"])


def the(ma):
    for c in CARDS:
        if c["ma"] == ma:
            return c
    return None


def the_theo_luong(stream, verified=True):
    rows = [c for c in CARDS if c["stream"] == stream and c["basis_verified"] == verified]
    return sorted(rows, key=lambda c: c["rank_in_stream"] or 99)


def the_chua_du_can_cu():
    return [c for c in CARDS if not c["basis_verified"]]


def ho_so(card):
    """Dữ kiện của thẻ (card_facts), theo mẫu B.6."""
    d = card["van_ban"]
    rows = []
    if card["card_type"] == "news":
        rows.append({"truong": "Sự kiện", "gia_tri": card["su_kien"], "trich": "", "nguon": "3 báo (xem mục 4)", "luc": "21/10/2026", "nhan": "verified"})
    if d:
        ex = d["excerpts"]
        verified = d["basis_label"] == "verified"
        rows.append({"truong": "Số hiệu", "gia_tri": d["so_hieu"], "trich": ex.get("number", ""), "nguon": d["source"], "luc": d["collected"], "nhan": "verified" if verified else "unverified"})
        rows.append({"truong": "Cơ quan, loại", "gia_tri": f'{d["issuer_name"]} · {d["doc_type"]}', "trich": "", "nguon": d["source"], "luc": d["collected"], "nhan": "verified" if verified else "unverified"})
        rows.append({"truong": "Trích yếu", "gia_tri": d["title_summary"], "trich": "", "nguon": d["source"], "luc": d["collected"], "nhan": "verified" if verified else "unverified"})
        if d["signed_date"]:
            rows.append({"truong": "Ngày ký", "gia_tri": d["signed_date"].strftime("%d/%m/%Y"), "trich": ex.get("signed_date", ""), "nguon": d["source"], "luc": d["collected"], "nhan": "verified" if verified else "unverified"})
        if d["effective_date"]:
            rows.append({"truong": "Ngày hiệu lực", "gia_tri": d["effective_date"].strftime("%d/%m/%Y"), "trich": ex.get("effective_date", ""), "nguon": d["source"], "luc": d["collected"], "nhan": "verified" if verified else "unverified"})
        elif d["comment_deadline"]:
            rows.append({"truong": "Hạn góp ý", "gia_tri": d["comment_deadline"].strftime("%d/%m/%Y"), "trich": ex.get("comment_deadline", ""), "nguon": d["source"], "luc": d["collected"], "nhan": "verified"})
        elif not verified:
            rows.append({"truong": "Ngày hiệu lực", "gia_tri": "01/11/2026 hoặc 15/11/2026", "trich": "", "nguon": "Công báo TP.HCM · vbpl.vn", "luc": d["collected"], "nhan": "unverified"})
        for phan, ngay in d["partial_effects"]:
            rows.append({"truong": "Hiệu lực riêng", "gia_tri": f"{phan}: {ngay.strftime('%d/%m/%Y')}", "trich": "", "nguon": d["source"], "luc": d["collected"], "nhan": "verified"})
        for r in d["relations"]:
            rows.append({"truong": r["relation"], "gia_tri": f'{r["other"]}' + (f' ({r["scope"]})' if r["scope"] else ""), "trich": r["excerpt"], "nguon": d["source"], "luc": d["collected"], "nhan": "verified"})
    for item in CAN_CU_RIENG.get(card["ma"], []):
        rows.append(item)
    return rows


# Điều khoản cụ thể làm căn cứ cho thẻ Hỏi đáp, Khoảng trống, Tin tức (văn bản thật).
CAN_CU_RIENG = {
    "T-20261021-04": [
        {"truong": "Quy định áp dụng", "gia_tri": "Điều 254 Bộ luật Dân sự 2015 – Quyền về lối đi qua", "trich": "Chủ sở hữu có bất động sản bị vây bọc bởi các bất động sản của các chủ sở hữu khác mà không có hoặc không đủ lối đi ra đường công cộng, có quyền yêu cầu chủ sở hữu bất động sản vây bọc dành cho mình một lối đi hợp lý trên phần đất của họ.", "nguon": "vbpl.vn", "luc": "07:00 20/10/2026", "nhan": "verified"},
    ],
    "T-20261021-05": [
        {"truong": "Quy định áp dụng", "gia_tri": "Điều 328 Bộ luật Dân sự 2015 – Đặt cọc; còn hiệu lực ngày 21/10/2026", "trich": "nếu bên nhận đặt cọc từ chối việc giao kết, thực hiện hợp đồng thì phải trả cho bên đặt cọc tài sản đặt cọc và một khoản tiền tương đương giá trị tài sản đặt cọc, trừ trường hợp có thỏa thuận khác", "nguon": "vbpl.vn", "luc": "07:00 20/10/2026", "nhan": "verified"},
    ],
    "T-20261021-06": [
        {"truong": "Quy định áp dụng", "gia_tri": "Điều 174 Bộ luật Hình sự 2015 – Tội lừa đảo chiếm đoạt tài sản", "trich": "Người nào bằng thủ đoạn gian dối chiếm đoạt tài sản của người khác…", "nguon": "vbpl.vn", "luc": "07:00 20/10/2026", "nhan": "verified"},
    ],
}

# ---------------------------------------------------------------- Tin Khẩn (alerts)

ALERTS = [
    {
        "ma": "K-20261020-01",
        "case_code": "K2",
        "ten_loai": "Văn bản văn phòng đã viện dẫn vừa thay đổi",
        "document_id": 106,
        "su_viec": "Bị đính chính khoản 2 Điều 9, đăng trên Công báo ngày 20/10/2026.",
        "bai": [{"tieu_de": "Hồ sơ cấp sổ đỏ lần đầu gồm những gì?", "pham_vi": "khoản 2 Điều 9", "web_url": "luatsunam.com/ho-so-cap-so-do-lan-dau"}],
        "can_cu_trich": "Đính chính khoản 2 Điều 9: thay cụm từ \"bản sao có chứng thực\" bằng \"bản sao\"… (minh họa)",
        "phat_hien": "09:40 20/10",
        "status": "sent",
        "nhac_lai": "13:40 20/10",
    },
]
for _a in ALERTS:
    _a["van_ban"] = van_ban(_a["document_id"])

# ---------------------------------------------------------------- Cần xem (review_items)

REVIEW_ITEMS = [
    {"ma": "R-1", "reason_code": "TIER1_MISMATCH", "loai": "Hai nguồn Tầng 1 ghi khác nhau", "doi_tuong": "xx/2026/QĐ-UBND (minh họa) – bảng giá đất TP.HCM", "document_id": 104, "ly_do": "Ngày hiệu lực: Công báo TP.HCM ghi 01/11/2026, vbpl.vn ghi 15/11/2026.", "severity": "normal", "cho": "5 giờ", "qua_han": False,
     "doi_chieu": [("Công báo TP.HCM", "01/11/2026", "Quyết định này có hiệu lực kể từ ngày 01 tháng 11 năm 2026."), ("vbpl.vn", "15/11/2026", "Quyết định này có hiệu lực kể từ ngày 15 tháng 11 năm 2026.")]},
    {"ma": "R-2", "reason_code": "FIELD_UNSURE", "loai": "Máy đọc chưa chắc", "doi_tuong": "4xx/2026/TT-BCA (minh họa) – giấy phép lái xe", "document_id": 105, "ly_do": "Bản PDF scan; không tìm thấy câu hiệu lực khớp trong phần chữ (OCR 82 điểm).", "severity": "normal", "cho": "26 giờ", "qua_han": False, "doi_chieu": []},
    {"ma": "R-3", "reason_code": "CITATION_NOT_FOUND", "loai": "Số hiệu viện dẫn không tìm thấy", "doi_tuong": "Bài \"Thừa kế không có di chúc chia thế nào?\"", "document_id": None, "ly_do": "Bài viện dẫn \"Nghị quyết 0x/20yy (minh họa)\", chưa tìm thấy trên vbpl.vn; tin Khẩn K2 cho viện dẫn này chưa chạy được.", "severity": "normal", "cho": "50 giờ", "qua_han": True, "doi_chieu": []},
    {"ma": "R-4", "reason_code": "SOURCE_DOWN", "loai": "Nguồn lỗi", "doi_tuong": "Công báo TP.HCM", "document_id": None, "ly_do": "Lỗi 2 lượt liên tiếp từ 08:10: trang trả về trang bảo trì. Hệ thống thử lại mỗi 60 phút; quá 24 giờ thì chuyển dán link tay.", "severity": "normal", "cho": "3 giờ", "qua_han": False, "doi_chieu": []},
]

# ---------------------------------------------------------------- Mốc lịch (calendar_entries)

CALENDAR = [
    {"ngay": date(2026, 10, 23), "gio": "08:00", "tieu_de": "Kỳ họp thứ 2: thảo luận ở tổ về các dự án luật (minh họa)", "loai": "Phiên họp", "origin": "manual", "document_id": None},
    {"ngay": date(2026, 10, 29), "gio": "", "tieu_de": "Nhắc T-7: hạn góp ý dự thảo Nghị định về hộ kinh doanh", "loai": "Nhắc T-7", "origin": "system", "document_id": 103},
    {"ngay": date(2026, 11, 1), "gio": "", "tieu_de": "Nhắc T-30: hiệu lực 2xx/2026/TT-BNV (minh họa)", "loai": "Nhắc T-30", "origin": "system", "document_id": 102},
    {"ngay": date(2026, 11, 1), "gio": "", "tieu_de": "Hiệu lực xx/2026/QĐ-UBND (minh họa) theo Công báo TP.HCM — chưa chốt", "loai": "Hiệu lực", "origin": "system", "document_id": 104},
    {"ngay": date(2026, 11, 5), "gio": "", "tieu_de": "Hạn góp ý dự thảo Nghị định về đăng ký hộ kinh doanh", "loai": "Hạn góp ý", "origin": "system", "document_id": 103},
    {"ngay": date(2026, 11, 8), "gio": "", "tieu_de": "Nhắc T-7: hiệu lực 1xx/2026/NĐ-CP (minh họa)", "loai": "Nhắc T-7", "origin": "system", "document_id": 101},
    {"ngay": date(2026, 11, 14), "gio": "", "tieu_de": "Kỳ họp thứ 2: kết thúc đợt 1", "loai": "Phiên họp", "origin": "manual", "document_id": None},
    {"ngay": date(2026, 11, 15), "gio": "", "tieu_de": "Hiệu lực 1xx/2026/NĐ-CP (minh họa) – đăng ký đất đai, cấp Giấy chứng nhận lần đầu", "loai": "Hiệu lực", "origin": "system", "document_id": 101},
    {"ngay": date(2026, 11, 20), "gio": "08:00", "tieu_de": "Kỳ họp thứ 2: bắt đầu đợt 2", "loai": "Phiên họp", "origin": "manual", "document_id": None},
    {"ngay": date(2026, 11, 21), "gio": "", "tieu_de": "Kỳ họp thứ 2: dự kiến bế mạc (dự phòng 23/11)", "loai": "Phiên họp", "origin": "manual", "document_id": None},
    {"ngay": date(2026, 12, 1), "gio": "", "tieu_de": "Hiệu lực 2xx/2026/TT-BNV (minh họa) – hợp đồng lao động điện tử", "loai": "Hiệu lực", "origin": "system", "document_id": 102},
    {"ngay": date(2026, 12, 1), "gio": "", "tieu_de": "Hiệu lực 4xx/2026/TT-BCA (minh họa) – giấy phép lái xe (chưa chốt)", "loai": "Hiệu lực", "origin": "system", "document_id": 105},
]
for _e in CALENDAR:
    _e["con_ngay"] = con_ngay(_e["ngay"])


def lich_theo_tuan():
    tuan = []
    for e in sorted(CALENDAR, key=lambda x: x["ngay"]):
        iso = e["ngay"].isocalendar()
        key = (iso[0], iso[1])
        if not tuan or tuan[-1]["key"] != key:
            tuan.append({"key": key, "ten": f"Tuần {iso[1]}", "muc": []})
        tuan[-1]["muc"].append(e)
    return tuan


# ---------------------------------------------------------------- Đối thủ (competitor_articles)

COMPETITOR_ARTICLES = [
    {"id": 1, "don_vi": "Đối thủ A", "tieu_de": "Bùng cọc mua đất xử lý thế nào?", "dang": "qa", "chu_de": "A-DD-02", "ngay": "20/10/2026", "moi": True, "luot_xem": 12400, "tang": 28, "loi_thoi": False, "can_cu": "Điều 328 Bộ luật Dân sự 2015 – còn hiệu lực"},
    {"id": 2, "don_vi": "Đối thủ A", "tieu_de": "Thủ tục cấp sổ đỏ lần đầu mới nhất", "dang": "procedure", "chu_de": "A-DD-01", "ngay": "20/10/2026", "moi": True, "luot_xem": 8100, "tang": 12, "loi_thoi": False, "can_cu": "31/2024/QH15 – còn hiệu lực"},
    {"id": 3, "don_vi": "Đối thủ B", "tieu_de": "Rút BHXH một lần năm 2026 được không?", "dang": "qa", "chu_de": "B-BH", "ngay": "20/10/2026", "moi": True, "luot_xem": 21000, "tang": 35, "loi_thoi": False, "can_cu": ""},
    {"id": 4, "don_vi": "Đối thủ B", "tieu_de": "Ly hôn đơn phương cần giấy tờ gì?", "dang": "qa", "chu_de": "A-HN-01", "ngay": "20/10/2026", "moi": True, "luot_xem": 5300, "tang": 4, "loi_thoi": False, "can_cu": ""},
    {"id": 5, "don_vi": "Đối thủ B", "tieu_de": "Hướng dẫn cấp sổ đỏ lần đầu năm 2025", "dang": "procedure", "chu_de": "A-DD-01", "ngay": "02/2025", "moi": False, "luot_xem": 30200, "tang": 6, "loi_thoi": True, "can_cu": "1yy/2024/NĐ-CP (minh họa) – bị thay thế một phần"},
    {"id": 6, "don_vi": "Đối thủ C", "tieu_de": "Đặt cọc 30% giá trị có hợp pháp không?", "dang": "qa", "chu_de": "A-DD-02", "ngay": "11/2023", "moi": False, "luot_xem": None, "tang": None, "loi_thoi": True, "can_cu": "Bộ luật Dân sự 33/2005/QH11 – hết hiệu lực từ 01/01/2017"},
    {"id": 7, "don_vi": "Đối thủ C", "tieu_de": "Mẫu đơn khởi kiện đòi tiền đặt cọc", "dang": "form", "chu_de": "A-DD-02", "ngay": "20/10/2026", "moi": True, "luot_xem": None, "tang": None, "loi_thoi": False, "can_cu": ""},
    {"id": 8, "don_vi": "Đối thủ D", "tieu_de": "Bị lừa đảo qua mạng thì báo ai?", "dang": "qa", "chu_de": "A-HS-01", "ngay": "20/10/2026", "moi": True, "luot_xem": 9600, "tang": 22, "loi_thoi": False, "can_cu": "Điều 174 Bộ luật Hình sự 2015"},
    {"id": 9, "don_vi": "Đối thủ D", "tieu_de": "Hợp đồng lao động điện tử có giá trị pháp lý không?", "dang": "qa", "chu_de": "A-LD-01", "ngay": "19/10/2026", "moi": False, "luot_xem": 2100, "tang": 3, "loi_thoi": False, "can_cu": ""},
    {"id": 10, "don_vi": "Đối thủ E", "tieu_de": "Thành lập hộ kinh doanh cần những gì?", "dang": "procedure", "chu_de": "A-KD-01", "ngay": "18/10/2026", "moi": False, "luot_xem": None, "tang": None, "loi_thoi": False, "can_cu": ""},
    {"id": 11, "don_vi": "Đối thủ F", "tieu_de": "Tranh chấp lối đi chung giải quyết ở đâu?", "dang": "qa", "chu_de": "A-DD-04", "ngay": "15/10/2026", "moi": False, "luot_xem": 4800, "tang": 2, "loi_thoi": False, "can_cu": "Điều 254 Bộ luật Dân sự 2015"},
    {"id": 12, "don_vi": "Đối thủ G", "tieu_de": "Phạt nguội xe máy tra cứu ở đâu?", "dang": "qa", "chu_de": "B-GT", "ngay": "20/10/2026", "moi": True, "luot_xem": 15800, "tang": 41, "loi_thoi": False, "can_cu": ""},
    {"id": 13, "don_vi": "Đơn vị dữ liệu 1", "tieu_de": "Văn bản mới về đăng ký đất đai (minh họa)", "dang": "new_doc", "chu_de": "A-DD-01", "ngay": "20/10/2026", "moi": True, "luot_xem": None, "tang": None, "loi_thoi": False, "can_cu": "1xx/2026/NĐ-CP (minh họa)"},
    {"id": 14, "don_vi": "Đơn vị dữ liệu 2", "tieu_de": "Điểm mới về hợp đồng lao động điện tử (minh họa)", "dang": "new_doc", "chu_de": "A-LD-01", "ngay": "20/10/2026", "moi": True, "luot_xem": None, "tang": None, "loi_thoi": False, "can_cu": "2xx/2026/TT-BNV (minh họa)"},
    {"id": 15, "don_vi": "Đối thủ A", "tieu_de": "Chia tài sản chung khi ly hôn: những điều cần biết", "dang": "commentary", "chu_de": "A-HN-03", "ngay": "17/10/2026", "moi": False, "luot_xem": 3900, "tang": 1, "loi_thoi": False, "can_cu": ""},
    {"id": 16, "don_vi": "Đối thủ G", "tieu_de": "Đổi giấy phép lái xe online mất bao lâu?", "dang": "procedure", "chu_de": "B-GT", "ngay": "20/10/2026", "moi": True, "luot_xem": 7200, "tang": 18, "loi_thoi": False, "can_cu": ""},
]
for _a in COMPETITOR_ARTICLES:
    _a["ten_dang"] = DANG_BAI[_a["dang"]]

DON_VI_DOI_THU = ["Đối thủ A", "Đối thủ B", "Đối thủ C", "Đối thủ D", "Đối thủ E", "Đối thủ F", "Đối thủ G", "Đơn vị dữ liệu 1", "Đơn vị dữ liệu 2"]

# Bảng đơn vị × dạng bài, 7 ngày (số liệu tổng hợp minh họa).
TONG_HOP_7_NGAY = {
    "Đối thủ A": {"qa": 9, "new_doc": 1, "form": 0, "procedure": 4, "commentary": 2},
    "Đối thủ B": {"qa": 7, "new_doc": 0, "form": 1, "procedure": 3, "commentary": 0},
    "Đối thủ C": {"qa": 3, "new_doc": 0, "form": 5, "procedure": 1, "commentary": 0},
    "Đối thủ D": {"qa": 6, "new_doc": 2, "form": 0, "procedure": 1, "commentary": 1},
    "Đối thủ E": {"qa": 1, "new_doc": 0, "form": 0, "procedure": 2, "commentary": 0},
    "Đối thủ F": {"qa": 4, "new_doc": 0, "form": 0, "procedure": 0, "commentary": 0},
    "Đối thủ G": {"qa": 8, "new_doc": 0, "form": 0, "procedure": 5, "commentary": 0},
    "Đơn vị dữ liệu 1": {"qa": 12, "new_doc": 14, "form": 6, "procedure": 2, "commentary": 3},
    "Đơn vị dữ liệu 2": {"qa": 5, "new_doc": 11, "form": 0, "procedure": 0, "commentary": 4},
}
COT_DANG_BAI = ["qa", "new_doc", "form", "procedure", "commentary"]

CHU_DE_DOI_THU_7_NGAY = [
    {"chu_de": "A-DD-02", "ten": "Chuyển nhượng, đặt cọc mua bán", "so_bai": 9, "so_don_vi": 4, "van_phong_co_bai": True},
    {"chu_de": "A-DD-01", "ten": "Cấp sổ lần đầu, cấp đổi", "so_bai": 8, "so_don_vi": 4, "van_phong_co_bai": True},
    {"chu_de": "B-GT", "ten": "Giao thông (phạt nguội, điểm bằng lái)", "so_bai": 7, "so_don_vi": 2, "van_phong_co_bai": False},
    {"chu_de": "A-HN-01", "ten": "Ly hôn thuận tình, đơn phương", "so_bai": 6, "so_don_vi": 3, "van_phong_co_bai": True},
    {"chu_de": "A-HS-01", "ten": "Lừa đảo chiếm đoạt, lừa đảo qua mạng", "so_bai": 5, "so_don_vi": 3, "van_phong_co_bai": False},
]

KHOANG_TRONG = [
    {"chu_de": "A-DD-04", "ten": "Tranh chấp ranh giới, lối đi", "so_nguon": 5, "the": "T-20261021-04"},
    {"chu_de": "A-HS-01", "ten": "Lừa đảo chiếm đoạt, lừa đảo qua mạng", "so_nguon": 5, "the": "T-20261021-06"},
    {"chu_de": "B-GT", "ten": "Giao thông (phạt nguội, điểm bằng lái)", "so_nguon": 7, "the": None},
    {"chu_de": "B-BH", "ten": "Bảo hiểm xã hội (rút BHXH một lần)", "so_nguon": 6, "the": None},
]

# ---------------------------------------------------------------- Kho câu hỏi (questions)

QUESTIONS = [
    {"cau_hoi": "Rút BHXH một lần năm 2026 được không?", "chu_de": "B-BH", "so_nguon": 7, "can_cu": "unchecked", "da_co_bai": False},
    {"cau_hoi": "Bị bùng cọc khi mua đất có lấy lại được tiền không?", "chu_de": "A-DD-02", "so_nguon": 6, "can_cu": "valid", "da_co_bai": False},
    {"cau_hoi": "Làm sổ đỏ lần đầu cần giấy tờ gì?", "chu_de": "A-DD-01", "so_nguon": 5, "can_cu": "outdated", "da_co_bai": True},
    {"cau_hoi": "Đất chưa có sổ có bán được không?", "chu_de": "A-DD-01", "so_nguon": 5, "can_cu": "valid", "da_co_bai": False},
    {"cau_hoi": "Ly hôn đơn phương mất bao lâu?", "chu_de": "A-HN-01", "so_nguon": 4, "can_cu": "unchecked", "da_co_bai": True},
    {"cau_hoi": "Bị lừa đảo qua mạng báo ai?", "chu_de": "A-HS-01", "so_nguon": 4, "can_cu": "valid", "da_co_bai": False},
    {"cau_hoi": "Bán hàng online có phải đăng ký hộ kinh doanh không?", "chu_de": "A-KD-01", "so_nguon": 4, "can_cu": "unchecked", "da_co_bai": False},
    {"cau_hoi": "Hợp đồng lao động điện tử có cần ký tay không?", "chu_de": "A-LD-01", "so_nguon": 3, "can_cu": "valid", "da_co_bai": False},
    {"cau_hoi": "Tranh chấp lối đi chung kiện ở đâu?", "chu_de": "A-DD-04", "so_nguon": 3, "can_cu": "valid", "da_co_bai": False},
]
TINH_TRANG_CAN_CU = {"valid": "Còn hiệu lực", "outdated": "Căn cứ lỗi thời", "unchecked": "Chưa đối chiếu"}

# ---------------------------------------------------------------- Kho bài (firm_articles)

FIRM_ARTICLES = [
    {"tieu_de": "Hồ sơ cấp sổ đỏ lần đầu gồm những gì?", "status": "published", "ngay": "10/10/2026", "chu_de": "A-DD-01", "web": "luatsunam.com/ho-so-cap-so-do-lan-dau", "facebook": True, "vien_dan": ["3xx/2025/NĐ-CP (minh họa), khoản 2 Điều 9", "31/2024/QH15"], "canh_bao": "Văn bản viện dẫn vừa bị đính chính (tin Khẩn K-20261020-01)", "nguon_goc": "Chế độ thủ công"},
    {"tieu_de": "Ly hôn đơn phương: thủ tục và thời gian giải quyết", "status": "published", "ngay": "05/10/2026", "chu_de": "A-HN-01", "web": "luatsunam.com/ly-hon-don-phuong", "facebook": True, "vien_dan": [], "canh_bao": "Chưa nhập viện dẫn: hệ thống không báo được khi văn bản thay đổi", "nguon_goc": "Chế độ thủ công"},
    {"tieu_de": "Đặt cọc mua đất: 5 điều cần biết trước khi xuống tiền", "status": "published", "ngay": "28/09/2026", "chu_de": "A-DD-02", "web": "luatsunam.com/dat-coc-mua-dat", "facebook": True, "vien_dan": ["91/2015/QH13, Điều 328"], "canh_bao": "", "nguon_goc": "Chế độ thủ công"},
    {"tieu_de": "Thừa kế không có di chúc chia thế nào?", "status": "published", "ngay": "15/09/2026", "chu_de": "A-TK-01", "web": "luatsunam.com/thua-ke-khong-di-chuc", "facebook": False, "vien_dan": ["91/2015/QH13, Điều 650–651", "Nghị quyết 0x/20yy (minh họa)"], "canh_bao": "1 viện dẫn chưa tìm thấy trên Tầng 1", "nguon_goc": "Chế độ thủ công"},
    {"tieu_de": "Kỳ họp thứ 2: các dự án luật về đất đai cần theo dõi (minh họa)", "status": "written", "ngay": "", "chu_de": "A-DD-01", "web": "", "facebook": False, "vien_dan": [], "canh_bao": "", "nguon_goc": "Chế độ thủ công"},
]

# ---------------------------------------------------------------- Chủ đề (topics) – danh mục bản 1, mục 18

DANH_MUC_A = [
    ("Đất đai", "DD", [
        ("Cấp sổ lần đầu, cấp đổi", "sổ đỏ, sổ hồng"),
        ("Chuyển nhượng, đặt cọc mua bán", "mất cọc, bùng cọc"),
        ("Chuyển mục đích sử dụng", "lên thổ cư"),
        ("Tranh chấp ranh giới, lối đi", ""),
        ("Thu hồi, bồi thường, tái định cư", "giải tỏa, đền bù"),
        ("Thuế phí khi sang tên", ""),
        ("Nhà dự án, chung cư chậm sổ", ""),
        ("Cập nhật giấy tờ sau sắp xếp đơn vị hành chính", ""),
    ]),
    ("Thừa kế", "TK", [
        ("Chia thừa kế không có di chúc", ""),
        ("Lập, sửa, hủy di chúc", "di chúc có hợp lệ không"),
        ("Khai nhận, phân chia di sản tại công chứng", ""),
        ("Tranh chấp thừa kế nhà đất", ""),
        ("Thời hiệu thừa kế", ""),
        ("Thừa kế có yếu tố nước ngoài, Việt kiều", ""),
    ]),
    ("Hôn nhân gia đình", "HN", [
        ("Ly hôn thuận tình, đơn phương", ""),
        ("Quyền nuôi con, cấp dưỡng", ""),
        ("Chia tài sản chung, tài sản riêng", ""),
        ("Ly hôn có yếu tố nước ngoài", ""),
    ]),
    ("Dân sự", "DS", [
        ("Vay mượn, đòi nợ cá nhân", "vỡ hụi"),
        ("Hợp đồng, ủy quyền", ""),
        ("Bồi thường thiệt hại", ""),
        ("Khởi kiện, án phí, thủ tục tòa", ""),
    ]),
    ("Lao động", "LD", [
        ("Sa thải, chấm dứt hợp đồng trái luật", ""),
        ("Nợ lương, trợ cấp thôi việc", ""),
        ("Tai nạn lao động", ""),
    ]),
    ("Hình sự", "HS", [
        ("Lừa đảo chiếm đoạt, lừa đảo qua mạng", ""),
        ("Bị bắt, tạm giam, bảo lĩnh", ""),
        ("Quyền của bị hại", ""),
        ("Án treo, xóa án tích", ""),
    ]),
    ("Hành chính", "HC", [
        ("Khiếu nại, khởi kiện quyết định hành chính", ""),
        ("Xử phạt vi phạm hành chính", ""),
        ("Thủ tục sau chính quyền hai cấp", ""),
    ]),
    ("Kinh doanh thương mại", "KD", [
        ("Thành lập, thay đổi doanh nghiệp, hộ kinh doanh", ""),
        ("Tranh chấp hợp đồng, đòi nợ doanh nghiệp", ""),
        ("Góp vốn, chuyển nhượng vốn", ""),
        ("Giải thể", ""),
    ]),
]

# Số liệu hiển thị cạnh chủ đề (minh họa): (số câu hỏi, số bài đối thủ 30 ngày, số bài văn phòng)
SO_LIEU_CHU_DE = {
    "A-DD-01": (14, 21, 1), "A-DD-02": (11, 18, 1), "A-DD-04": (5, 6, 0), "A-HN-01": (9, 12, 1),
    "A-HS-01": (7, 9, 0), "A-KD-01": (6, 5, 0), "A-LD-01": (4, 4, 0), "A-TK-01": (8, 7, 1), "A-HN-03": (3, 4, 0),
}


def danh_muc_a():
    out = []
    for linh_vuc, ma_lv, chu_de in DANH_MUC_A:
        items = []
        for i, (ten, dan_gian) in enumerate(chu_de, start=1):
            ma = f"A-{ma_lv}-{i:02d}"
            so = SO_LIEU_CHU_DE.get(ma, (0, 0, 0))
            items.append({"ma": ma, "ten": ten, "dan_gian": dan_gian, "so_cau_hoi": so[0], "so_bai_doi_thu": so[1], "so_bai_vp": so[2], "khoang_trong": so[1] >= 4 and so[2] == 0})
        out.append({"linh_vuc": linh_vuc, "ma": ma_lv, "chu_de": items})
    return out


DANH_MUC_B = [
    ("B-TH", "Thuế", "thuế thu nhập cá nhân, hộ kinh doanh"),
    ("B-GT", "Giao thông", "phạt nguội, điểm bằng lái"),
    ("B-BH", "Bảo hiểm xã hội, y tế", "rút BHXH một lần"),
    ("B-CT", "Cư trú, hộ tịch, định danh", ""),
    ("B-NH", "Ngân hàng, tín dụng", "nợ xấu"),
    ("B-TD", "Tiêu dùng, thương mại điện tử", ""),
    ("B-CN", "Công nghệ, dữ liệu, an ninh mạng", ""),
    ("B-XD", "Xây dựng, cấp phép xây dựng", ""),
    ("B-GD", "Giáo dục", ""),
    ("B-YT", "Y tế", ""),
    ("B-QS", "Nghĩa vụ quân sự", ""),
    ("B-XNC", "Xuất nhập cảnh", ""),
]

CHU_DE_TIN_TUC = [
    {"ma": "N-2026-0041", "ten": "Giả danh cán bộ thuế gọi điện lừa đảo", "nhac_lan_cuoi": "21/10/2026", "het_han": "04/11/2026", "con_han": True},
    {"ma": "N-2026-0038", "ten": "Sạt lở bờ sông, di dời khẩn cấp", "nhac_lan_cuoi": "12/10/2026", "het_han": "26/10/2026", "con_han": True},
    {"ma": "N-2026-0029", "ten": "Vụ sập giàn giáo công trình", "nhac_lan_cuoi": "20/09/2026", "het_han": "04/10/2026", "con_han": False},
]


def ten_chu_de(ma):
    for linh_vuc, ma_lv, chu_de in DANH_MUC_A:
        for i, (ten, _) in enumerate(chu_de, start=1):
            if f"A-{ma_lv}-{i:02d}" == ma:
                return ten
    for code, ten, _ in DANH_MUC_B:
        if code == ma:
            return ten
    return ma


# ---------------------------------------------------------------- Số liệu từ khóa (keyword_metrics)

KEYWORDS = [
    {"tu_khoa": "thủ tục cấp sổ đỏ lần đầu", "chu_de": "A-DD-01", "hien_thi": 4820, "nhap": 96, "vi_tri": 14.2, "tim_thang": 9900, "xu_huong": "+35%"},
    {"tu_khoa": "bùng cọc mua đất", "chu_de": "A-DD-02", "hien_thi": 2310, "nhap": 41, "vi_tri": 18.6, "tim_thang": 2400, "xu_huong": "+12%"},
    {"tu_khoa": "ly hôn đơn phương", "chu_de": "A-HN-01", "hien_thi": 6100, "nhap": 152, "vi_tri": 9.8, "tim_thang": 14800, "xu_huong": "0%"},
    {"tu_khoa": "tranh chấp lối đi chung", "chu_de": "A-DD-04", "hien_thi": 0, "nhap": 0, "vi_tri": None, "tim_thang": 1300, "xu_huong": "+5%"},
    {"tu_khoa": "hợp đồng lao động điện tử", "chu_de": "A-LD-01", "hien_thi": 120, "nhap": 2, "vi_tri": 41.0, "tim_thang": 880, "xu_huong": "+60%"},
    {"tu_khoa": "luật sư đất đai TP.HCM", "chu_de": "", "hien_thi": 980, "nhap": 23, "vi_tri": 11.3, "tim_thang": 1600, "xu_huong": "+8%"},
]
LAN_NHAP_TU_KHOA = [("Search Console", "01/10/2026", 20), ("Keyword Planner", "15/09/2026", 36), ("Google Trends", "18/10/2026", 3)]

# ---------------------------------------------------------------- Tín hiệu nhập tay (manual_signals)

SIGNALS = [
    {"url": "https://www.tiktok.com/@kenh-phap-luat/video/(minh họa)", "nen_tang": "TikTok", "tieu_de": "Video \"3 cách nhận biết cuộc gọi giả danh cán bộ thuế\" (minh họa)", "ghi_chu": "Nhiều bình luận hỏi cách báo công an", "chu_de": "A-HS-01", "luc": "35 phút trước", "ket_qua": "ok"},
    {"url": "https://www.facebook.com/(trang hỏi đáp pháp luật – minh họa)", "nen_tang": "Facebook", "tieu_de": "Bài hỏi đáp về bùng cọc mua đất (minh họa)", "ghi_chu": "1,2 nghìn bình luận", "chu_de": "A-DD-02", "luc": "Hôm qua 20:14", "ket_qua": "ok"},
    {"url": "https://bit.ly/(link rút gọn)", "nen_tang": "Khác", "tieu_de": "", "ghi_chu": "", "chu_de": "", "luc": "Hôm qua 17:02", "ket_qua": "rejected", "ly_do": "Link rút gọn không được chấp nhận; dán link gốc của bài"},
]

# ---------------------------------------------------------------- Vận hành

AI_7_NGAY = [("15/10", 1.12), ("16/10", 0.84), ("17/10", 2.05), ("18/10", 0.96), ("19/10", 1.40), ("20/10", 0.77), ("21/10", 0.58)]
HAN_MUC_AI = 3.00


DIGEST = {
    "ngay": HOM_NAY,
    "lap_luc": "06:21",
    "dung_gio": True,
    "telegram": "✅ Telegram 06:30",
    "gmail": "✅ Gmail 06:30",
    "van_ban_moi_a": [101, 102],
    "van_ban_moi_b": {"so_luong": 7, "noi_bat": ["4xx/2026/TT-BCA (minh họa) – cấp, đổi giấy phép lái xe", "Thông tư (minh họa) về hóa đơn điện tử hộ kinh doanh", "Nghị định (minh họa) về xử phạt trong lĩnh vực y tế"]},
    "tin_nhieu_bao": [("Giả danh cán bộ thuế gọi điện lừa đảo", 3), ("Điều chỉnh bảng giá đất TP.HCM", 5), ("Kỳ họp thứ 2: chương trình làm việc", 4)],
}


def tom_tat_telegram():
    """Tóm tắt 6h30 theo mẫu Phụ lục B.2 (có tin Khẩn chưa xem nên dòng 1 là tin Khẩn)."""
    pro = the_theo_luong("pro")
    pub = the_theo_luong("public")
    a = ALERTS[0]
    dong = [
        f"☀️ Bản tin {THU_HOM_NAY}, {HOM_NAY.strftime('%d/%m')}",
        f"🔴 Khẩn: {len(ALERTS)} · Nên viết: {len(pro)} chuyên môn, {len(pub)} đại chúng",
        f"1. KHẨN {a['case_code']}: {a['van_ban']['so_hieu']} – {a['su_viec']}",
        f"2. {pro[0]['tieu_de']}",
        f"🆕 9 văn bản mới · 👀 23 bài đối thủ, nhiều nhất về đặt cọc mua đất · ⏳ {len(REVIEW_ITEMS)} cần xem · 1 nguồn lỗi",
        f"👉 {{khu quản trị}}/ban-tin/{HOM_NAY.isoformat()}",
    ]
    return "\n".join(dong)
