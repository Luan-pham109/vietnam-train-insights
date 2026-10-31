# Coverage

Cập nhật: 2026-10-31 (Claude). Nguồn: `05_outputs/dashboard/coverage.json`, `markets.json`. Ngưỡng theo `00_brain/confidence.md` (medium = ≥10 evidence, ≥3 nguồn, ≥5 tác giả). Chỉ tính evidence của task `reviewed`, bỏ dòng review lỗi.

Task reviewed: T-001 → T-018 trừ T-016 (17/18; T-014 TikTok bị chặn, 0 raw; T-015 `ad_library` chỉ Meta). Đang mở: T-016 `serp_ai` lượt 2 (M05, nhận từ 2026-10-31). Tổng 528 raw, 1392 evidence; dùng được 1284, 645 tác giả. Tỷ lệ evidence biết nguồn gốc khách (origin): 50%.

| Mã | Câu hỏi | Ưu tiên | Evidence | Nguồn | Tác giả | Evidence intl | Mức | |
|---|---|---|---|---|---|---|---|---|
| C01 | Khách nước ngoài đi tàu VN gồm những segment nào (backpacker, couple, family, senior, group tour)? | P0 | 43 | 6 | 19 | 43 | medium |  |
| C02 | Vì sao họ chọn tàu thay vì bay/xe (JTBD, trigger)? | P0 | 79 | 9 | 55 | 31 | medium |  |
| C03 | Họ tìm thông tin và đặt vé ở đâu, theo thứ tự nào? | P0 | 262 | 16 | 110 | 44 | medium |  |
| C04 | Barrier lớn nhất ở từng journey stage là gì? | P0 | 223 | 6 | 193 | 28 | medium |  |
| C05 | Họ lo gì về trust (vé giả, mất tiền, phí ẩn, không có ghế)? | P0 | 124 | 12 | 98 | 30 | medium |  |
| C06 | Họ chọn hạng/khoang thế nào, tiêu chí là gì (khoang 4 riêng, giường dưới, VIP)? | P0 | 250 | 13 | 187 | 139 | medium |  |
| C07 | Chặng cuối từ ga đến điểm đến (Sa Pa, Hội An, Hạ Long...) xử lý thế nào, đau ở đâu? | P0 | 61 | 7 | 56 | 9 | medium |  |
| C08 | Tuyến/combo nào họ muốn mà không có chuyến thẳng? | P1 | 82 | 7 | 50 | 13 | medium |  |
| C09 | Thanh toán, tiền tệ, giấy tờ (hộ chiếu, tên trên vé) gây vấn đề gì? | P0 | 24 | 10 | 21 | 5 | medium |  |
| C11 | Khách Ấn, Trung, Hàn khác khách phương Tây thế nào ở lý do đi tàu, hạng ghế, barrier? | P0 | 45 | 7 | 28 | 41 | medium |  |
| C12 | Mỗi thị trường cần gì riêng: ví thanh toán, ngôn ngữ, đồ ăn (chay/kiêng), đi theo nhóm/gia đình? | P0 | 15 | 5 | 14 | 7 | medium |  |
| C10 | Khách Việt đi tàu vì gì, đau gì (Tết, hoàn đổi, giá)? | P1 | 17 | 1 | 3 | 0 | low |  |
| M01 | Kênh nào được nhắc/recommend nhiều nhất (dsvn.vn, 12Go, Baolau, Trip.com, Traveloka, Klook, agent, quầy ga)? | P0 | 218 | 16 | 83 | 37 | medium |  |
| M02 | Từng kênh được khen/chê vì gì (giá, phí, UX, hỗ trợ, độ tin cậy)? | P0 | 72 | 5 | 49 | 0 | medium |  |
| M03 | Đối thủ định vị và quảng cáo gì (messaging, offer)? | P1 | 25 | 2 | 14 | 0 | low |  |
| M04 | Tàu du lịch tư nhân (Lotus, Chapa Express, Violette, SapaLy, Livitrans...) được nhìn nhận thế nào so với tàu DSVN? | P0 | 151 | 10 | 127 | 102 | medium |  |
| M05 | AI engine/SERP đang recommend ai khi hỏi cách đặt vé tàu VN? | P0 | 119 | 1 | 3 | 0 | low | ⚠ P0 < medium |
| M07 | Mỗi thị trường đặt vé tàu VN qua kênh nào (Trip.com/Ctrip, Fliggy, MakeMyTrip, MyRealTrip, Klook, KKday...)? Họ tìm thông tin trên nền tảng nào? | P0 | 12 | 4 | 12 | 12 | medium |  |
| M06 | Chính sách, giá, tàu mới, sản lượng của DSVN thay đổi gì? | P1 | 54 | 2 | 5 | 0 | low |  |
| I01 | Tip/workaround người đi thật hay chia sẻ là gì? | P0 | 240 | 11 | 129 | 37 | medium |  |
| I02 | "Ước gì biết trước" - kỳ vọng vs thực tế trên tàu/tại ga? | P0 | 200 | 7 | 186 | 72 | medium |  |
| I03 | Tuyến/đoạn nào được khen là đẹp, đáng đi (Hải Vân, ven biển...)? | P1 | 68 | 9 | 53 | 20 | medium |  |

