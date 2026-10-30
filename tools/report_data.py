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
USER_EXCL = {"T-009", "T-011", "T-013", "T-015"}  # T-013, T-015: phía cung (trang + quảng cáo đối thủ)
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

# --- Phương pháp
GROUP = {"reddit": "Diễn đàn & cộng đồng", "reddit_in": "Diễn đàn & cộng đồng", "tripadvisor": "Diễn đàn & cộng đồng",
         "tripadvisor_forum": "Diễn đàn & cộng đồng", "muse_fb_radar": "Diễn đàn & cộng đồng",
         "gmaps_station": "Review sau trải nghiệm", "appstore": "Review sau trải nghiệm", "tripadvisor_review": "Review sau trải nghiệm",
         "youtube": "Vlog & blog", "youtube_in": "Vlog & blog", "youtube_kr": "Vlog & blog", "naver_blog": "Vlog & blog",
         "tistory": "Vlog & blog", "trip_com_cn": "Vlog & blog",
         "seat61": "Nguồn định hình nhận thức", "serp_ai": "Nguồn định hình nhận thức", "competitor_site": "Phía cung (trang đối thủ)", "ad_library": "Phía cung (trang đối thủ)"}
GROUPS = ["Diễn đàn & cộng đồng", "Review sau trải nghiệm", "Vlog & blog", "Nguồn định hình nhận thức", "Phía cung (trang đối thủ)"]
BIAS = {"Diễn đàn & cộng đồng": "Lệch về khách tự lên kế hoạch, nói tiếng Anh; câu hỏi trước chuyến nhiều hơn trải nghiệm",
        "Review sau trải nghiệm": "Lệch về phàn nàn và trải nghiệm cực đoan",
        "Vlog & blog": "Lệch về người làm nội dung, tuyến du lịch; có thể có affiliate",
        "Nguồn định hình nhận thức": "Ít mẫu, đọc theo ảnh hưởng; AI dao động giữa các lần chạy",
        "Phía cung (trang đối thủ)": "Claim của chính đối thủ, chưa kiểm chứng"}
srcname = lambda e: e["raw_id"].split("-")[0]
all_ev = [json.loads(l) for f in sorted(glob.glob(os.path.join(ROOT, "03_evidence", "*", "*.jsonl")))
          for l in open(f, encoding="utf-8") if l.strip()]
raw_files = glob.glob(os.path.join(ROOT, "02_raw", "*", "*", "*.md"))
raw_by_src = collections.Counter(f.split(os.sep)[-3] for f in raw_files)
msrc = []
for g in GROUPS:
    srcs = sorted({s for s, gg in GROUP.items() if gg == g and (raw_by_src.get(s) or any(srcname(e) == s for e in rows))})
    es = [e for e in rows if GROUP.get(srcname(e)) == g]
    msrc.append({"group": g, "sources": ", ".join(srcs), "raw": sum(raw_by_src.get(s, 0) for s in srcs),
                 "evidence": len(es), "authors": len({e["author_hash"] for e in es}), "bias": BIAS[g]})
evmap = json.load(open(os.path.join(ROOT, "05_outputs", "insight_ev.json"), encoding="utf-8"))
used = set(x for v in evmap.values() for x in v)
import datetime as _dt
_today = _dt.date.today()
def _fresh(e):
    try:
        return (_today - _dt.date.fromisoformat(str(e.get("posted_at"))[:10])).days <= 548
    except ValueError:
        return True
fresh_n = sum(1 for e in rows if _fresh(e))
# Ví dụ F04: từ quote tới insight
PRIV = {"lotus": "Lotus", "chapa_express": "Chapa Express", "violette": "Violette", "sapaly": "Sapaly", "livitrans": "Livitrans",
        "laman_express": "Laman", "vietage": "Vietage"}
f4 = [e for e in rows if e["ev_id"] in set(evmap.get("F04", []))]
ops = []
for k, n in PRIV.items():
    es = [e for e in f4 if k in (e.get("entities") or []) and e["task_id"] == "T-012"]
    if es:
        ops.append({"operator": n, "positive": sum(1 for e in es if e["sentiment"] > 0), "neutral": sum(1 for e in es if e["sentiment"] == 0),
                    "negative": sum(1 for e in es if e["sentiment"] < 0), "reviews": len({e["author_hash"] for e in es})})
ops.sort(key=lambda r: -(r["positive"] - r["negative"]))
DOWN = ["tripadvisor_review-20261027-0001-e08", "tripadvisor_review-20261027-0001-e10", "tripadvisor_review-20261027-0005-e04"]
def claim(label, cond, src_note):
    es = [e for e in f4 if cond(e)]
    return {"claim": label, "evidence": len(es), "authors": len({e["author_hash"] for e in es}), "how": src_note}
