# Insight nháp - chờ Luan review

Tự sinh bởi `tools/insight_draft.py`. Số evidence tính theo topic; tin cậy chỉ tính evidence của task đã reviewed (ngưỡng: ≥10 ev, ≥3 nguồn, ≥5 tác giả).

| ID | Insight | Nhóm khách | Ev (đã duyệt / tổng) | Nguồn | Tin cậy | Gắn với Vexere | Hành động đề xuất |
|---|---|---|---|---|---|---|---|
| INS-001 | Lúc bước ra khỏi ga là điểm mất trust lớn nhất của chặng cuối: chèo kéo, hét giá, giả tài xế; khách tự vệ bằng Grab hoặc đặt xe trước | Xem card | - / 22 | 3 | trung bình | Card đầy đủ trong 04_insights | Add-on chặng cuối (BRD hướng dẫn chặng cuối train): ưu tiên ga có pain rõ nhất **Lào Cai → Sa Pa**, rồi Huế, Đà Nẵng. Bán xe đón đặt trước (tên khách trên bảng, biển số gửi trước) - trả lời đúng nỗi sợ "giả tài xế". |
| INS-002 | Nhà vệ sinh (ở ga và trên tàu) là pain vệ sinh lặp lại nhiều nhất; khách đã quen tự chuẩn bị, chất lượng khác nhau rõ theo ga | Xem card | - / 25 | 3 | trung bình | Card đầy đủ trong 04_insights | Pre-trip checklist trên e-ticket: mang khăn ướt/giấy, lót gối, khẩu trang - giảm gap kỳ vọng (I02), giảm review xấu đổ về kênh bán. |
| INS-003 | Khách không phân biệt được site chính thức với site trung gian bán vé DSVN giá cao gấp nhiều lần; cộng đồng tự "dạy nhau" dsvn.vn là chính thức | Xem card | - / 10 | 2 | thấp | Card đầy đủ trong 04_insights | Trust signal là điều kiện cần cho kênh bán vé tàu cho khách nước ngoài: ghi rõ "giá vé = giá DSVN + phí dịch vụ X", hiển thị giá VND gốc, nói rõ quan hệ với DSVN. |
| D01 | Khách nước ngoài muốn đặt kênh chính thức nhưng bị đẩy sang trung gian giá cao: dsvn.vn khó dùng, thẻ quốc tế lỗi, Vexere đòi số điện thoại VN | Nước ngoài | 31 / 31 | 5 | trung bình | Trực tiếp: lỗi của chính Vexere | Kiểm tra ngay flow đặt vé EN: cho nhập số điện thoại quốc tế, test thẻ quốc tế; đo tỷ lệ rớt ở bước nhập SĐT |
| D02 | Chọn khoang và chỗ là nỗi lo lớn nhất trước chuyến: khoang 4 riêng, giường dưới, cả nhóm cùng 1 khoang, bên nào ngắm cảnh - và bị xếp khác với chỗ đã đặt | Nước ngoài | 91 / 91 | 6 | trung bình | Trực tiếp: UI chọn chỗ, card vé | Sơ đồ khoang rõ trên trang chọn chỗ EN (giường dưới/trên, khoang 4/6, hướng ngồi), nút 'đặt trọn khoang' |
| D03 | Khách không phân biệt được tàu mới với tàu cũ qua mã tàu (SE3 sạch hơn SE13), trong khi đây là yếu tố quyết định trải nghiệm | Nước ngoài | 26 / 26 | 4 | trung bình | Trực tiếp: hạng mục phân loại tàu Q4 | Gắn nhãn chất lượng/năm đóng toa theo mã tàu trên card vé |
| D04 | Toa tư nhân (Lotus, Livitrans, Chapa...) bị hoài nghi có đáng tiền không so với tàu SE đã nâng cấp; khách thấy chủ yếu trả cho trang trí và đồ ăn nhẹ | Nước ngoài | 40 / 40 | 4 | trung bình | Trực tiếp: mở bán tàu du lịch tư nhân | Card so sánh toa tư nhân vs SE cùng chuyến (giá, dịch vụ khác gì); review thật trên trang tàu tư nhân |
| D05 | Hiểu nhầm về thời điểm mở bán: thấy 'hết vé' nhưng thực ra chưa mở (60/30 ngày); khoang 4 và giường dưới hết sớm vào cuối tuần | Nước ngoài | 42 / 42 | 5 | trung bình | Trực tiếp: hiển thị trạng thái chuyến | Hiển thị 'chưa mở bán - mở ngày X' thay cho 'hết vé'; nhắc khi mở bán |
| D06 | Đoạn Huế - Đà Nẵng (Hải Vân) là lý do chính để đi tàu ban ngày; khách hỏi ngồi bên nào nhưng toa đảo chiều làm hỏng kỳ vọng | Nước ngoài | 45 / 45 | 4 | trung bình | Content/SEO + UI chọn chỗ | Trang tuyến Huế - Đà Nẵng: bên ngồi ngắm biển theo chiều đi, cảnh báo toa có thể đảo chiều |
| D07 | Thu phí ngầm tại ga: gửi hành lý, porter đòi tiền, phòng chờ 'miễn phí' rồi tính tiền, giá vé khác nhau giữa các lần mua | Cả hai | 25 / 25 | 3 | trung bình | Gián tiếp: trust + pre-trip guide | Email/e-ticket: các khoản không phải trả tại ga, giá tham chiếu gửi đồ |
| D08 | Khách Việt phàn nàn app/web DSVN: thanh toán rườm rà, tải vé lỗi, đặt nhầm ngày | Việt Nam | 18 / 18 | 2 | thấp | Cơ hội: Vexere là kênh thay thế dễ hơn | Messaging 'đặt vé tàu không rườm rà' cho khách Việt; so sánh số bước thanh toán Vexere vs DSVN |
| D09 | Phòng chờ nóng, không điều hoà, quá tải ở nhiều ga - khách Việt phàn nàn nhiều nhất | Việt Nam | 7 / 7 | 1 | thấp | Thấp: Vexere không kiểm soát được | Chỉ dùng cho pre-trip guide (đến ga vừa đủ giờ); không ưu tiên |
| D10 | Thái độ nhân viên ga (bảo vệ, soát vé) phân cực mạnh theo từng ga, là lý do chính của review 1 sao | Việt Nam | 35 / 35 | 1 | thấp | Thấp: thuộc DSVN | Không hành động trực tiếp; có thể chia sẻ với DSVN như feedback đối tác |
| D11 | Khách Ấn lo nhất chuyện đồ chay khi đi tàu VN: hỏi có đồ chay không, mang đồ ăn sẵn theo; vlogger Ấn hay quy giá vé ra rupee | Ấn Độ | 11 / 11 | 2 | thấp | Trực tiếp: nội dung + bộ lọc/ghi chú dịch vụ ăn chay, hiển thị giá quy đổi INR | FAQ/landing tiếng Anh cho khách Ấn: đồ chay trên tàu và tại ga; cân nhắc INR trong currency switch |

