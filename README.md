# Hệ thống thông tin pháp lý nóng

Hệ thống thông tin nội bộ giúp đội nội dung trả lời ba câu hỏi mỗi sáng:

1. **Có gì mới?** Văn bản pháp luật mới, sắp có hiệu lực, dự thảo đang lấy ý kiến, tin được nhiều báo cùng viết.
2. **Đối thủ viết gì?** Bài mới, chủ đề viết nhiều, bài tăng lượt xem, bài có thể lỗi thời, khoảng trống.
3. **Hôm nay nên viết gì?** 5–7 thẻ gợi ý chia hai luồng Chuyên môn và Đại chúng, mỗi thẻ có căn cứ gốc và đoạn trích.

Đặc tả: **Đặc tả 3.2** (tài liệu Claude Docs "Hệ thống thông tin pháp lý nóng"), gồm tab chính, Phụ lục A (lược đồ dữ liệu, 27 bảng), Phụ lục B (mẫu đầu ra), Phụ lục C (5 màn hình) và tab Rà soát 3.1 → 3.2.

## Trạng thái hiện tại: bản mẫu giao diện

Kho này mới có **bản mẫu giao diện** của khu quản trị (Phụ lục C), dựng bằng Django để dùng lại được template khi làm thật.

- Dữ liệu là **minh họa** (`quantri/demo.py`), không phải văn bản hay bài viết thật. Số hiệu văn bản dạng `1xx/2026/NĐ-CP (minh họa)` là giả định.
- Ngày giả định: Thứ Tư 21/10/2026.
- Nút thao tác chưa ghi dữ liệu; bấm vào sẽ hiện thông báo nói rõ khi chạy thật thao tác ghi vào bảng nào (theo Phụ lục C.10).
- Chưa có cơ sở dữ liệu, thu thập, AI, Telegram, Gmail, đăng nhập thật.
- Chưa dùng HTMX: tương tác hiện ở `quantri/static/quantri/app.js`. HTMX vào cùng các nút ghi dữ liệu ở Lát 1.

| Màn hình | Địa chỉ | Trả lời câu hỏi |
|---|---|---|
| Hôm nay | `/` | Cả ba câu hỏi, tin Khẩn, tình trạng nguồn |
| Bản tin | `/ban-tin/2026-10-21/` | Nội dung email 06:30 và tóm tắt Telegram |
| Tin Khẩn | `/canh-bao/<mã>/` | Văn bản đã viện dẫn vừa thay đổi |
| Gợi ý | `/goi-y/`, `/goi-y/<mã thẻ>/` | Hôm nay nên viết gì |
| Đối thủ | `/doi-thu/` + `tong-hop/`, `cau-hoi/`, `khoang-trong/` | Đối thủ viết gì |
| Văn bản | `/van-ban/` + `lich/`, `can-xem/`, `/van-ban/<id>/` | Có gì mới |
| Chủ đề | `/chu-de/` + `kho-bai/`, `tu-khoa/` | Danh mục, kho bài văn phòng, số liệu từ khóa |
| Dán link | nút "+ Dán link" | Đưa tín hiệu tay vào hệ thống |

## Chạy thử

Cần Python 3.12 trở lên.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Mở http://127.0.0.1:8000/.

Kiểm thử:

```bash
python manage.py test
```

Xuất một tệp HTML để xem thử ở nơi không chạy được Django (mọi màn hình trong một tệp, chuyển màn hình bằng `#địa-chỉ`):

```bash
python manage.py xuat_ban_mau --out dist/ban-mau.html
```

## Cấu trúc

```
hethong/                  cấu hình Django
quantri/                  khu quản trị
  demo.py                 dữ liệu minh họa, tên trường theo Phụ lục A
  views.py, urls.py       màn hình theo Phụ lục C
  templates/quantri/      template, dùng lại khi làm thật
  static/quantri/         app.css, app.js
  management/commands/    xuat_ban_mau: xuất một tệp xem thử
config/settings.yaml      ngưỡng tự đặt (mục 20) và con số lấy từ luật (mục 11)
tests/                    kiểm thử màn hình và bản xuất
```

Con số lấy từ luật trong `config/settings.yaml` chưa điền giá trị: mỗi con số phải kèm căn cứ, số văn bản hợp nhất và ngày đối chiếu, đối chiếu trong GĐ0 và chốt sau khi Kỳ họp thứ 2 bế mạc.

## Bước tiếp theo

1. **GĐ0 – kiểm tra nguồn.** Đọc thử từng nguồn Tầng 1 (Công báo, vbpl.vn, Công báo địa phương), báo chí và trang đối thủ; ghi lại cách đọc được, tần suất, chặn máy đọc. Đây là việc quyết định hệ thống có chạy được hay không.
2. **Lát 1 – văn bản và tin Khẩn.** PostgreSQL theo Phụ lục A, thu thập Tầng 1, bảng Văn bản, Cần xem, tin Khẩn K1/K2, đăng nhập mật khẩu và OTP.
3. **Lát 2 – đối thủ và gợi ý.** Phiếu bài đối thủ, kho câu hỏi, thẻ gợi ý, bản tin 06:30 qua Telegram và Gmail.
