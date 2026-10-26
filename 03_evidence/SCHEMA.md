# Evidence unit - schema v0.3

v0.3: `date_precision` thêm giá trị `estimated` (ngày suy từ mốc tương đối "3 tháng trước" hoặc ngày-tháng không có năm). Ngày suy ra neo theo ngày crawl, lấy mốc gần nhất trước ngày crawl.

v0.2: thêm field bắt buộc `market`. Evidence nộp trước v0.2 thiếu `market` được coi là `unknown`.

Path: `03_evidence/<YYYY-MM>/<task_id>.jsonl`, mỗi dòng 1 evidence.
1 raw có thể tách ra nhiều evidence: mỗi ý riêng biệt (1 pain, 1 tip...) là 1 dòng.

| Field | Bắt buộc | Kiểu | Ghi chú |
|---|---|---|---|
| `ev_id` | ✓ | string | `<raw_id>-e<nn>` |
| `raw_id` | ✓ | string | Phải tồn tại trong `02_raw/` |
| `task_id` | ✓ | string | |
| `quote` | ✓ | string | **Nguyên văn** từ raw, ≤400 ký tự, giữ ngôn ngữ gốc (中文, 한국어, हिन्दी...) - không dịch |
| `summary_vi` | ✓ | string | 1 câu tiếng Việt |
| `type` | ✓ | enum | taxonomy.type |
| `stage` | ✓ | enum | taxonomy.stage |
| `topics` | ✓ | string[] | 1-3 mã taxonomy.topic |
| `topic_suggest` | | string | Khi có `other` |
| `segment` | ✓ | enum | Không chắc → `unknown` |
| `market` | ✓ | enum | taxonomy.market, theo quy tắc xác định. Không chắc → `unknown` |
| `entities` | | string[] | taxonomy.entity |
| `routes` | | string[] | `HAN-LCA` |
| `sentiment` | ✓ | int | -1 / 0 / 1 |
| `questions` | ✓ | string[] | Mã trong questions.md |
| `author_hash` | ✓ | string | |
| `posted_at` | ✓ | date | |
| `date_precision` | | enum | `comment` / `thread` (ngày bài gốc chứ không phải ngày comment) / `estimated` (ngày suy từ mốc tương đối hoặc thiếu năm) |
| `lang` | ✓ | string | |
| `review` | | enum | Claude ghi: `ok` / `wrong_tag` / `quote_mismatch` / `irrelevant` |

Ví dụ:
```json
{"ev_id":"reddit-20261025-0001-e01","raw_id":"reddit-20261025-0001","task_id":"T-001","quote":"dsvn.vn kept rejecting my Revolut card so I ended up paying 12Go almost 30% more","summary_vi":"Thẻ quốc tế bị DSVN từ chối, phải sang 12Go chịu giá cao hơn ~30%","type":"workaround","stage":"book","topics":["payment_card","price_fee_hidden"],"segment":"intl_backpacker","market":"unknown","entities":["dsvn","twelve_go"],"routes":["HAN-DAD"],"sentiment":-1,"questions":["C09","M02"],"author_hash":"3f9a1c2b7e","posted_at":"2025-11-03","lang":"en"}
```
