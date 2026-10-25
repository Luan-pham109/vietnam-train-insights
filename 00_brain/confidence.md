# Rule confidence cho insight

| Mức | Điều kiện |
|---|---|
| `low` | <10 evidence **hoặc** chỉ 1 nguồn |
| `medium` | ≥10 evidence **và** ≥3 nguồn **và** ≥5 tác giả khác nhau |
| `high` | Đạt `medium` **và** có xác nhận từ data nội bộ (`06_validation/`) |

## Status của insight
`hypothesis` (dưới medium) → `supported` (medium) → `validated` (high) / `rejected` (data nội bộ bác bỏ)

## Quy tắc
- Đếm theo `author_hash` khác nhau, không đếm theo số evidence (1 người spam 10 comment = 1).
- Evidence quá 18 tháng: chỉ dùng làm bối cảnh, không tính vào ngưỡng (giá, chính sách, app thay đổi nhanh).
- Nguồn định hình nhận thức (`seat61`, `serp_ai`) được đánh giá riêng theo ảnh hưởng, không đếm số lượng.
- Không cộng dồn giữa các segment. Insight cho `intl_*` phải đứng trên evidence `intl_*`.
