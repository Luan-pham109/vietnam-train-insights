# Insight tàu hoả Việt Nam - bản tổng hợp 2026-10-28

Nguồn: 14 task (T-001 đến T-014) đã review, 1.275 evidence từ 485 bài gốc, 16 nguồn (Reddit, TripAdvisor forum + review, Google Maps ga, app store, FB group, YouTube EN/Ấn/Hàn, Naver, Tistory, Ctrip, Seat61, AI engine, trang đối thủ). Tin cậy chỉ tính evidence của task đã duyệt, không bị đánh lỗi. Ngưỡng "trung bình": ≥10 evidence, ≥3 nguồn, ≥5 tác giả. Mọi quote truy ngược được bằng `ev_id` trong `03_evidence/`.

## Tóm tắt

1. **Khoảng trống lớn nhất của Vexere nằm ở AI engine và trang tàu EN, không phải ở sản phẩm.** AI gợi ý dsvn.vn đầu tiên 20/30 lượt hỏi; Vexere được nhắc 11/30, riêng ChatGPT 1/10 - dù vexere.com là domain AI trích dẫn nhiều nhất (5/15 lượt có nguồn). Trang tàu EN của Vexere chưa có tàu tư nhân trong khi mọi đối thủ đều bán (F02, F14).
2. **Nỗi lo số 1 trước chuyến là chọn khoang/giường** (F03, 217 evidence, 12 nguồn) - trùng đúng hạng mục UI phân loại tàu Q4.
3. **Tàu tư nhân không bán được bằng lời hứa "ngủ ngon"**: được khen đồ ăn, nhân viên; bị chê ồn, giá, bị đổi cabin - 2/3 ca đổi cabin là Chapa Express, hãng Vexere onboard đầu tiên (F04, F05).
4. **Trust đứt ở 2 điểm: site giả dạng DSVN và cửa ga** (chèo kéo, giả tài xế, thu phí ngầm) - F01, F08, F09.
5. **Khách Hàn đã tự tìm tới Vexere** (F11) - insight trỏ thẳng vào Vexere rõ nhất; khách Trung gần như không thu được qua web công khai.

## Khách là ai (C01, C02) - đọc với phản biện
- Dữ liệu social **không đo được cơ cấu khách**. Trong evidence khách nước ngoài có nhóm rõ: gia đình (26 evidence, 12 tác giả), đoàn/tour (10, 6), cặp đôi (11, 3); 286 evidence khách nước ngoài không rõ nhóm.
- Thị trường xác định được (tự nhận hoặc nền tảng bản địa): Hàn 49 evidence/30 tác giả, phương Tây 21/7, Ấn 18/8, Trung 7/3. Đây là độ dày nội dung công khai, **không phải tỷ trọng khách** - phải lấy từ booking nội bộ theo quốc tịch.
- Lý do chọn tàu (C02, 73 evidence): trải nghiệm, rẻ hơn, tránh say xe, ngủ qua đêm thay khách sạn; lý do bỏ tàu: đắt ngang máy bay ở một số chặng, chậm. Mẫu nhỏ - chỉ dùng làm giả thuyết cho messaging.

## Cạnh tranh - share of voice (proxy, không phải thị phần)
Nhắc tên kênh trong nội dung người dùng (không tính AI engine, Seat61, trang đối thủ):

| Kênh | Evidence | Tác giả | Ghi chú |
|---|---|---|---|
| dsvn.vn | 25 | 22 | Được dạy nhau là "chính thức", kèm mẹo VNPay |
| Baolau | 20 | 13 | Được khen nhiều nhất trong kênh trung gian (14 tích cực) |
| 12Go | 16 | 11 | Nhắc nhiều, ít khen hơn Baolau |
| Vexere | 8 | 8 | 3 khách Hàn kể đặt qua app; 3 lời khuyên dùng Vexere (FB, Reddit); 1 phàn nàn SĐT |
| Quầy ga | 7 | 7 | Giá gốc, chỉ tiền mặt |
| Klook | 5 | 5 | Chủ yếu khách Hàn |

