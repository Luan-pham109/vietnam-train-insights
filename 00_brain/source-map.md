# Source map v0.1

| Mã nguồn | Nguồn | Segment | Câu hỏi chính | Tần suất | Wave |
|---|---|---|---|---|---|
| `reddit` | r/VietNam, r/travel, r/solotravel, r/backpacking, r/VietnamTravel | intl | C03 C04 C05 C06 M01 M02 I01 | Weekly | 1 |
| `tripadvisor_forum` | TripAdvisor Vietnam forum (train threads) | intl | C03 C04 C07 M01 I01 | Weekly | 1 |
| `tripadvisor_review` | Review tàu du lịch tư nhân | intl | C06 M04 I02 | Monthly | 1 |
| `gmaps_station` | Google Maps review ga HAN, SGN, HUE, DAD, NHA, LCA, DTH | intl + vn | C04 C07 I02 | Monthly | 1 |
| `appstore` | App Store + Google Play: DSVN, 12Go, Baolau, Trip.com, Traveloka, Vexere (review nhắc tàu) | intl + vn | C04 C05 C09 M02 | Monthly | 1 |
| `muse_fb_radar` | FB group Muse radar đang thu | intl + vn | C03 C04 C07 I01 | Liên tục | 1 |
| `youtube` | Vlog tàu VN: transcript + comment | intl | C02 C06 I02 I03 | Monthly | 2 |
| `tiktok` | Video review tàu/khoang | intl + vn | C02 C06 I02 | Monthly | 2 |
| `seat61` | seat61.com trang Vietnam | intl | M01 C03 | Quarterly (snapshot) | 2 |
| `serp_ai` | Google SERP + ChatGPT/Perplexity/Gemini với bộ prompt cố định | intl | M05 M01 | Monthly | 2 |
| `competitor_site` | Trang tàu VN của 12Go, Baolau, Trip.com, Klook, Traveloka | - | M02 M03 | Monthly | 2 |
| `ad_library` | Meta Ad Library, Google Ads Transparency | - | M03 | Monthly | 3 |
| `news` | VnExpress, Tuổi Trẻ, Thanh Niên, VnExpress International, dsvn.vn | vn | M06 C10 | Weekly | 3 |
| `forum_vn` | VOZ, Tinhte | vn | C10 | Monthly | 3 |
| `quora` | Quora (câu hỏi về tàu VN) | in | C11 C12 M07 I01 | Monthly | M |
| `reddit_in` | r/india, r/IndiaTravel, r/indiasocial | in | C11 C12 M07 | Monthly | M |
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
