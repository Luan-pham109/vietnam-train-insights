# Vietnam Train Insights

Kho insight ngành tàu hoả Việt Nam, tổng hợp từ nguồn bên ngoài. Phục vụ quyết định marketing/product cho Train tại Vexere.

## Trả lời 3 nhóm câu hỏi
1. **Khách hàng**: ai, cần gì, cản trở gì, trigger gì - theo segment và journey stage
2. **Cạnh tranh**: ai đang giữ khách, mạnh/yếu ở đâu (proxy, không phải thị phần thật)
3. **Insider**: tip, workaround, điều chỉ người đi thật mới biết

## Vai trò
| Agent | Vai trò | Ghi vào |
|---|---|---|
| **Muse** | Researcher + social listening: thu thập, extract evidence | `02_raw/`, `03_evidence/`, trạng thái task trong `01_tasks/` |
| **Claude** | Điều phối + bộ não: câu hỏi, taxonomy, giao task, kiểm tra, mapping, synthesis | `00_brain/`, `01_tasks/`, `04_insights/`, `05_outputs/`, `06_validation/` |
| **Luan** | Owner: chốt ưu tiên, duyệt insight, validate bằng data nội bộ | mọi nơi |

Quy tắc chi tiết: [AGENTS.md](AGENTS.md)

## Luồng
```
00_brain/questions  ->  01_tasks (Claude giao)  ->  02_raw (Muse thu)  ->  03_evidence (Muse extract)
      ^                                                                         |
      |                                                                         v
06_validation (data nội bộ)  <-  05_outputs (artifact)  <-  04_insights (Claude synthesis + review)
```

## Cấu trúc
| Folder | Nội dung |
|---|---|
| `00_brain/` | Question bank, taxonomy, source map, rule confidence - nguồn sự thật về cách phân loại |
| `01_tasks/` | Research brief Claude giao Muse, mỗi task 1 file |
| `02_raw/` | Nội dung gốc, bất biến, `02_raw/<source>/<YYYY-MM>/<raw_id>.md` |
| `03_evidence/` | Evidence unit dạng JSONL, `03_evidence/<YYYY-MM>/<task_id>.jsonl` |
| `04_insights/` | Insight card, mỗi card 1 file `INS-xxx.md` |
| `05_outputs/` | Artifact tổng hợp: journey pain map, competitor matrix, insider tips, signal log |
| `06_validation/` | Đối chiếu insight với data nội bộ (Metabase, GA4, Clarity, CS chat) |

## Scope v0.1
- Ưu tiên **khách nước ngoài** trước (>30% khách Train, nguồn EN dễ thu, gắn với roadmap Q4: UI/UX khách Tây, chặng cuối, tàu du lịch tư nhân, AEO)
- Khách Việt: chỉ thu signal thị trường + nguồn Muse radar FB group đang có
