# Source map v0.7

| Mã nguồn | Nguồn | Segment | Câu hỏi chính | Tần suất | Wave |
|---|---|---|---|---|---|
| `reddit` | r/VietNam, r/travel, r/solotravel, r/backpacking, r/VietnamTravel | intl | C03 C04 C05 C06 M01 M02 I01 | Weekly | 1 |
| `tripadvisor_forum` | TripAdvisor Vietnam forum (train threads) | intl | C03 C04 C07 M01 I01 | Weekly | 1 |
| `tripadvisor_review` | Review tàu du lịch tư nhân | intl | C06 M04 I02 | Monthly | 1 |
| `gmaps_station` | Google Maps review ga HAN, SGN, HUE, DAD, NHA, LCA, DTH | intl + vn | C04 C07 I02 | Monthly | 1 |
| `appstore` | App Store + Google Play: DSVN, 12Go, Baolau, Trip.com, Traveloka, Vexere (review nhắc tàu) | intl + vn | C04 C05 C09 M02 | Monthly | 1 |
| `muse_fb_radar` | FB group Muse radar đang thu | intl + vn | C03 C04 C07 I01 | Liên tục | 1 |
| `youtube` | Vlog tàu VN: transcript + comment | intl | C02 C06 I02 I03 | Monthly | 2 |
| `tiktok` | Video review tàu/khoang (chặn đăng nhập, xem dưới) | intl + vn | C02 C06 I02 | Quarterly (thử lại) | 2 |
| `seat61` | seat61.com trang Vietnam | intl | M01 C03 | Quarterly (snapshot) | 2 |
| `serp_ai` | Google SERP + ChatGPT/Perplexity/Gemini với bộ prompt cố định | intl | M05 M01 | Monthly | 2 |
| `competitor_site` | Trang tàu VN của 12Go, Baolau, Trip.com, Klook, Traveloka | - | M02 M03 | Monthly | 2 |
| `ad_library` | Meta Ad Library, Google Ads Transparency | - | M03 | Monthly | 3 |
| `news` | VnExpress, Tuổi Trẻ, Thanh Niên, VnExpress International, dsvn.vn | vn | M06 C10 | Weekly | 3 |
| `forum_vn` | VOZ, Tinhte | vn | C10 | Monthly | 3 |
| `quora` | Quora (câu hỏi về tàu VN) | in | C11 C12 M07 I01 | Monthly | M |
| `reddit_in` | r/india, r/IndiaTravel, r/indiasocial, r/india_tourism | in | C11 C12 M07 | Monthly | M |
| `youtube_in` | Vlog Ấn Độ (Hindi/English) về tàu VN: transcript + comment | in | C02 C11 I02 | Monthly | M |
| `xiaohongshu` | 小红书 - 越南火车/越南卧铺/河内到沙巴 | cn | C11 C12 M07 I01 | Monthly | M |
| `mafengwo` | 马蜂窝 - du ký + Q&A tàu VN | cn | C11 I01 I02 | Monthly | M |
| `trip_com_cn` | Review/Q&A tiếng Trung trên Ctrip | cn | M02 M07 | Monthly | M |
| `naver_blog` | Naver Blog/Cafe - 베트남 기차/침대기차/사파 기차 | kr | C11 C12 M07 I01 | Monthly | M |
| `tistory` | Tistory blog tiếng Hàn | kr | C11 I02 | Monthly | M |
| `youtube_kr` | Vlog Hàn về tàu VN | kr | C02 C11 I02 | Monthly | M |

## Ghi chú độ lệch nguồn (bắt buộc đọc khi synthesis)
- `reddit`, `tripadvisor`: lệch về khách phương Tây, nói tiếng Anh, chủ động lên kế hoạch → over-represent ở `plan`/`book`.
- `gmaps_station`, `appstore`: lệch về phàn nàn.
- `seat61`, `serp_ai`: ít mẫu nhưng **định hình nhận thức** → đánh giá theo ảnh hưởng, không đếm số lượng.
- Wave M (thị trường): bù blind spot Ấn/Trung/Hàn của wave 1. Nền tảng CN/KR cần đăng nhập + chống bot mạnh → **thử truy cập trước, thu sau**. Không lấy được thì báo, không lách bằng tài khoản.
- Nguồn tiếng Trung lẫn khách Đài/Hồng Kông → tách `tw_hk`.
- Khách Hàn chủ yếu đi Đà Nẵng/Nha Trang/Phú Quốc bằng máy bay → volume nội dung về tàu có thể thấp. Ít evidence cũng là một phát hiện, cần ghi nhận chứ không ép số lượng.