Độ phủ tổng: 96% (18/22 câu đạt medium; P0: 16/17). M06 (DSVN thay đổi gì, P1) từ 2 lên 54 evidence nhờ T-018 `news` nhưng chỉ 2 nguồn và 5 "tác giả" (3 báo + 2 người TripAdvisor) - là signal log, đọc theo dòng thời gian chứ không theo ngưỡng. C10 (khách Việt, P1) có 17 evidence nhưng 1 nguồn (`news`), chưa có tiếng nói khách Việt trực tiếp (`forum_vn` chưa chạy). M03 vẫn 2 nguồn.

- C01 tính từ taxonomy v0.8 (segment khách nước ngoài cụ thể → C01, Luan duyệt 2026-10-28): proxy ai hay viết, không phải cơ cấu khách thật.
- M05 script ghi `low` vì chỉ 1 nguồn (`serp_ai`) và 3 "tác giả" (3 engine). Theo `confidence.md`, `serp_ai` được đánh giá theo ảnh hưởng, không đếm số lượng → coi là **baseline đủ dùng** (30 cặp engine × prompt, 2026-10-28). Lượt 2 (T-016) mở từ 2026-10-31.

- Nguồn phía cung (`competitor_site`, `ad_library`) và báo chí (`news`, từ 2026-10-31) không tính vào share of voice người dùng, không suy nguồn gốc khách (origin = unknown) và không tính vào insight F/D (trừ insight có `include_news`).

**Đọc đúng:** medium = đủ *volume* để viết insight. Insight cho một thị trường cụ thể chỉ dùng origin tin cậy cao. Share of voice/số evidence là proxy, không phải thị phần.

## Evidence theo thị trường (origin)

| Thị trường | Mã | Evidence | Tin cậy cao | Tin cậy TB | Tác giả | Nguồn |
|---|---|---|---|---|---|---|
| Ấn Độ | in | 18 | 18 | 0 | 8 | 2 |
| Trung Quốc | cn | 17 | 17 | 0 | 4 | 2 |
| Đài Loan/Hồng Kông | tw_hk | 0 | 0 | 0 | 0 | 0 |
| Hàn Quốc | kr | 54 | 54 | 0 | 31 | 4 |
| Phương Tây | western | 36 | 36 | 0 | 12 | 3 |
| Châu Á khác | other_asia | 5 | 5 | 0 | 1 | 1 |
| Nước ngoài (chưa rõ nước) | intl | 257 | 236 | 21 | 166 | 5 |
| Expat | expat | 0 | 0 | 0 | 0 | 0 |
| Việt Nam | vn | 259 | 259 | 0 | 181 | 5 |
| Chưa rõ | unknown | 638 | 0 | 0 | 270 | 12 |

Trung Quốc gần như trống do Xiaohongshu/Mafengwo chặn đăng nhập (xem `source-map.md`). Ấn mỏng, Hàn tốt nhất trong wave M. Phương Tây tăng nhờ profile TripAdvisor (T-017).
