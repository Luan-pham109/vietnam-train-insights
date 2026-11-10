# Coverage

Cập nhật: 2026-11-10 (Claude). Nguồn: `05_outputs/dashboard/coverage.json`, `markets.json`. Ngưỡng theo `00_brain/confidence.md` (medium = ≥10 evidence, ≥3 nguồn, ≥5 tác giả). Chỉ tính evidence của task `reviewed`, bỏ dòng review lỗi.

Task reviewed: T-001 → T-020, T-022 (21/22; T-021 `reddit` lượt 2 đang rework - chỉ sửa `type` 2 dòng; T-014 TikTok bị chặn, 0 raw; T-015 `ad_library` chỉ Meta). Tổng 578 raw, 1642 evidence; dùng được 1506, 729 tác giả. Tỷ lệ evidence biết nguồn gốc khách (origin): 48%.

| Mã | Câu hỏi | Ưu tiên | Evidence | Nguồn | Tác giả | Evidence intl | Mức | |
|---|---|---|---|---|---|---|---|---|
| C01 | Khách nước ngoài đi tàu VN gồm những segment nào (backpacker, couple, family, senior, group tour)? | P0 | 47 | 6 | 20 | 47 | medium |  |
| C02 | Vì sao họ chọn tàu thay vì bay/xe (JTBD, trigger)? | P0 | 101 | 10 | 74 | 31 | medium |  |
| C03 | Họ tìm thông tin và đặt vé ở đâu, theo thứ tự nào? | P0 | 384 | 17 | 130 | 47 | medium |  |
| C04 | Barrier lớn nhất ở từng journey stage là gì? | P0 | 225 | 6 | 194 | 30 | medium |  |
| C05 | Họ lo gì về trust (vé giả, mất tiền, phí ẩn, không có ghế)? | P0 | 125 | 13 | 99 | 30 | medium |  |
| C06 | Họ chọn hạng/khoang thế nào, tiêu chí là gì (khoang 4 riêng, giường dưới, VIP)? | P0 | 272 | 14 | 203 | 138 | medium |  |
| C07 | Chặng cuối từ ga đến điểm đến (Sa Pa, Hội An, Hạ Long...) xử lý thế nào, đau ở đâu? | P0 | 69 | 8 | 64 | 9 | medium |  |
| C08 | Tuyến/combo nào họ muốn mà không có chuyến thẳng? | P1 | 88 | 8 | 55 | 13 | medium |  |
| C09 | Thanh toán, tiền tệ, giấy tờ (hộ chiếu, tên trên vé) gây vấn đề gì? | P0 | 33 | 11 | 27 | 5 | medium |  |
| C11 | Khách Ấn, Trung, Hàn khác khách phương Tây thế nào ở lý do đi tàu, hạng ghế, barrier? | P0 | 45 | 7 | 28 | 41 | medium |  |
| C12 | Mỗi thị trường cần gì riêng: ví thanh toán, ngôn ngữ, đồ ăn (chay/kiêng), đi theo nhóm/gia đình? | P0 | 15 | 5 | 14 | 7 | medium |  |
| C10 | Khách Việt đi tàu vì gì, đau gì (Tết, hoàn đổi, giá)? | P1 | 57 | 2 | 39 | 0 | low |  |
| M01 | Kênh nào được nhắc/recommend nhiều nhất (dsvn.vn, 12Go, Baolau, Trip.com, Traveloka, Klook, agent, quầy ga)? | P0 | 319 | 17 | 87 | 37 | medium |  |
| M02 | Từng kênh được khen/chê vì gì (giá, phí, UX, hỗ trợ, độ tin cậy)? | P0 | 72 | 5 | 49 | 0 | medium |  |
| M03 | Đối thủ định vị và quảng cáo gì (messaging, offer)? | P1 | 25 | 2 | 14 | 0 | low |  |
| M04 | Tàu du lịch tư nhân (Lotus, Chapa Express, Violette, SapaLy, Livitrans...) được nhìn nhận thế nào so với tàu DSVN? | P0 | 150 | 10 | 126 | 101 | medium |  |
| M05 | AI engine/SERP đang recommend ai khi hỏi cách đặt vé tàu VN? | P0 | 216 | 1 | 3 | 0 | low | ⚠ P0 < medium |
| M07 | Mỗi thị trường đặt vé tàu VN qua kênh nào (Trip.com/Ctrip, Fliggy, MakeMyTrip, MyRealTrip, Klook, KKday...)? Họ tìm thông tin trên nền tảng nào? | P0 | 12 | 4 | 12 | 12 | medium |  |
| M06 | Chính sách, giá, tàu mới, sản lượng của DSVN thay đổi gì? | P1 | 57 | 2 | 5 | 0 | low |  |
| I01 | Tip/workaround người đi thật hay chia sẻ là gì? | P0 | 259 | 12 | 146 | 37 | medium |  |
| I02 | "Ước gì biết trước" - kỳ vọng vs thực tế trên tàu/tại ga? | P0 | 199 | 7 | 185 | 71 | medium |  |
| I03 | Tuyến/đoạn nào được khen là đẹp, đáng đi (Hải Vân, ven biển...)? | P1 | 76 | 10 | 61 | 20 | medium |  |