## Trạng thái truy cập (cập nhật sau review)
- `gmaps_station` (T-003, 2026-10-26): cần đăng nhập Google để xem >5 review và sắp xếp newest-first. Trần trong phạm vi 2 năm: Sài Gòn 26, Lào Cai 8, Đồng Hới 27, Huế 41, Đà Nẵng 41. Re-crawl theo quý để lấy review mới tích luỹ. Ngày chỉ có dạng tương đối → `date_precision: estimated`. Loại review gửi hàng hoá (ngoài scope).
- `appstore` (T-004, 2026-10-26): App Store web chỉ có trang đầu 10 review/storefront, không phân trang. **Baolau: không có app, website-only** - kiểm lại theo quý. Vexere, Traveloka: 0 review nhắc tàu trong tập mới nhất đã xem. Review tàu của 12Go/Trip.com/Klook chủ yếu về tàu nước khác.
- `tripadvisor_forum` (T-002, 2026-10-27): đọc được không đăng nhập, không captcha (có lúc hiện DataDome Device Check rồi tự qua). Thread cũ chỉ hiện "1 year ago" → ngày suy từ forum search, có thể gán sai tác giả/ngày; tác giả + ngày trên trang thread thắng. Đợt sau mở rộng forum Da Nang, Ninh Binh, Quy Nhon, Nha Trang (thread tàu di sản Đà Nẵng - Huế k14919975 là thread chi tiết nhất về HD1/HD2/HD3).
- `muse_fb_radar` (T-005, 2026-10-26): 3 nhóm riêng tư (Vietnam is Awesome, Another Side of Vietnam, Hanoi Massive) chưa tìm. Reply FB có tag tên thật → phải thay bằng `[name]` khi đưa vào raw.
- `quora` (T-006, 2026-10-27): **không truy cập được** - tìm kiếm và đáp án dài bị tường đăng nhập; 4 đáp án đọc được đều trước 2025. Bỏ khỏi nguồn chủ động.
- `reddit_in` (T-006): đọc được không đăng nhập; bài về tàu VN rất hiếm (2 bài dùng được qua 4 sub).
- `youtube_in` (T-006): đọc được trang, mô tả, comment, transcript không đăng nhập.
- `xiaohongshu` (T-007, 2026-10-27): **không truy cập được** - tường đăng nhập QR/số điện thoại. Kiểm lại theo quý.
- `mafengwo` (T-007): **không truy cập được** - note đầy đủ và Q&A đẩy về đăng nhập/trang chủ.
- `trip_com_cn` (T-007): đọc được không đăng nhập; tìm kiếm nội bộ kém, phải dùng web search giới hạn site; có lúc gặp captcha. Đợt sau thử mục review ga.
- `naver_blog`, `tistory`, `youtube_kr` (T-008, 2026-10-27): đọc đầy đủ không đăng nhập. Naver Cafe chỉ lấy bài công khai.
- Kết luận wave M: Hàn thu tốt (29 bài), Ấn mỏng (11 bài, chủ yếu vlog), Trung gần như không thu được qua web công khai (3 bài).
- `serp_ai` (T-009, 2026-10-27): ChatGPT dùng được không đăng nhập; **Perplexity không truy cập được** (tường đăng nhập trước khi hiện đáp án) - kiểm lại theo tháng; Gemini dùng được sau khi đăng xuất (phải chạy phiên đăng xuất); Google SERP + AI Overview dùng được nhưng IP ra Mỹ (California) dù giao diện tiếng Việt - baseline là góc nhìn truy cập từ Mỹ, không phải từ VN. Chạy lại bộ 10 prompt cố định hằng tháng. Đáp án AI không lặp lại được → raw phải chứa trích đoạn nêu đủ mọi kênh được xếp hạng.
- `youtube` EN (T-010, 2026-10-27): đọc được transcript + comment không đăng nhập. Ngày comment dạng tương đối → `estimated`. Loại video có nhãn AD/HOSTED và kênh của hãng/đại lý (SJourney, Lotus Train, New Livitrans, Travel Agent Hanoi).
- `seat61` (T-011, 2026-10-28): toàn bộ nội dung tàu VN nằm trong 1 trang `Vietnam.htm` (cập nhật 2026-06-10). Snapshot theo quý, so ngày cập nhật trên trang. Link đặt vé mang tham số affiliate (Baolau, 12Go, cổng seat61) nhưng trang không ghi công bố hoa hồng cho vé tàu.
- `tripadvisor_review` (T-012, 2026-10-27): 7/7 trang hãng đọc được. Tàu di sản Huế - Đà Nẵng không có trang hãng riêng. Sapaly (9) và Livitrans (5) có ít review từ 2025 → re-crawl theo quý. Chapa Express có 2 trang trùng tên - dùng trang 219 review.
- `competitor_site` (T-013, 2026-10-28): 12Go, Baolau, Klook, Bookaway, vietnam-railway.com, Trip.com (trang kết quả `businessType=vn_train`), Vexere (`vexere.com/vn/trains.en`; `/en/trains` 404) đọc được không đăng nhập. **Traveloka desktop không xem được** (báo chỉ hỗ trợ mobile web) - thử mobile web lần sau. Phí và chính sách hoàn/đổi phần lớn chỉ hiện ở checkout. Phải tìm bằng tìm kiếm nội bộ của trang, không chỉ đoán URL. Chạy lại hằng tháng, giữ Vexere làm mốc.
- `tiktok` (T-014, 2026-10-28): **không truy cập được** - tìm kiếm EN/VI bật tường đăng nhập, không có video/caption/comment. Kiểm lại theo quý; góc video ngắn tạm lấy từ YouTube Shorts.
- `ad_library` (T-015, 2026-10-29): Meta Ad Library đọc được không đăng nhập; tìm theo tên ngắn rất nhiễu (12Go, Trip.com ra hàng chục nghìn kết quả) - phải lọc theo trang + từ khoá. **Google Ads Transparency Center bị chặn** (trang unusual-traffic + reCAPTCHA) - thử lại đợt sau. Baolau, vietnam-railway.com, Livitrans không có trang nhà quảng cáo trên Meta. Hãng tàu tư nhân ít tự chạy ad, chủ yếu được nhắc qua Klook/đại lý tour. Ad là phía cung: không tính share of voice, không suy nguồn gốc khách.
- `tripadvisor_forum` lượt 2 (T-017, 2026-10-30): forum Đà Nẵng/Ninh Bình/Quy Nhơn/Nha Trang chỉ ra 6 thread ngày hợp lệ (nhiều thread 2025 chỉ hiện "1 year ago"). **Hẹn ngày theo k-number** (Claude duyệt 2026-10-31): thread chỉ hiện "1 year ago" được nhận nếu k-number lớn hơn k-number của một thread mốc có ngày bài gốc chính xác ≥2025-01-01 (thread mốc đã thu hoặc mở được). Khi đó `posted_at` = ngày thread mốc, `date_precision: estimated`, `Note:` ghi k-number + ngày của thread mốc. Không dùng ngày reply sớm nhất làm cận dưới (đó là cận trên của bài gốc). Nha Trang: ít thread tàu mới, quét lại theo quý.
- `news` (T-018, 2026-10-30): VnExpress, Tuổi Trẻ, Thanh Niên đọc được (VnExpress search trực tiếp có lúc 406, vào qua trang chủ). **dsvn.vn lỗi truy cập** (privacy error) - thử lại đợt sau. VnExpress International ít bài DSVN - kiểm theo quý. `author_hash` theo báo (publisher), không theo phóng viên. Lượt sau chỉ thu bài từ ngày bài mới nhất của T-018 (2026-10-12).
