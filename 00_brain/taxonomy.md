# Taxonomy v0.7

Muse chỉ dùng mã ở đây. Thiếu mã → `other` + `topic_suggest`. Claude gom đề xuất, nâng version.

## type - loại evidence
| Mã | Nghĩa |
|---|---|
| `need` | Nhu cầu, mong muốn |
| `pain` | Trải nghiệm tệ đã xảy ra |
| `barrier` | Thứ làm chần chừ/bỏ ngang trước khi mua |
| `question` | Câu hỏi thật trước chuyến (rất giá trị cho AEO) |
| `tip` | Mẹo/kinh nghiệm chủ động chia sẻ |
| `workaround` | Cách lách khi hệ thống không đáp ứng |
| `comparison` | So sánh kênh/tàu/phương tiện |
| `praise` | Khen |
| `signal` | Tin thị trường, chính sách, giá |

## stage - journey
`inspire` · `plan` · `compare` · `book` · `pre_trip` · `station` · `onboard` · `last_mile` · `post_trip` · `na`

## topic
| Nhóm | Mã |
|---|---|
| Giá & phí | `price_level` · `price_fee_hidden` · `price_vs_flight_bus` · `price_dynamic_tet` |
| Đặt vé | `booking_channel` · `booking_ux` · `booking_availability` · `booking_window` · `eticket_delivery` · `seat_selection` |
| Thanh toán & giấy tờ | `payment_card` · `payment_wallet` (Alipay, WeChat Pay, UPI, Kakao/Naver Pay...) · `payment_currency` · `id_passport_name` |
| Hoàn/đổi | `refund_change` |
| Sản phẩm tàu | `class_cabin` · `train_type` · `private_train` · `cleanliness` · `toilet` · `food_onboard` · `noise_sleep` · `safety_security` · `luggage` · `punctuality_delay` · `scenery` · `staff_attitude` · `power_outlet` · `air_conditioning` · `accessibility` · `food_dietary` (chay, halal, kiêng) |
| Ga | `station_navigation` · `station_facilities` · `boarding_process` · `station_history` (kiến trúc, di sản, lịch sử ga) · `touting` (chèo kéo: taxi, xe ôm, bán hàng, xe đẩy hành lý) |
| Chặng cuối | `last_mile_transport` · `last_mile_shuttle` · `arrival_time` |
| Lộ trình | `route_missing` · `route_connection` · `schedule_info` |
| Trust | `trust_scam` · `trust_agent` · `customer_support` |
| Tiện ích | `wifi` (wifi ở ga hoặc trên tàu) |
| Ngôn ngữ | `language_barrier` (biển báo, nhân viên, app/web không có ngôn ngữ của khách) |
| Chọn phương tiện | `mode_choice` (chọn tàu hay xe/bay/limousine vì lý do không phải giá: thời gian, say xe, thoải mái, ngắm cảnh, an toàn đi đêm) |
| Liên vận | `cross_border_train` (tàu liên vận Việt - Trung: Gia Lâm/Đồng Đăng - Nam Ninh, Lào Cai - Hà Khẩu) |
| Tổng quát | `overall_experience` (đánh giá chung, không nêu vấn đề cụ thể - giá trị thấp, chỉ dùng khi không tách được ý cụ thể hơn) |
| Khác | `other` |

## segment
| Mã | Nghĩa |
|---|---|
| `intl_backpacker` | Khách nước ngoài đi một mình/bạn bè, budget |
| `intl_couple` | Cặp đôi |
| `intl_family` | Gia đình có trẻ em |
| `intl_senior` | Người lớn tuổi |
| `intl_group_tour` | Đoàn, qua tour |
| `intl_unknown` | Nước ngoài, không rõ nhóm |
| `expat` | Người nước ngoài sống ở VN |
| `vn_domestic` | Khách Việt |
| `unknown` | Không xác định được - **dùng khi không chắc** |

## topic → câu hỏi mặc định
Script tính độ phủ tự gán thêm các câu hỏi dưới đây theo topic, cộng với `questions` Muse đã gán. Muse vẫn gán `questions` đầy đủ theo nội dung.

| Topic | Câu hỏi |
|---|---|
| `price_vs_flight_bus` · `mode_choice` | C02 |
| `booking_channel` | C03 M01 |
| `trust_scam` · `trust_agent` · `price_fee_hidden` | C05 |
| `class_cabin` · `seat_selection` · `train_type` | C06 |
| `last_mile_transport` · `last_mile_shuttle` · `arrival_time` | C07 |
| `route_missing` · `route_connection` | C08 |
| `payment_card` · `payment_wallet` · `payment_currency` · `id_passport_name` | C09 |
| `language_barrier` · `food_dietary` | C12 |
| `private_train` | M04 |
| `scenery` | I03 |
| type `tip` · `workaround` (theo loại evidence, không theo topic) | I01 |
| `touting` | C05 C07 |