claims = [
    claim("Được khen đồ ăn, nhân viên", lambda e: e["sentiment"] > 0 and set(e["topics"]) & {"food_onboard", "staff_attitude"}, "topic food_onboard/staff_attitude, sắc thái tích cực"),
    claim("Vẫn ngủ kém, ồn, xóc", lambda e: e["sentiment"] < 0 and "noise_sleep" in e["topics"], "topic noise_sleep, sắc thái tiêu cực"),
    claim("Giá không xứng", lambda e: e["sentiment"] < 0 and "price_level" in e["topics"], "topic price_level, sắc thái tiêu cực"),
    claim("Bị đổi sang cabin chung dù đã trả tiền cabin riêng", lambda e: e["ev_id"] in DOWN, "đọc tay từng review, 2 là Chapa Express"),
]
funnel = [
    {"step": "Nguồn đã thử", "value": len({f.split(os.sep)[-3] for f in raw_files}) + 4, "note": "Gồm 4 nguồn bị chặn đăng nhập, không thu được: Quora, Xiaohongshu, Mafengwo, TikTok"},
    {"step": "Bài gốc thu về", "value": len(raw_files), "note": "Thread, review, video, trang - lưu dạng trích đoạn, có link gốc"},
    {"step": "Đơn vị evidence", "value": len(all_ev), "note": "Mỗi ý riêng biệt trong một bài = 1 evidence, kèm quote nguyên văn"},
    {"step": "Đã duyệt, không lỗi", "value": len(rows), "note": "Task đã qua review; loại dòng bị đánh lỗi khi spot-check"},
    {"step": "Còn trong 18 tháng", "value": fresh_n, "note": "Bài cũ hơn 18 tháng chỉ làm bối cảnh, không tính vào ngưỡng"},
    {"step": "Dùng trong insight", "value": len(used), "note": "Evidence nằm trong ít nhất 1 cụm insight F01-F14"},
    {"step": "Insight cuối", "value": len(evmap), "note": "Mỗi insight đã đối chiếu từng nhận định với evidence"},
]
qa = []
for f in sorted(glob.glob(os.path.join(ROOT, "01_tasks", "T-*.md"))):
    t = open(f, encoding="utf-8").read()
    tid = re.search(r"task_id: (\S+)", t).group(1)
    title = re.search(r"^# \S+ - (.+)$", t, re.M)
    rev = t.split("## Review", 1)[1] if "## Review" in t else ""
    es = [e for e in all_ev if e["task_id"] == tid]
    chk = [e for e in es if e.get("review")]
    bad = [e for e in chk if e.get("review") in BAD]
    qa.append({"task_id": tid, "title": title.group(1).strip() if title else tid, "evidence": len(es), "checked": len(chk),
               "errors": len(bad), "error_rate": round(len(bad) / len(chk), 3) if chk else None,
               "rework_rounds": len(re.findall(r"`rework`", rev.split("Trả lời")[0])) if rev else 0,
               "status": status.get(tid, "")})
# Tam giác hoá: insight × nhóm nguồn (số evidence đã duyệt)
ev_src = {e["ev_id"]: GROUP.get(srcname(e), "Khác") for e in rows}
ins = json.load(open(os.path.join(OUT, "insights.json"), encoding="utf-8"))
tri = []
for r in ins:
    c = collections.Counter(ev_src.get(x, "Khác") for x in evmap.get(r["id"], []))
    for g in GROUPS:
        tri.append({"insight": r["id"], "group": g, "evidence": c.get(g, 0)})
# Codebook
tax = open(os.path.join(ROOT, "00_brain", "taxonomy.md"), encoding="utf-8").read()
def sec(a, b):
    return tax.split(a, 1)[1].split(b, 1)[0] if a in tax else ""
codebook = [
    {"dimension": "Loại ý (type)", "codes": 9, "used": len({e["type"] for e in rows}), "example": "pain, barrier, question, tip, workaround, comparison, praise, need, signal"},
    {"dimension": "Bước hành trình (stage)", "codes": 10, "used": len({e["stage"] for e in rows}), "example": "plan → compare → book → pre_trip → station → onboard → last_mile → post_trip"},
    {"dimension": "Chủ đề (topic)", "codes": len(set(re.findall(r"`([a-z_]+)`", sec("## topic", "## segment")))), "used": len({t for e in rows for t in e["topics"]}), "example": "class_cabin, seat_selection, trust_scam, last_mile_transport, noise_sleep..."},
    {"dimension": "Nhóm khách (segment)", "codes": len(set(re.findall(r"\| `([a-z_]+)` \|", sec("## segment", "## topic →")))), "used": len({e["segment"] for e in rows}), "example": "intl_family, intl_couple, intl_group_tour, vn_domestic, unknown"},
    {"dimension": "Thị trường (market)", "codes": len(set(re.findall(r"\| `([a-z_]+)` \|", sec("## market", "Quy tắc")))), "used": len({e.get("market") or "unknown" for e in rows}), "example": "kr, in, cn, tw_hk, western, vn, unknown"},
    {"dimension": "Thực thể (kênh, hãng tàu)", "codes": len(set(re.findall(r"`([a-z0-9_]+)`", sec("## entity", "## route")))), "used": len({x for e in rows for x in (e.get("entities") or [])}), "example": "dsvn, baolau, twelve_go, vexere, chapa_express, lotus..."},
    {"dimension": "Sắc thái (sentiment)", "codes": 3, "used": len({e["sentiment"] for e in rows}), "example": "-1 tiêu cực, 0 trung tính, 1 tích cực"},
]
content = json.load(open(os.path.join(ROOT, "05_outputs", "report-content.json"), encoding="utf-8"))
for name, data in [("method_funnel", funnel), ("method_qa", qa), ("method_sources", msrc), ("triangulation", tri),
                   ("codebook", codebook), ("walk_ops", ops), ("walk_claims", claims), ("rejected", content["rejected"]), ("method_rules", content["method_rules"]), ("ai_runs", ai_runs), ("ai_engines", ai_eng), ("channels", ch),
                   ("summary", content["summary"]), ("actions", content["actions"]), ("tips", content["tips"])]:
    json.dump(data, open(os.path.join(OUT, f"{name}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(ai_eng, ensure_ascii=False)); print(json.dumps(ch[:6], ensure_ascii=False))
