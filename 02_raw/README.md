# Raw - chuẩn file

Path: `02_raw/<source>/<YYYY-MM>/<raw_id>.md` (YYYY-MM = tháng crawl)
`raw_id`: `<source>-<YYYYMMDD>-<nnnn>`, ví dụ `reddit-20261025-0001`

Bất biến: đã tạo thì không sửa, không xoá.

```markdown
---
raw_id: tripadvisor-20261027-0001
source: tripadvisor_forum
url: https://...                # bắt buộc, để kiểm chứng toàn văn
title: "..."                    # tiêu đề thread (ngắn, giữ nguyên)
posted_at: 2025-11-03
date_precision: thread          # comment | thread | estimated
crawled_at: 2026-10-27
lang: en
raw_mode: excerpt
engagement: {score: null, comments: 17}
task_id: T-002
---

[c:3f9a1c2b7e] role: op | location: Sydney, Australia | date: 2025-11-03
> "đoạn trích nguyên văn ≤50 từ"
> "đoạn trích nguyên văn khác của cùng bài, tổng ≤50 từ cho bài này"

[c:8f2a5c54ae] role: reply | date: 2025-11-04
> "đoạn trích nguyên văn ≤50 từ"

Note: <ghi chú của Muse nếu cần - không bao giờ dùng làm quote>
```

Quy tắc:
- **Mỗi bài đăng (post/comment/review) trích tối đa 50 từ**, cộng dồn mọi đoạn của bài đó (tiếng Trung/Nhật/Hàn: 100 ký tự). Chỉ trích đoạn dùng làm evidence; bài không dùng thì không ghi.
- Ngoại lệ nội dung dài (Luan duyệt 2026-10-28): transcript video tối đa 5 đoạn, trang hướng dẫn dài (seat61) tối đa 10 đoạn/trang; mỗi đoạn ≤50 từ (CJK ≤100 ký tự). Comment dưới video vẫn theo mức 50 từ/comment.
- Đoạn trích là **nguyên văn** trong ngoặc kép, được cắt giữa câu bằng `[...]`. Không viết lại, không tóm tắt, không dịch.
- Dòng header mỗi bài: `role` (op/reply/review), `location` nếu trang có hiện, `date` nếu có. Tên người không ghi; tên được tag trong nội dung → `[name]`.
- Evidence `quote` phải là chuỗi con của một đoạn trích trong raw.
- Toàn văn để kiểm chứng: mở `url`. Claude spot-check bằng cách đối chiếu với trang gốc.
- Raw tạo trước 2026-10-27 (T-001, T-003, T-004, T-005) đã được cắt về dạng trích đoạn ngày 2026-10-27, Luan duyệt. T-002 đang được Muse đọc lại theo chuẩn mới.