## market - thị trường khách (khác `segment`)
`segment` = đi với ai, kiểu chuyến. `market` = khách đến từ thị trường nào. Hai chiều độc lập, evidence ghi cả hai.

| Mã | Nghĩa |
|---|---|
| `in` | Ấn Độ |
| `cn` | Trung Quốc đại lục |
| `tw_hk` | Đài Loan, Hồng Kông, Macau - **tách khỏi `cn`** dù cùng viết tiếng Trung |
| `kr` | Hàn Quốc |
| `western` | Âu, Mỹ, Úc, NZ, Canada |
| `other_asia` | Châu Á khác (Nhật, ASEAN...) |
| `vn` | Việt Nam |
| `expat` | Người nước ngoài sống ở VN |
| `intl` | Khách nước ngoài, chưa rõ nước nào |
| `unknown` | Không xác định - **mặc định** |

Quy tắc xác định (theo thứ tự, không đạt thì `unknown`):
1. Tác giả tự nói ("as an Indian", "我们从广州来", "한국에서").
2. Nền tảng + ngôn ngữ bản địa của thị trường: Xiaohongshu/Mafengwo/Douyin + chữ giản thể → `cn`; chữ phồn thể → `tw_hk`; Naver/Tistory + tiếng Hàn → `kr`; tiếng Hindi → `in`.
3. **Không suy từ tên người, ảnh đại diện, hay tiếng Anh có giọng.** Reddit/TripAdvisor tiếng Anh mà không tự nói → `unknown`.

## origin - nguồn gốc khách do script suy luận (lớp riêng, không ghi đè `market`)
`market` = khách tự nói hoặc nền tảng bản địa, Muse gán. `origin` = script `tools/dashboard_data.py` tự tính theo thứ tự dưới đây, mỗi evidence lấy quy tắc đầu tiên khớp.

| # | Quy tắc | origin | Tin cậy |
|---|---|---|---|
| 1 | `market` khác `unknown` (khách tự nói / nền tảng bản địa) | theo `market` | cao |
| 2 | `segment` = `vn_domestic` / `expat` / `intl_*` (khách tự nói) | `vn` / `expat` / `intl` | cao |
| 3 | `origin_hint` + `origin_cue` bắt đầu bằng `profile:` (quê ghi trên profile, vd TripAdvisor) | theo `origin_hint` | cao |
| 4 | `lang` = `vi` | `vn` | cao |
| 5 | `lang` = `ko` / `zh-Hans` / `zh-Hant` / `hi` / `ja` | `kr` / `cn` / `tw_hk` / `in` / `other_asia` | cao |
| 6 | `origin_hint` + `origin_cue` là dấu hiệu nội dung ("first time in Vietnam", "flight home") | theo `origin_hint` | trung bình |
| 7 | `author_role: op` trên `tripadvisor_forum`, hoặc bài trên r/travel, r/solotravel, r/backpacking | `intl` | trung bình |
| 8 | Còn lại (comment tiếng Anh trên r/VietNam, review tiếng Anh trên Maps...) | `unknown` | - |

Dùng:
- Insight cho **một thị trường cụ thể** (Ấn, Trung, Hàn, Việt...): chỉ dùng origin tin cậy **cao**.
- Insight "khách nước ngoài nói chung": được cộng tin cậy trung bình, ghi rõ trong mục Phản biện.
- Quy tắc 4 (tiếng Việt → người Việt): spot-check 30/30 đúng (2026-10-27, mẫu T-003/T-004). Quy tắc 7: rà 26/26 dòng OP TripAdvisor không tự nhận (2026-10-27), sai ước ~4-8%, giữ tin cậy trung bình. Sai >10% → hạ xuống trung bình.