## Quote tiêu biểu
- **INS-001**: "a man suddenly ran towards us, claimed to be our driver, and took us to our destination."
- **INS-002**: "The toilets are sooo dirty, they also occasionally will just launch piss when you push the flush button."
- **INS-003**: " dsvn.vn là chính thức

## Bằng chứng
- "
- **D01**: "Vexere doesn't let me book without VN number.." - _Mới 1 quote nhắc Vexere - cần kiểm chứng bằng funnel nội bộ, đây là giả thuyết đáng test nhất_
- **D02**: "been assigned to the top bunk in a 6 berth cabin when I had booked a bottom bunk in a 4 berth"
- **D03**: "SE3 was very clean, modern and slightly longer beds than SE13. SE13 was old and not as clean."
- **D04**: "you are just paying extra for some snacks and a decorated carriage with colourful bedding" - _Phần lớn evidence từ T-002 đang làm lại_
- **D05**: "It looks fully booked but it means not avible yet so far in advance"
- **D06**: "I booked coach 1, seat 16 which was supposed to be the ocean view but unfortunately my carriage was switched around"
- **D07**: "he will demand a tip which was unexpected as he is a train staff"
- **D08**: "Hình thức thanh toán quá phức tạp, hãy đơn giản quy trình và đa dạng ngân hàng sao cho thuận tiện. Lằng nhằng quá, rất muốn bỏ cuộc"
- **D09**: "NHƯNG NHÀ GA KHÔNG CÓ ĐIỀU HOÀ !!"
- **D10**: "nhân viên soát vé thái độ vô cùng, khách đang vội hỏi thì không hướng dẫn"
- **D11**: "Availability of veg food in Vietnam or ready made food packets should be carried?" - _Mỏng: chủ yếu vlog YouTube (creator), 2 bài Reddit_