AI engine (F02) và Seat61 xếp tương tự: dsvn.vn → Baolau/12Go. Seat61 không nhắc Vexere; Gemini có lượt xếp Vexere "Best Overall for Foreign Travelers".

## Insight chi tiết

## Kênh đặt vé & trust

### F01 - dsvn.vn dùng được với khách nước ngoài nếu biết mẹo (chọn VNPay, có Apple Pay trên app iOS, thêm số 0 trước số điện thoại); khách không biết mẹo thì sang Baolau/12Go chấp nhận trả thêm phí để thẻ nước ngoài chạy được; site giả dạng DSVN bắt trả gấp nhiều lần giá ga
- **Nhóm khách:** Nước ngoài · **Tin cậy:** trung bình · **Bằng chứng:** 131 evidence, 108 tác giả, 7 nguồn (appstore, gmaps_station, muse_fb_radar, reddit, tripadvisor, tripadvisor_review, youtube)
- **Quote:**
  - "Choose the vnpay option when it comes to paying and there's no problem using international cards." `reddit-20261026-0020-e02`
  - "Should’ve used Baolau, its a little bit more expensive than the official VR website but you can pay using any sort of card." `reddit-20261026-0007-e04`
  - "At the station the price for the return tickets were only 27 USD (700K VND) for both of us" `reddit-20261026-0007-e02`
