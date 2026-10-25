# Taxonomy v0.1

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
| Thanh toán & giấy tờ | `payment_card` · `payment_currency` · `id_passport_name` |
| Hoàn/đổi | `refund_change` |
| Sản phẩm tàu | `class_cabin` · `train_type` · `private_train` · `cleanliness` · `toilet` · `food_onboard` · `noise_sleep` · `safety_security` · `luggage` · `punctuality_delay` · `scenery` · `staff_attitude` |
| Ga | `station_navigation` · `station_facilities` · `boarding_process` |
| Chặng cuối | `last_mile_transport` · `last_mile_shuttle` · `arrival_time` |
| Lộ trình | `route_missing` · `route_connection` · `schedule_info` |
| Trust | `trust_scam` · `trust_agent` · `customer_support` |
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

## entity - tên chuẩn (viết thường, snake_case)
- Kênh bán: `dsvn` · `twelve_go` · `baolau` · `trip_com` · `traveloka` · `klook` · `vexere` · `local_agent` · `hotel_desk` · `station_counter` · `vietnam_railway_agent_site`
- Tàu DSVN: theo mã tàu `se1`, `se3`, `sp3`... hoặc `dsvn_generic`
- Tàu du lịch tư nhân: `lotus` · `chapa_express` · `violette` · `sapaly` · `livitrans` · `orient_express` · `hai_van_heritage`
- Thay thế: `flight` · `sleeper_bus` · `limousine` · `private_car`

## route - mã IATA-like của ga
`HAN` Hà Nội · `SGN` Sài Gòn · `HUE` Huế · `DAD` Đà Nẵng · `NHA` Nha Trang · `LCA` Lào Cai · `HPH` Hải Phòng · `DTH` Đồng Hới · `QNH` Quy Nhơn · `NBH` Ninh Bình · `PTH` Phan Thiết · `DLT` Đà Lạt
Dạng `HAN-LCA`. Thêm ga mới → đề xuất.
