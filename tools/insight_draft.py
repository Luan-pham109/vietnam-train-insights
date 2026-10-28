"""Tính số liệu + chọn quote cho bộ insight. Định nghĩa ở 05_outputs/insight-draft.defs.json (Claude viết).
Output: 05_outputs/dashboard/insights.json + 05_outputs/insight-draft.md
Chạy: python3 -I tools/insight_draft.py

Bộ lọc mỗi insight (AND giữa các điều kiện có mặt):
  topics (any) | entities (any) | match: "topics_or_entities" (mặc định topics)
  lang, market, author_role, sentiment ("neg"/"pos"), tasks (list), exclude_tasks (list)
Tin cậy: chỉ tính evidence của task reviewed và không bị đánh lỗi.
  trung bình: ≥10 evidence, ≥3 nguồn, ≥5 tác giả. Insight có "influence": true (nguồn định hình nhận thức
  như serp_ai) đánh giá theo ảnh hưởng, ghi "đo lường" thay vì ngưỡng đếm.
"""
import glob, json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BAD = {"wrong_tag", "quote_mismatch", "irrelevant"}
status = {}
for f in glob.glob(os.path.join(ROOT, "01_tasks", "T-*.md")):
    t = open(f, encoding="utf-8").read()
    status[re.search(r"task_id: (\S+)", t).group(1)] = re.search(r"status: (\S+)", t).group(1)
rows = [json.loads(l) for f in sorted(glob.glob(os.path.join(ROOT, "03_evidence", "*", "*.jsonl")))
        for l in open(f, encoding="utf-8") if l.strip()]
rows = [e for e in rows if e.get("review") not in BAD]
src = lambda e: e["raw_id"].split("-")[0]
defs = json.load(open(os.path.join(ROOT, "05_outputs", "insight-draft.defs.json"), encoding="utf-8"))


def match(d, e):
    tp = bool(set(d.get("topics", [])) & set(e.get("topics", [])))
    en = bool(set(d.get("entities", [])) & set(e.get("entities") or []))
    mode = d.get("match", "topics")
    if mode == "any": pass
    elif mode == "topics" and not tp: return False
    if mode == "entities" and not en: return False
    if mode == "topics_or_entities" and not (tp or en): return False
    if mode == "topics_and_entities" and not (tp and en): return False
    if d.get("lang") and e.get("lang") != d["lang"]: return False
    if d.get("market") and e.get("market") != d["market"]: return False
    if d.get("author_role") and e.get("author_role") != d["author_role"]: return False
    if d.get("sentiment") == "neg" and e.get("sentiment", 0) >= 0: return False
    if d.get("sentiment") == "pos" and e.get("sentiment", 0) <= 0: return False
    if d.get("tasks") and e["task_id"] not in d["tasks"]: return False
    if d.get("exclude_tasks") and e["task_id"] in d["exclude_tasks"]: return False
    return True


def stats(x):
    return len(x), len({e["author_hash"] for e in x}), len({src(e) for e in x})


out = []
for d in defs:
    es = [e for e in rows if match(d, e)]
    rv = [e for e in es if status.get(e["task_id"]) == "reviewed"]
    n, a, s = stats(es)
    rn, ra, rs = stats(rv)
    if d.get("influence"):
        conf = "đo lường"
    else:
        conf = "trung bình" if rn >= 10 and rs >= 3 and ra >= 5 else "thấp"
    # quote: ưu tiên ev_id Claude chỉ định, sau đó tự chọn đa dạng nguồn
    pick = [e for i in d.get("quote_ids", []) for e in rv if e["ev_id"] == i]
    seen = {src(e) for e in pick}
    for e in sorted(rv, key=lambda e: (e.get("sentiment", 0) if d.get("sentiment") != "pos" else -e.get("sentiment", 0))):
        if len(pick) >= 3: break
        if src(e) in seen or e in pick: continue
        pick.append(e); seen.add(src(e))
    out.append({"id": d["id"], "theme": d.get("theme", ""), "insight": d["insight"], "who": d["who"],
                "evidence": n, "authors": a, "sources": s, "evidence_reviewed": rn, "authors_reviewed": ra,
                "sources_reviewed": rs, "source_list": sorted({src(e) for e in rv}),
                "confidence": conf, "status": "supported" if conf in ("trung bình", "đo lường") else "hypothesis",
                "action": d["action"], "quote": d.get("quote") or (pick[0]["quote"] if pick else ""),
                "quotes": [{"ev_id": e["ev_id"], "quote": e["quote"], "summary_vi": e.get("summary_vi", "")} for e in pick],
                "vexere_fit": d["vexere_fit"], "note": d.get("note", ""), "counter": d.get("counter", "")})
json.dump(out, open(os.path.join(ROOT, "05_outputs", "dashboard", "insights.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
md = ["# Bảng insight - tự sinh", "", "Sinh bởi `tools/insight_draft.py` từ `05_outputs/insight-draft.defs.json`. Tin cậy chỉ tính evidence của task đã reviewed (ngưỡng ≥10 ev, ≥3 nguồn, ≥5 tác giả).", "",
      "| ID | Insight | Nhóm khách | Ev đã duyệt | Tác giả | Nguồn | Tin cậy | Gắn với Vexere |", "|---|---|---|---|---|---|---|---|"]
for r in out:
    md.append(f"| {r['id']} | {r['insight']} | {r['who']} | {r['evidence_reviewed']} | {r['authors_reviewed']} | {r['sources_reviewed']} | {r['confidence']} | {r['vexere_fit']} |")
open(os.path.join(ROOT, "05_outputs", "insight-draft.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
for r in out:
    print(r["id"], r["evidence_reviewed"], r["authors_reviewed"], r["sources_reviewed"], r["confidence"], r["source_list"])
