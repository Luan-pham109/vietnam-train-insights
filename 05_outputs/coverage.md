# Coverage

Cập nhật: 2026-10-28 (Claude). Nguồn: `05_outputs/dashboard/coverage.json`, `markets.json`. Ngưỡng theo `00_brain/confidence.md` (medium = ≥10 evidence, ≥3 nguồn, ≥5 tác giả). Chỉ tính evidence của task `reviewed`, bỏ dòng review lỗi.

Task reviewed: T-001 → T-008, T-010, T-011 (10/12). T-009 (SERP/AI) và T-012 (TripAdvisor review tàu tư nhân) đang `rework` - chưa tính. Tổng repo 474 raw, 1213 evidence; dùng được 903, 531 tác giả. Tỷ lệ evidence biết nguồn gốc khách (origin): 53%.

| Mã | Câu hỏi | Ưu tiên | Evidence | Nguồn | Tác giả | Evidence intl | Mức | |
|---|---|---|---|---|---|---|---|---|
| C01 | Khách nước ngoài đi tàu VN gồm những segment nào (backpacker, couple, family, senior, group tour)? | P0 | 0 | 0 | 0 | 0 | none | ⚠ P0 < medium |
| C02 | Vì sao họ chọn tàu thay vì bay/xe (JTBD, trigger)? | P0 | 65 | 9 | 49 | 23 | medium |  |
| C03 | Họ tìm thông tin và đặt vé ở đâu, theo thứ tự nào? | P0 | 107 | 11 | 83 | 29 | medium |  |
| C04 | Barrier lớn nhất ở từng journey stage là gì? | P0 | 218 | 6 | 190 | 26 | medium |  |
| C05 | Họ lo gì về trust (vé giả, mất tiền, phí ẩn, không có ghế)? | P0 | 86 | 9 | 79 | 18 | medium |  |
| C06 | Họ chọn hạng/khoang thế nào, tiêu chí là gì (khoang 4 riêng, giường dưới, VIP)? | P0 | 175 | 10 | 124 | 79 | medium |  |
| C07 | Chặng cuối từ ga đến điểm đến (Sa Pa, Hội An, Hạ Long...) xử lý thế nào, đau ở đâu? | P0 | 53 | 7 | 51 | 6 | medium |  |
| C08 | Tuyến/combo nào họ muốn mà không có chuyến thẳng? | P1 | 69 | 6 | 46 | 10 | medium |  |
| C09 | Thanh toán, tiền tệ, giấy tờ (hộ chiếu, tên trên vé) gây vấn đề gì? | P0 | 19 | 9 | 18 | 5 | medium |  |
| C11 | Khách Ấn, Trung, Hàn khác khách phương Tây thế nào ở lý do đi tàu, hạng ghế, barrier? | P0 | 45 | 7 | 28 | 41 | medium |  |
| C12 | Mỗi thị trường cần gì riêng: ví thanh toán, ngôn ngữ, đồ ăn (chay/kiêng), đi theo nhóm/gia đình? | P0 | 15 | 5 | 14 | 7 | medium |  |
| C10 | Khách Việt đi tàu vì gì, đau gì (Tết, hoàn đổi, giá)? | P1 | 0 | 0 | 0 | 0 | none |  |
| M01 | Kênh nào được nhắc/recommend nhiều nhất (dsvn.vn, 12Go, Baolau, Trip.com, Traveloka, Klook, agent, quầy ga)? | P0 | 70 | 11 | 57 | 25 | medium |  |
| M02 | Từng kênh được khen/chê vì gì (giá, phí, UX, hỗ trợ, độ tin cậy)? | P0 | 39 | 3 | 39 | 0 | medium |  |
| M03 | Đối thủ định vị và quảng cáo gì (messaging, offer)? | P1 | 0 | 0 | 0 | 0 | none |  |
| M04 | Tàu du lịch tư nhân (Lotus, Chapa Express, Violette, SapaLy, Livitrans...) được nhìn nhận thế nào so với tàu DSVN? | P0 | 42 | 7 | 29 | 15 | medium |  |
| M05 | AI engine/SERP đang recommend ai khi hỏi cách đặt vé tàu VN? | P0 | 0 | 0 | 0 | 0 | none | ⚠ P0 < medium |
| M07 | Mỗi thị trường đặt vé tàu VN qua kênh nào (Trip.com/Ctrip, Fliggy, MakeMyTrip, MyRealTrip, Klook, KKday...)? Họ tìm thông tin trên nền tảng nào? | P0 | 12 | 4 | 12 | 12 | medium |  |
| M06 | Chính sách, giá, tàu mới, sản lượng của DSVN thay đổi gì? | P1 | 2 | 1 | 2 | 0 | low |  |
| I01 | Tip/workaround người đi thật hay chia sẻ là gì? | P0 | 229 | 11 | 128 | 31 | medium |  |
| I02 | "Ước gì biết trước" - kỳ vọng vs thực tế trên tàu/tại ga? | P0 | 146 | 6 | 132 | 18 | medium |  |
| I03 | Tuyến/đoạn nào được khen là đẹp, đáng đi (Hải Vân, ven biển...)? | P1 | 57 | 7 | 44 | 12 | medium |  |

Độ phủ tổng: 79% (17/22 câu đạt medium; P0: 15/17). Không đổi so với 2026-10-27: T-010, T-011 thêm volume cho C02/C03/C06/I02/I03 nhưng không mở thêm câu nào.

P0 còn dưới ngưỡng:
- C01 (0 ev, 0 nguồn, 0 tác giả)
- M05 (0 ev, 0 nguồn, 0 tác giả) - chờ T-009 rework.

**Đọc đúng:** medium = đủ *volume* để viết insight. Insight cho một thị trường cụ thể chỉ dùng origin tin cậy cao (cột `cao` bên dưới). Share of voice/số evidence là proxy, không phải thị phần.

## Evidence theo thị trường (origin)

| Thị trường | Mã | Evidence | Tin cậy cao | Tin cậy TB | Tác giả | Nguồn |
|---|---|---|---|---|---|---|
| Ấn Độ | in | 18 | 18 | 0 | 8 | 2 |
| Trung Quốc | cn | 4 | 4 | 0 | 1 | 1 |
| Đài Loan/Hồng Kông | tw_hk | 0 | 0 | 0 | 0 | 0 |
| Hàn Quốc | kr | 47 | 47 | 0 | 28 | 3 |
| Phương Tây | western | 18 | 18 | 0 | 6 | 3 |
| Châu Á khác | other_asia | 5 | 5 | 0 | 1 | 1 |
| Nước ngoài (chưa rõ nước) | intl | 147 | 126 | 21 | 69 | 4 |
| Expat | expat | 0 | 0 | 0 | 0 | 0 |
| Việt Nam | vn | 242 | 242 | 0 | 178 | 4 |
| Chưa rõ | unknown | 422 | 0 | 0 | 250 | 8 |

Trung Quốc gần như trống do Xiaohongshu/Mafengwo chặn đăng nhập (xem `source-map.md`). Ấn mỏng, Hàn tốt nhất trong wave M.