- **So what cho Vexere:** Landing EN: 'đại lý chính thức DSVN' + giá all-in so với giá ga + thẻ quốc tế/Apple Pay chạy ngay, không cần mẹo; kiểm ô SĐT trong flow EN nhận số quốc tế (có 1 phàn nàn 'Vexere doesn't let me book without VN number', dsvn cũng cần mẹo thêm số 0)
- **Phản biện:** Ô số điện thoại và lỗi thẻ mới có vài evidence - là giả thuyết cần đo funnel, không phải kết luận; Reddit/TripAdvisor lệch về khách tự lên kế hoạch

### F02 - AI engine gợi ý dsvn.vn đầu tiên ở 20/30 lượt hỏi; Vexere được nhắc 11/30 (ChatGPT 1/10, Gemini 5/10, Google AI 5/10). Trong 15 lượt có dẫn nguồn, vexere.com được trích ở 5 lượt (nhiều nhất, dsvn.vn 4) - nội dung Vexere đã được AI dùng làm nguồn nhưng chưa thành lời gợi ý đặt vé ở ChatGPT
- **Nhóm khách:** Khách hỏi AI (proxy) · **Tin cậy:** đo lường · **Bằng chứng:** 119 evidence, 3 tác giả, 1 nguồn (serp_ai)
- **Quote:**
  - "1. Best Overall for Foreign Travelers: Vexere [...] vexere.com/vn/trains.en" `serp_ai-20261027-gemini-p02-e01`
  - "Option 1: Official Vietnam Railways website" `serp_ai-20261027-chatgpt-p01-e01`
- **So what cho Vexere:** Đặt baseline AEO: 10 prompt × 3 engine, mục tiêu tăng Vexere từ 11/30 lượt; nội dung answer-first nêu tên thương hiệu trong câu trả lời (không chỉ là nguồn); ưu tiên ChatGPT (1/10)
- **Phản biện:** 1 lần chạy/engine/prompt, dao động cao - đọc là mốc, chưa phải xu hướng · Dao động mạnh giữa 2 ngày chạy; Google ra IP Mỹ; Perplexity bị chặn

## Chọn chỗ & sản phẩm tàu

### F03 - Chọn khoang và giường là nỗi lo lớn nhất trước chuyến: khoang 4 riêng, giường dưới, cả nhóm cùng khoang, bên nào ngắm cảnh, tàu mới hay cũ (SE3 khác SE13); có ca bị xếp khác chỗ đã đặt (giường trên thay vì dưới, toa đổi chiều)
- **Nhóm khách:** Nước ngoài (cả Tây và Hàn) · **Tin cậy:** trung bình · **Bằng chứng:** 217 evidence, 180 tác giả, 12 nguồn (gmaps_station, muse_fb_radar, naver_blog, reddit, reddit_in, tistory, trip_com_cn, tripadvisor, tripadvisor_review, youtube, youtube_in, youtube_kr)
- **Quote:**
  - "having traveled several times by train and been assigned to the top bunk in a 6 berth cabin when I had booked a bottom bunk in a 4 berth" `muse_fb_radar-20261026-0014-e03`
  - "Book/pay for a 4 bed room all to yourself. People in hard seats will try to get an empty bed." `reddit-20261026-0022-e01`
  - "we booked a standard/local 4 berth soft sleeper on 2 trains. SE3 was very clean, modern and slightly longer beds than SE13." `tripadvisor-20261026-0026-e05`
- **So what cho Vexere:** Sơ đồ khoang EN (tầng giường, khoang 4/6, hướng ngồi), nút đặt trọn khoang, nhãn chất lượng/năm đóng toa theo mã tàu
- **Phản biện:** Câu hỏi trước chuyến chiếm nhiều; chưa đo được tỷ lệ bị xếp sai thực tế

### F04 - Tàu tư nhân phân cực mạnh theo hãng: được khen đồ ăn và nhân viên, nhưng vẫn ngủ kém vì toa gắn đoàn tàu DSVN; bị chê giá không xứng; 3 review (2 là Chapa Express) kể bị đổi sang cabin chung dù đã trả tiền cabin VIP/riêng. Vietage (15/15 khen), Lotus được khen; Sapaly, Livitrans, Laman bị chê nhiều; Chapa Express, Violette lẫn lộn
- **Nhóm khách:** Nước ngoài · **Tin cậy:** trung bình · **Bằng chứng:** 205 evidence, 158 tác giả, 9 nguồn (gmaps_station, muse_fb_radar, naver_blog, reddit, seat61, tripadvisor, tripadvisor_review, youtube, youtube_in)
- **Quote:**
  - "What we actually got: two bunk beds in a shared 4-berth cabin with two strangers. That is not an upgrade. It is a downgrade dressed up in the word “upgrade.”" `tripadvisor_review-20261027-0001-e10`
  - "This was amazing. The view is very nice, the food is awsome and the service was impeccable. I really recommand" `tripadvisor_review-20261027-0007-e10`
  - "A friend recently went on lotus and aircon stopped frequently throughout the night." `tripadvisor-20261026-0026-e06`
- **So what cho Vexere:** Trước khi mở bán Chapa: chốt với hãng cam kết đúng cabin đã đặt + chính sách hoàn tiền khi đổi cabin; trang hãng ghi rõ toa gắn đoàn tàu nào, khác toa thường ở đâu; review thật theo hãng; không quảng cáo 'ngủ ngon'
- **Phản biện:** TripAdvisor review lệch về trải nghiệm cực đoan; mỗi hãng ≤15 review

### F05 - Ngủ kém trên tàu đêm (ồn, xóc, loa thông báo mỗi ga) là pain lặp lại ở cả toa DSVN lẫn toa tư nhân, kể cả khi cabin được khen sạch đẹp
- **Nhóm khách:** Nước ngoài · **Tin cậy:** trung bình · **Bằng chứng:** 30 evidence, 29 tác giả, 7 nguồn (gmaps_station, muse_fb_radar, naver_blog, reddit, tripadvisor, tripadvisor_review, youtube)
- **Quote:**
  - "We did not get a good night's sleep. The track was rough and the train bounced, swayed and bumped. It was noisy." `tripadvisor-20261026-0016-e05`
  - "Toilet is pre-departure clean. But very obvious is the sound of the people next door." `reddit-20261026-0004-e01`
  - "Tàu chạy rất ồn." `gmaps_station-20261026-0059-e02`
- **So what cho Vexere:** Pre-trip: nút tai, bịt mắt, giờ dừng ga; không hứa 'ngủ ngon' trong copy
- **Phản biện:** Người ngủ ngon ít viết review

## Đặt vé

### F06 - Hiểu nhầm thời điểm mở bán: thấy 'hết vé' nhưng thực ra chưa mở (60/30 ngày); khoang 4 và giường dưới hết sớm vào cuối tuần, lễ
- **Nhóm khách:** Nước ngoài · **Tin cậy:** trung bình · **Bằng chứng:** 46 evidence, 33 tác giả, 7 nguồn (appstore, gmaps_station, muse_fb_radar, reddit, seat61, tripadvisor, youtube)
- **Quote:**
  - "some bookingsites start sale 1 month before travel. It looks fully booked but it means not avible yet so far in advance" `muse_fb_radar-20261026-0003-e02`
  - "Sleeper 4-berth soft compartments sell out 2-5 days ahead on Lao Cai-Hanoi, especially Fri/Sat/Sun departures" `reddit-20261026-0012-e02`
  - "I guess you have to face a harsh reality..2 berth sleeper cabins are few + very hard to book - due to lack of availability - especially at this late date." `tripadvisor-20261026-0033-e01`
- **So what cho Vexere:** Hiện 'chưa mở bán - mở ngày X' thay cho 'hết vé' + nhắc khi mở bán
- **Phản biện:** Quy tắc mở bán do DSVN đổi theo mùa (Tết) - cần nguồn chính thức

## Nội dung & tuyến

### F07 - Đoạn Huế - Đà Nẵng (đèo Hải Vân) là lý do chính để đi tàu ban ngày, khách Tây và khách Hàn cùng nhắc; khách hỏi ngồi bên nào nhưng toa có thể bị đổi chiều làm sai kỳ vọng
- **Nhóm khách:** Nước ngoài · **Tin cậy:** trung bình · **Bằng chứng:** 67 evidence, 54 tác giả, 8 nguồn (gmaps_station, muse_fb_radar, naver_blog, reddit, tistory, tripadvisor, tripadvisor_review, youtube)
- **Quote:**
  - "I booked coach 1, seat 16 which was supposed to be the ocean view but unfortunately my carriage was switched around" `reddit-20261026-0021-e03`
  - "The 2 bed cab8n is fir 10 am train reach8ng Da nang at 6 am in morning, so the scenic part is in dark I think" `tripadvisor-20261026-0035-e09`
  - "that's South to North, seat on the right side of the train for the coastal view" `muse_fb_radar-20261026-0005-e02`
- **So what cho Vexere:** Trang tuyến Huế - Đà Nẵng: bên ngắm biển theo chiều đi, cảnh báo đổi chiều; tàu di sản HD
- **Phản biện:** Ít liên quan chuyển đổi trực tiếp

## Tại ga & chặng cuối

### F08 - Lúc bước ra khỏi ga là điểm mất trust lớn nhất: chèo kéo, hét giá, giả tài xế (Lào Cai, Huế); khách tự vệ bằng Grab hoặc đặt xe trước
- **Nhóm khách:** Cả hai · **Tin cậy:** trung bình · **Bằng chứng:** 49 evidence, 47 tác giả, 6 nguồn (gmaps_station, muse_fb_radar, reddit, reddit_in, tripadvisor, youtube)
- **Quote:**
  - "a man suddenly ran towards us, claimed to be our driver, and took us to our destination." `gmaps_station-20261026-0087-e01`
  - "Just say no thank you and ignore. The shuttle from lao cai is 55k." `reddit-20261026-0010-e04`
  - "beware of random local taxi drivers may scam passengers by tampering with meters" `gmaps_station-20261026-0012-e01`
- **So what cho Vexere:** Bán xe đón đặt trước có tên khách + biển số gửi trước; FAQ theo ga (Grab có ở Lào Cai không)
- **Phản biện:** Google Maps lệch về phàn nàn; chưa biết tần suất thật

### F09 - Thu phí ngầm tại ga: gửi hành lý, porter đòi tiền, phòng chờ 'miễn phí' rồi tính tiền
- **Nhóm khách:** Cả hai · **Tin cậy:** trung bình · **Bằng chứng:** 26 evidence, 25 tác giả, 4 nguồn (gmaps_station, muse_fb_radar, reddit, tistory)
- **Quote:**
  - "For luggage they charge you 100000 VND." `gmaps_station-20261026-0019-e01`
  - "he will demand a tip which was unexpected as he is a train staff" `gmaps_station-20261026-0167-e01`
  - "Bảo vào phòng chờ VIP miễn phí,bảo lựa đồ ăn đồ uống thoải mái đi xong tính 120k." `gmaps_station-20261026-0063-e01`
- **So what cho Vexere:** E-ticket/email: khoản nào không phải trả tại ga, giá tham chiếu gửi đồ
- **Phản biện:** Tập trung ở vài ga

### F10 - Nhà vệ sinh (ở ga và trên tàu) là pain vệ sinh lặp lại nhiều nhất; khách đã quen tự chuẩn bị, chất lượng khác rõ theo ga
- **Nhóm khách:** Cả hai · **Tin cậy:** trung bình · **Bằng chứng:** 24 evidence, 23 tác giả, 5 nguồn (gmaps_station, muse_fb_radar, reddit, tripadvisor, tripadvisor_review)
- **Quote:**
  - "The toilets are sooo dirty, they also occasionally will just launch piss when you push the flush button." `reddit-20261026-0001-e02`
  - "Toilets are generally good at the start of a trip but can get a bit grim towards the end." `tripadvisor-20261026-0001-e05`
  - "nhà vệ sinh công cộng thường xuyên rơi vào tình trạng ẩm thấp, có mùi khó chịu" `gmaps_station-20261026-0018-e01`
- **So what cho Vexere:** Chỉ dùng cho pre-trip guide; feedback cho đối tác
- **Phản biện:** Vexere không kiểm soát

## Thị trường

### F11 - Khách Hàn tự đặt vé tàu qua Klook, MyRealTrip và cả Vexere (3 bài Naver kể đặt qua app Vexere, 1 hướng dẫn trên Tistory); bàn rất kỹ chuyện giường tầng 1/2 và khoang 4 người
- **Nhóm khách:** Hàn Quốc · **Tin cậy:** trung bình · **Bằng chứng:** 20 evidence, 18 tác giả, 3 nguồn (naver_blog, tistory, youtube_kr)
- **Quote:**
  - "저는 vexere앱에서 예약했어요!" `naver_blog-20261027-0006-e01`
  - "클룩 같은 대행앱에서 기차예약을 하면 수수료도 있고, 좌석 선택도 자유롭지 않아요." `tistory-20261027-0002-e01`
  - "1등석을 탔는데도 몸이 거부하니까 다음에는 제일 낮은 자리 타야겠어." `youtube_kr-20261027-0006-e01`
- **So what cho Vexere:** Kéo booking Train theo quốc tịch Hàn để kiểm chứng; hướng dẫn đặt vé tiếng Hàn; cân nhắc affiliate blogger Naver
- **Phản biện:** 29 bài blog/vlog; blogger không đại diện toàn bộ khách

### F12 - Khách Ấn lo nhất chuyện đồ chay khi đi tàu VN và quen quy giá ra rupee; thảo luận công khai về tàu VN rất ít
- **Nhóm khách:** Ấn Độ · **Tin cậy:** thấp · **Bằng chứng:** 11 evidence, 8 tác giả, 2 nguồn (reddit_in, youtube_in)
- **Quote:**
  - "हमें सीधे वहां तो कुछ वेजिटेरियन मिलेगा नहीं।" `youtube_in-20261027-0001-e01`
  - "Stock a few ready-to-eat packs for train journeys." `reddit_in-20261027-0002-e03`
- **So what cho Vexere:** FAQ EN cho khách Ấn: đồ chay trên tàu/tại ga; cân nhắc INR trong currency switch
- **Phản biện:** Mỏng, chủ yếu creator · Chủ yếu vlog YouTube

### F13 - Khách Việt phàn nàn app/web DSVN: thanh toán rườm rà, tải vé lỗi, đặt nhầm ngày
- **Nhóm khách:** Việt Nam · **Tin cậy:** thấp · **Bằng chứng:** 18 evidence, 18 tác giả, 2 nguồn (appstore, gmaps_station)
- **Quote:**
  - "Hình thức thanh toán quá phức tạp, hãy đơn giản quy trình và đa dạng ngân hàng sao cho thuận tiện. Lằng nhằng quá, rất muốn bỏ cuộc" `appstore-20261026-0005-e01`
  - "lúc về check lại thì thấy nhầm ngày khởi hành sang 17/8" `gmaps_station-20261026-0226-e01`
- **So what cho Vexere:** Messaging 'đặt vé tàu không rườm rà'; so số bước thanh toán Vexere vs DSVN
- **Phản biện:** Chỉ 2 nguồn (app store, Maps)

## Đối thủ

### F14 - Trên trang bán vé, chỉ Baolau và Vexere claim rõ 'đại lý chính thức DSVN'; mọi đối thủ đều bán tàu tư nhân, trang tàu EN của Vexere thì chưa; Baolau có Alipay, Vexere chưa có ví châu Á
- **Nhóm khách:** Đối thủ (proxy) · **Tin cậy:** đo lường · **Bằng chứng:** 60 evidence, 7 tác giả, 1 nguồn (competitor_site)
- **Quote:**
  - "Baolau is an official ticket agent of Vietnam Railways since 2015 and works directly with the major private railway companies in Vietnam" `competitor_site-20261028-0004-e04`
  - "Vexere is an Official Partner of Vietnam Railways (VNR / DSVN)" `competitor_site-20261028-0010-e06`
- **So what cho Vexere:** Đưa tàu tư nhân lên trang EN cùng lúc onboard Chapa; cân nhắc Alipay/WeChat nếu theo khách Trung
- **Phản biện:** Claim trên trang, chưa kiểm chứng; snapshot 1 ngày

## Insider tips (I01) - dùng được ngay cho content, AEO, CS
| Tip | Evidence |
|---|---|
| Trả trên dsvn.vn bằng VNPay thì thẻ quốc tế chạy; thêm số 0 trước SĐT | `reddit-20261026-0020-e02`, `reddit-20261026-0020-e03` |
| Đặt trọn khoang 4 để không bị người ghế cứng chiếm giường | `reddit-20261026-0022-e01` |
| Giường tầng 1 - tầng 2 chạm trần (khách Hàn) | `tistory-20261027-0004-e01` |
| Tàu số thấp (SE1/SE2, SE3) mới hơn tàu số cao | `reddit-20261026-0002-e04`, `tripadvisor-20261026-0026-e05` |
| Tàu dài mở bán 60 ngày, tàu ngắn ~30 ngày; "hết vé" có thể là chưa mở | `muse_fb_radar-20261026-0003-e03`, `muse_fb_radar-20261026-0003-e02` |
| Huế - Đà Nẵng: Nam → Bắc ngồi bên phải để ngắm biển | `muse_fb_radar-20261026-0005-e02` |
| Lào Cai → Sa Pa: shuttle 55k/người, từ chối người chèo kéo, hoặc đặt xe trước | `reddit-20261026-0010-e04`, `muse_fb_radar-20261026-0017-e02` |
| Dùng Grab ở ga để tránh hét giá | `gmaps_station-20261026-0012-e02` |

## Ưu tiên hành động
| # | Việc | Insight | Tác động | Công sức | Đo bằng |
|---|---|---|---|---|---|
| 1 | Baseline + nội dung AEO nêu tên Vexere, ưu tiên ChatGPT | F02 | Cao | Thấp | Vexere x/30 lượt hằng tháng |
| 2 | Đưa tàu tư nhân lên trang EN cùng lúc onboard Chapa; mô tả thật (gắn đoàn tàu nào, cam kết đúng cabin) | F04, F14 | Cao | Trung bình | CVR trang tàu tư nhân, tỷ lệ khiếu nại đổi cabin |
| 3 | UI chọn khoang/giường + nhãn tàu mới/cũ (Q4) | F03 | Cao | Trung bình | CVR bước chọn chỗ, field abandonment (Clarity) |
| 4 | Kiểm ô SĐT quốc tế + thẻ quốc tế trong flow EN | F01 | Trung bình | Thấp | Drop-off bước nhập thông tin theo locale |
| 5 | Trạng thái "chưa mở bán - mở ngày X" | F06 | Trung bình | Thấp | Search không có kết quả → quay lại |
| 6 | Shuttle Lào Cai → Sa Pa đặt trước + pre-trip guide theo ga | F08, F09 | Trung bình | Trung bình | Attach rate add-on |
| 7 | Nội dung tiếng Hàn + kiểm booking khách Hàn | F11 | Trung bình | Thấp | Booking Train theo quốc tịch Hàn |

## Validate bằng data nội bộ (chưa làm)
| Insight | Cần kéo |
|---|---|
| F01 | Drop-off theo locale EN ở bước SĐT/thanh toán (GA4/Clarity); tỷ lệ thanh toán lỗi theo loại thẻ (Metabase) |
| F03 | Field-level abandonment ở bước chọn chỗ (Clarity) |
| F06 | Search tuyến không có chuyến trong cửa sổ 30-60 ngày (log, BI-2775) |
| F11 | Booking Train theo quốc tịch/ngôn ngữ app Hàn |
| F12, F13 (Trung) | Booking theo quốc tịch Ấn, Trung - quyết định có đầu tư thị trường hay không |

## Đã sửa / loại khi tổng hợp
- **Bỏ** nhận định "dsvn.vn hay lỗi thẻ quốc tế" (bản nháp D01): data thật chỉ có 1 evidence tiêu cực về thẻ và nó nói về Vexere; các evidence còn lại cho thấy dsvn.vn chạy được nếu chọn VNPay. Đã viết lại thành F01.
- **Bỏ** "khách Hàn né DSVN vì lỗi thẻ Hàn": chỉ có trong báo cáo của Muse, không có evidence.
- **Sửa** tàu tư nhân (D04 → F04): review sau chuyến (T-012) phân cực theo hãng, khác ý kiến forum trước chuyến.
- **Loại khỏi danh sách hành động**: phòng chờ nóng (D09), thái độ nhân viên ga (D10) - nhiều evidence nhưng ngoài tầm Vexere; giữ làm feedback đối tác.
- Khách Trung (D13): 3 bài, 3 tác giả - không đủ để kết luận; chỉ ghi nhận khoảng trống.

## Khoảng trống còn lại
- Khách Trung: Xiaohongshu, Mafengwo chặn đăng nhập → cần data nội bộ hoặc agent tour.
- Khách Việt (C10): ngoài scope v0.1.
- M05 mới 1 lần chạy/engine, dao động mạnh → chạy 2 lần/tháng từ tháng 11.
- TikTok chặn; YouTube Shorts thay thế ở đợt sau.
