# Raw - chuẩn file

Path: `02_raw/<source>/<YYYY-MM>/<raw_id>.md` (YYYY-MM = tháng crawl)
`raw_id`: `<source>-<YYYYMMDD>-<nnnn>`, ví dụ `reddit-20261025-0001`

Bất biến: đã tạo thì không sửa, không xoá.

```markdown
---
raw_id: reddit-20261025-0001
source: reddit
url: https://...
title: "..."
posted_at: 2025-11-03        # ngày bài gốc
crawled_at: 2026-10-25
lang: en
author_hash: 3f9a1c2b7e
engagement: {score: 42, comments: 17}
task_id: T-001
---

<Nội dung gốc: post + comment liên quan, giữ nguyên văn. Mỗi comment ghi dòng đầu `[c:<author_hash>]`>
```

1 thread = 1 file raw. Comment không liên quan đến tàu thì bỏ.

Nội dung phải **nguyên văn** từ nguồn: được cắt đoạn không liên quan (ghi `[...]`), không viết lại, không tóm tắt. Ghi chú của Muse để ở dòng `Note:` riêng. Tên người được gọi/tag trong nội dung → `[name]`.
