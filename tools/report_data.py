"""Data cho report insight trên dashboard (ngoài dashboard_data.py và insight_draft.py).

Chạy: python3 -I tools/report_data.py   (từ gốc repo)
Output 05_outputs/dashboard/:
  ai_runs.json     - mỗi lượt engine × prompt: kênh hạng 1, hạng của Vexere, Vexere có được trích dẫn nguồn không
  ai_engines.json  - tổng hợp theo engine
  channels.json    - share of voice kênh bán trong nội dung người dùng (proxy, không phải thị phần)
  summary.json, actions.json, tips.json - copy từ 05_outputs/report-content.json (nội dung Claude viết, đã đối chiếu data)
Chỉ tính evidence của task reviewed và không bị đánh lỗi.
"""
import collections, glob, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "05_outputs", "dashboard")
BAD = {"wrong_tag", "quote_mismatch", "irrelevant"}
status = {}
for f in glob.glob(os.path.join(ROOT, "01_tasks", "T-*.md")):
    t = open(f, encoding="utf-8").read()
    status[re.search(r"task_id: (\S+)", t).group(1)] = re.search(r"status: (\S+)", t).group(1)
rows = [json.loads(l) for f in sorted(glob.glob(os.path.join(ROOT, "03_evidence", "*", "*.jsonl")))
        for l in open(f, encoding="utf-8") if l.strip()]
rows = [e for e in rows if e.get("review") not in BAD and status.get(e["task_id"]) == "reviewed"]

ENGINE = {"chatgpt": "ChatGPT", "gemini": "Gemini", "google": "Google AI"}
NAME = {"dsvn": "dsvn.vn", "twelve_go": "12Go", "baolau": "Baolau", "vexere": "Vexere", "trip_com": "Trip.com",
        "klook": "Klook", "station_counter": "Quầy ga", "chapa_express": "Chapa Express", "vetau": "vetau.com.vn",
        "bookaway": "Bookaway", "vietnam_railway_agent_site": "Site giả dạng DSVN", "myrealtrip": "MyRealTrip",
        "traveloka": "Traveloka", "local_agent": "Đại lý", "hotel_desk": "Khách sạn"}

# --- AI engine runs
prompts = {}
for f in glob.glob(os.path.join(ROOT, "02_raw", "serp_ai", "*", "*.md")):
    t = open(f, encoding="utf-8").read()
    rid = re.search(r"^raw_id:\s*(\S+)", t, re.M).group(1)
    pr = re.search(r"^prompt:\s*(.+)$", t, re.M)
    prompts[rid] = pr.group(1).strip() if pr else ""
runs = collections.OrderedDict()
for e in rows:
    if e["task_id"] != "T-009":
        continue
    m = re.search(r"(serp_ai-\d+-(\w+)-(p\d+))", e["ev_id"])
    key = m.group(1)
    r = runs.setdefault(key, {"run": key, "engine": ENGINE.get(m.group(2), m.group(2)), "prompt_id": m.group(3),
                              "prompt": prompts.get(e["raw_id"], ""), "top1": "", "vexere_rank": None,
                              "vexere_cited": False, "channels": 0})
    ents = e.get("entities") or []
    rk = e.get("rank")
    r["channels"] = max(r["channels"], rk or 0)
    if rk == 1 and ents:
        r["top1"] = NAME.get(ents[0], ents[0])
    if "vexere" in ents and rk and (r["vexere_rank"] is None or rk < r["vexere_rank"]):
        r["vexere_rank"] = rk
    if "vexere.com" in (e.get("cited_domains") or []):
        r["vexere_cited"] = True
ai_runs = sorted(runs.values(), key=lambda r: (r["engine"], r["prompt_id"]))
ai_eng = []
for eng in sorted({r["engine"] for r in ai_runs}):
    rs = [r for r in ai_runs if r["engine"] == eng]
    ai_eng.append({"engine": eng, "runs": len(rs), "vexere_mentioned": sum(1 for r in rs if r["vexere_rank"]),
                   "vexere_first": sum(1 for r in rs if r["vexere_rank"] == 1),
                   "dsvn_first": sum(1 for r in rs if r["top1"] == "dsvn.vn"),
                   "vexere_cited": sum(1 for r in rs if r["vexere_cited"])})

# --- Share of voice trong nội dung người dùng
USER_EXCL = {"T-009", "T-011", "T-013"}
CH = ["dsvn", "baolau", "twelve_go", "vexere", "station_counter", "klook", "trip_com", "vietnam_railway_agent_site", "bookaway", "myrealtrip"]
ch = []
for c in CH:
    es = [e for e in rows if e["task_id"] not in USER_EXCL and c in (e.get("entities") or [])]
    if not es:
        continue
    ch.append({"channel": NAME.get(c, c), "evidence": len(es), "authors": len({e["author_hash"] for e in es}),
               "positive": sum(1 for e in es if e["sentiment"] > 0), "negative": sum(1 for e in es if e["sentiment"] < 0),
               "neutral": sum(1 for e in es if e["sentiment"] == 0)})
ch.sort(key=lambda r: -r["authors"])

content = json.load(open(os.path.join(ROOT, "05_outputs", "report-content.json"), encoding="utf-8"))
for name, data in [("ai_runs", ai_runs), ("ai_engines", ai_eng), ("channels", ch),
                   ("summary", content["summary"]), ("actions", content["actions"]), ("tips", content["tips"])]:
    json.dump(data, open(os.path.join(OUT, f"{name}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(ai_eng, ensure_ascii=False)); print(json.dumps(ch[:6], ensure_ascii=False))