Độ phủ tổng: 97% (18/22 câu đạt medium; P0: 16/17). C10 (khách Việt, P1) 57 evidence, 39 tác giả nhưng mới 2 nguồn (`news`, `forum_vn`) → còn `low`, cần thêm 1 nguồn Việt (vd review app DSVN tiếng Việt, FB group Việt). M06 (57 evidence), M03 vẫn 2 nguồn; T-022 news lượt 2 chỉ thêm 3 evidence (1 bài).

- C01 tính từ taxonomy v0.8 (segment khách nước ngoài cụ thể → C01, Luan duyệt 2026-10-28): proxy ai hay viết, không phải cơ cấu khách thật.
- M05 script ghi `low` vì chỉ 1 nguồn (`serp_ai`) và 3 "tác giả" (3 engine). Theo `confidence.md`, `serp_ai` đánh giá theo ảnh hưởng → coi là đủ dùng. Đã có **2 lượt** (T-009 2026-10-27/28, T-016 2026-11-04), 60 cặp engine × prompt. Google 2 lượt khác IP (Mỹ → VN) nên không so xu hướng Google. Perplexity chặn cả 2 lượt.

- Nguồn phía cung (`competitor_site`, `ad_library`), báo chí (`news`) và đáp án AI (`serp_ai`, từ 2026-11-05) không tính vào share of voice người dùng, không suy nguồn gốc khách (origin = unknown). Trước đó ngôn ngữ prompt `serp_ai` (tiếng Trung/Hàn/Việt) bị tính nhầm thành khách cn/kr/vn: cn 17 → 4, kr 54 → 47, vn 259 → 242.

**Đọc đúng:** medium = đủ *volume* để viết insight. Insight cho một thị trường cụ thể chỉ dùng origin tin cậy cao. Share of voice/số evidence là proxy, không phải thị phần.

## Evidence theo thị trường (origin)

| Thị trường | Mã | Evidence | Tin cậy cao | Tin cậy TB | Tác giả | Nguồn |
|---|---|---|---|---|---|---|
| Ấn Độ | in | 18 | 18 | 0 | 8 | 2 |
| Trung Quốc | cn | 4 | 4 | 0 | 1 | 1 |
| Đài Loan/Hồng Kông | tw_hk | 0 | 0 | 0 | 0 | 0 |
| Hàn Quốc | kr | 47 | 47 | 0 | 28 | 3 |
| Phương Tây | western | 37 | 37 | 0 | 13 | 3 |
| Châu Á khác | other_asia | 5 | 5 | 0 | 1 | 1 |
| Nước ngoài (chưa rõ nước) | intl | 260 | 239 | 21 | 166 | 5 |
| Expat | expat | 0 | 0 | 0 | 0 | 0 |
| Việt Nam | vn | 358 | 358 | 0 | 261 | 5 |
| Chưa rõ | unknown | 777 | 0 | 0 | 271 | 12 |

Trung Quốc gần như trống (4 evidence, 1 tác giả) do Xiaohongshu/Mafengwo chặn đăng nhập (xem `source-map.md`). Ấn mỏng, Hàn tốt nhất trong wave M.