## entity - tên chuẩn (viết thường, snake_case)
- Kênh bán: `dsvn` · `vetau` (vetau.com.vn + app Vé Tàu) · `twelve_go` (**không** viết `12go`) · `baolau` · `bookaway` · `vietage` · `trip_com` · `traveloka` · `klook` · `getyourguide` · `ivivu` · `vexere` · `local_agent` (đại lý địa phương có tên như Sapa Nomad cũng ghi mã này) · `hotel_desk` · `station_counter` · `vietnam_railway_agent_site`
- Tàu DSVN: theo mã tàu `se1`, `se3`, `sp3`... hoặc `dsvn_generic`
- Tàu du lịch tư nhân (**dùng đúng mã ngắn**: `lotus` không phải `lotus_train`, `violette` không phải `violette_train`, `sapaly` không phải `sapaly_express`): `lotus` · `chapa_express` · `violette` · `sapaly` · `king_express` · `victoria_express` · `et_pumpkin` · `vicsapa` · `sjourney` · `fanxipan_express` · `livitrans` · `orient_express` · `hai_van_heritage` · `laman_express` (Laman/Lamen/LAMAN) · `hana_train` · `charmy_express` · `damitrans` · `the_hanoi_train` (Tàu Hà Nội 5 Cửa Ô)
- Kênh theo thị trường: `fliggy` · `qunar` · `makemytrip` · `cleartrip` · `myrealtrip` · `kkday` (Ctrip trong nước TQ ghi `trip_com`)
- Thanh toán: `alipay` · `wechat_pay` · `upi` · `kakao_pay` · `naver_pay` · `vnpay` · `momo` · `viettel_money` · `apple_pay`
- `vietage` = The Vietage by Anantara (vừa là tàu, vừa tự bán vé)
- Thay thế: `flight` · `sleeper_bus` · `limousine` · `private_car`

## route - mã IATA-like của ga
`HAN` Hà Nội · `SGN` Sài Gòn · `HUE` Huế · `DAD` Đà Nẵng · `NHA` Nha Trang · `LCA` Lào Cai · `HPH` Hải Phòng · `DTH` Đồng Hới · `QNH` Quy Nhơn · `NBH` Ninh Bình · `PTH` Phan Thiết · `DLT` Đà Lạt · `GLA` Gia Lâm · `DDG` Đồng Đăng · `NNG` Nam Ninh (TQ) · `HKO` Hà Khẩu (TQ) · `TCH` Tháp Chàm (Phan Rang) · `DTI` Diêu Trì · `TLO` Thọ Lộc · `QNG` Quảng Ngãi
Dạng `HAN-LCA`. Thêm ga mới → đề xuất.

## Changelog
- v0.7 (2026-10-28, sau review T-009..T-012): thêm entity kênh `vetau`, `getyourguide`, `ivivu`; ví `momo`, `viettel_money`; tàu tư nhân `king_express`, `victoria_express`, `et_pumpkin`, `vicsapa`, `sjourney`, `fanxipan_express` (gặp ở T-009 SERP, T-010, T-011); ghi rõ mã sai hay gặp (`12go`, `lotus_train`, `violette_train`, `sapaly_express`); đại lý địa phương có tên → `local_agent`; ga `QNG` (T-008). Không nhận `route_distance` (T-011) - thông tin tĩnh, không phục vụ câu hỏi nào. Có `tools/validate_evidence.py` để Muse tự kiểm trước khi nộp.
- v0.6 (2026-10-27): thêm lớp `origin` do script suy luận (ngôn ngữ, profile, nguồn, dấu hiệu nội dung); market thêm `expat`, `intl`; field mới cho Muse `origin_hint`, `origin_cue`, `author_role`.
- v0.5 (2026-10-27, sau review T-002): thêm topic `mode_choice` (đề xuất `mode_choice_train_vs_bus` của Muse ở T-002 raw 0005; cùng ý lặp ở T-002 0007/0017 và T-005 0014: tàu vs limousine/xe khách/xe riêng theo tiêu chí không phải giá), map → C02.
- v0.4 (2026-10-26, sau review T-003/T-004/T-005): thêm topic `station_history` (16 dòng other ở T-003), `touting` (chèo kéo, gộp vendor_touting/vendor_conflict + taxi chèo kéo ở Huế/Đà Nẵng/Nha Trang), `wifi` (gộp wifi_onboard/station_wifi, 3 dòng), `overall_experience` (3 dòng qua T-001/T-003/T-004); map `touting` → C05 C07; entity `laman_express`, `hana_train`, `charmy_express`, `damitrans`, `the_hanoi_train`, `bookaway`, `vietage`; ga `DTI`, `TLO`. Không cần sửa lại dòng `other` cũ - Muse dùng mã mới từ task kế tiếp.
- v0.3 (2026-10-26, sau review T-001): thêm bảng topic → câu hỏi mặc định vì pilot cho thấy `questions` chỉ bám danh sách câu của task (vd `class_cabin` không map C06, `scenery` không map I03).
- v0.2 (2026-10-26): thêm chiều `market` (Ấn, Trung, Đài/Hồng Kông, Hàn...); topic `payment_wallet`, `food_dietary`, `language_barrier`, `cross_border_train`; nhận đề xuất của Muse từ T-001: `power_outlet`, `air_conditioning`, `accessibility`; entity kênh/thanh toán theo thị trường; ga liên vận.
