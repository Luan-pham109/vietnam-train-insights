"""Tính số evidence cho bảng insight nháp. Định nghĩa từng insight ở 05_outputs/insight-draft.defs.json
(do Claude viết). Output: 05_outputs/dashboard/insights.json + 05_outputs/insight-draft.md
Chạy: python3 -I tools/insight_draft.py"""
import glob, json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BAD = {"wrong_tag", "quote_mismatch", "irrelevant"}
status = {}
for f in glob.glob(os.path.join(ROOT, "01_tasks", "T-*.md")):
    t = open(f, encoding="utf-8").read()
    status[re.search(r"task_id: (\S+)", t).group(1)] = re.search(r"status: (\S+)", t).group(1)
rows = [json.loads(l) for f in glob.glob(os.path.join(ROOT, "03_evidence", "*", "*.jsonl"))
        for l in open(f, encoding="utf-8") if l.strip()]
rows = [e for e in rows if e.get("review") not in BAD]
defs = json.load(open(os.path.join(ROOT, "05_outputs", "insight-draft.defs.json"), encoding="utf-8"))
out = []
for d in defs:
    def match(e):
        if not set(d["topics"]) & set(e.get("topics", [])):
            return False
        if d.get("lang") and e.get("lang") != d["lang"]:
            return False
        if d.get("sentiment_neg") and e.get("sentiment", 0) >= 0:
            return False
        return True
    es = [e for e in rows if match(e)]
    rv = [e for e in es if status.get(e["task_id"]) == "reviewed"]
    def stats(x):
        return len(x), len({e["author_hash"] for e in x}), len({e["raw_id"].split("-")[0] for e in x})
    n, a, s = stats(es)
    rn, ra, rs = stats(rv)
    conf = "trung bình" if rn >= 10 and rs >= 3 and ra >= 5 else "thấp"
    st = "supported" if conf == "trung bình" else "hypothesis"
    out.append({"id": d["id"], "insight": d["insight"], "who": d["who"], "evidence": n, "authors": a, "sources": s,
                "evidence_reviewed": rn, "sources_reviewed": rs, "confidence": conf, "status": st,
                "action": d["action"], "quote": d["quote"], "vexere_fit": d["vexere_fit"], "note": d.get("note", "")})
# Card insight đã viết (04_insights) đứng đầu bảng
cards = []
for f in sorted(glob.glob(os.path.join(ROOT, "04_insights", "INS-*.md"))):
    t = open(f, encoding="utf-8").read()
    g = lambda k: (re.search(rf"^{k}: (.*)$", t, re.M) or [None, ""])[1].strip()
    title = re.search(r"^# INS-\d+ - (.+)$", t, re.M)
    q = re.search(r'"([^"]{20,200})"', t)
    so = re.search(r"## So what cho Vexere\n+- (.+)", t)
    cards.append({"id": g("insight_id"), "insight": title.group(1) if title else "", "who": "Xem card",
                  "evidence": int(g("evidence_count") or 0), "authors": int(g("unique_authors") or 0),
                  "sources": len([x for x in g("sources").strip("[]").split(",") if x.strip()]),
                  "evidence_reviewed": None, "sources_reviewed": None,
                  "confidence": {"medium": "trung bình", "low": "thấp", "high": "cao"}.get(g("confidence"), g("confidence")),
                  "status": g("status"), "action": so.group(1) if so else "", "quote": q.group(1) if q else "",
                  "vexere_fit": "Card đầy đủ trong 04_insights", "note": ""})
out = cards + out
json.dump(out, open(os.path.join(ROOT, "05_outputs", "dashboard", "insights.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
md = ["# Insight nháp - chờ Luan review", "", "Tự sinh bởi `tools/insight_draft.py`. Số evidence tính theo topic; tin cậy chỉ tính evidence của task đã reviewed (ngưỡng: ≥10 ev, ≥3 nguồn, ≥5 tác giả).", "",
      "| ID | Insight | Nhóm khách | Ev (đã duyệt / tổng) | Nguồn | Tin cậy | Gắn với Vexere | Hành động đề xuất |", "|---|---|---|---|---|---|---|---|"]
for r in out:
    md.append(f"| {r['id']} | {r['insight']} | {r['who']} | {r['evidence_reviewed'] if r['evidence_reviewed'] is not None else '-'} / {r['evidence']} | {r['sources']} | {r['confidence']} | {r['vexere_fit']} | {r['action']} |")
md += ["", "## Quote tiêu biểu"] + [f"- **{r['id']}**: \"{r['quote']}\"" + (f" - _{r['note']}_" if r['note'] else "") for r in out]
open(os.path.join(ROOT, "05_outputs", "insight-draft.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
for r in out: print(r["id"], r["evidence_reviewed"], r["evidence"], r["sources"], r["confidence"])
