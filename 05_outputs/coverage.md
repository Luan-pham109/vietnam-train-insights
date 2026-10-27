# Coverage

Cập nhật: 2026-10-27 (Claude). Nguồn: `05_outputs/dashboard/coverage.json`, `markets.json`. Ngưỡng theo `00_brain/confidence.md` (medium = ≥10 evidence, ≥3 nguồn, ≥5 tác giả).

Task reviewed: T-001, T-003, T-004. T-005 `rework` (sót 2 chỗ PII), T-002 `rework` (raw diễn giải, không nguyên văn + PII) - evidence của hai task vẫn được tính vào volume vì tag đúng, nhưng quote T-002 **không dùng trong insight** cho tới khi Muse đọc lại nguyên văn. Tổng 380 raw, 696 evidence (635 dùng được), 440 tác giả.

| Mã | Nhóm | Câu hỏi | Ưu tiên | Evidence | Nguồn | Tác giả | Evidence intl | Mức | |
|---|---|---|---|---|---|---|---|---|---|
| C01 | Khách hàng | Khách nước ngoài đi tàu VN gồm những segment nào (backpacker, couple, family, senior, group tour)? | P0 | 0 | 0 | 0 | 0 | none | ⚠ P0 < medium |
| C02 | Khách hàng | Vì sao họ chọn tàu thay vì bay/xe (JTBD, trigger)? | P0 | 29 | 4 | 24 | 0 | medium |  |
| C03 | Khách hàng | Họ tìm thông tin và đặt vé ở đâu, theo thứ tự nào? | P0 | 68 | 4 | 59 | 7 | medium |  |
| C04 | Khách hàng | Barrier lớn nhất ở từng journey stage là gì? | P0 | 204 | 5 | 185 | 8 | medium |  |
| C05 | Khách hàng | Họ lo gì về trust (vé giả, mất tiền, phí ẩn, không có ghế)? | P0 | 64 | 5 | 61 | 3 | medium |  |
| C06 | Khách hàng | Họ chọn hạng/khoang thế nào, tiêu chí là gì (khoang 4 riêng, giường dưới, VIP)? | P0 | 90 | 4 | 79 | 7 | medium |  |
| C07 | Khách hàng | Chặng cuối từ ga đến điểm đến (Sa Pa, Hội An, Hạ Long...) xử lý thế nào, đau ở đâu? | P0 | 45 | 4 | 44 | 2 | medium |  |
| C08 | Khách hàng | Tuyến/combo nào họ muốn mà không có chuyến thẳng? | P1 | 37 | 4 | 32 | 2 | medium |  |
| C09 | Khách hàng | Thanh toán, tiền tệ, giấy tờ (hộ chiếu, tên trên vé) gây vấn đề gì? | P0 | 17 | 5 | 16 | 2 | medium |  |
| C11 | Khách hàng | Khách Ấn, Trung, Hàn khác khách phương Tây thế nào ở lý do đi tàu, hạng ghế, barrier? | P0 | 1 | 1 | 1 | 0 | low | ⚠ P0 < medium |
| C12 | Khách hàng | Mỗi thị trường cần gì riêng: ví thanh toán, ngôn ngữ, đồ ăn (chay/kiêng), đi theo nhóm/gia đình? | P0 | 9 | 2 | 9 | 1 | low | ⚠ P0 < medium |
| C10 | Khách hàng | Khách Việt đi tàu vì gì, đau gì (Tết, hoàn đổi, giá)? | P1 | 0 | 0 | 0 | 0 | none |  |
| M01 | Cạnh tranh & thị trường | Kênh nào được nhắc/recommend nhiều nhất (dsvn.vn, 12Go, Baolau, Trip.com, Traveloka, Klook, agent, quầy ga)? | P0 | 37 | 4 | 33 | 3 | medium |  |
| M02 | Cạnh tranh & thị trường | Từng kênh được khen/chê vì gì (giá, phí, UX, hỗ trợ, độ tin cậy)? | P0 | 39 | 3 | 39 | 0 | medium |  |
| M03 | Cạnh tranh & thị trường | Đối thủ định vị và quảng cáo gì (messaging, offer)? | P1 | 0 | 0 | 0 | 0 | none |  |
| M04 | Cạnh tranh & thị trường | Tàu du lịch tư nhân (Lotus, Chapa Express, Violette, SapaLy, Livitrans...) được nhìn nhận thế nào so với tàu DSVN? | P0 | 20 | 4 | 18 | 1 | medium |  |
| M05 | Cạnh tranh & thị trường | AI engine/SERP đang recommend ai khi hỏi cách đặt vé tàu VN? | P0 | 0 | 0 | 0 | 0 | none | ⚠ P0 < medium |
| M07 | Cạnh tranh & thị trường | Mỗi thị trường đặt vé tàu VN qua kênh nào (Trip.com/Ctrip, Fliggy, MakeMyTrip, MyRealTrip, Klook, KKday...)? Họ tìm thông tin trên nền tảng nào? | P0 | 0 | 0 | 0 | 0 | none | ⚠ P0 < medium |
| M06 | Cạnh tranh & thị trường | Chính sách, giá, tàu mới, sản lượng của DSVN thay đổi gì? | P1 | 2 | 1 | 2 | 0 | low |  |
| I01 | Insider | Tip/workaround người đi thật hay chia sẻ là gì? | P0 | 56 | 2 | 49 | 0 | low | ⚠ P0 < medium |
| I02 | Insider | "Ước gì biết trước" - kỳ vọng vs thực tế trên tàu/tại ga? | P0 | 126 | 3 | 112 | 1 | medium |  |
| I03 | Insider | Tuyến/đoạn nào được khen là đẹp, đáng đi (Hải Vân, ven biển...)? | P1 | 34 | 4 | 30 | 2 | medium |  |

Độ phủ tổng: 69% (13/22 câu đạt medium; P0: 11/17).

**Đọc đúng:** đạt medium ở đây là đủ *volume* để viết insight, chưa phải đủ cho segment khách nước ngoài. Gần như toàn bộ evidence có `segment/market: unknown` (Google Maps, App Store, FB không tự nhận quốc tịch), và 16/37 dòng App Store nói về tàu nước khác. Insight riêng cho `intl_*` vẫn dưới ngưỡng ở mọi câu.

## Evidence theo thị trường

| Thị trường | Mã | Evidence | Tác giả | Nguồn |
|---|---|---|---|---|
| Ấn Độ | in | 0 | 0 | 0 |
| Trung Quốc | cn | 0 | 0 | 0 |
| Đài Loan/Hồng Kông | tw_hk | 0 | 0 | 0 |
| Hàn Quốc | kr | 0 | 0 | 0 |
| Phương Tây | western | 3 | 3 | 2 |
| Châu Á khác | other_asia | 0 | 0 | 0 |
| Việt Nam | vn | 0 | 0 | 0 |
| Chưa rõ | unknown | 632 | 438 | 5 |

Ấn/Trung/Hàn = 0: chờ T-006/T-007/T-008 (wave M). Share of voice/số evidence là proxy, không phải thị phần.
