"""Kiểm tra evidence của một hoặc nhiều task trước khi nộp / khi review.

Chạy (từ gốc repo): python3 -I tools/validate_evidence.py T-009 T-012
Kiểm: JSON hợp lệ, field bắt buộc (schema v0.3), mã type/stage/topics/segment/market/
origin_hint/entities/routes/questions có trong 00_brain, raw_id tồn tại, quote là chuỗi con
của raw (chuẩn hoá khoảng trắng), độ dài quote, origin_cue có thì phải có origin_hint.
Thoát mã 1 nếu có lỗi. Muse nên chạy trước khi đổi status sang submitted.
"""
import collections
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAX = open(os.path.join(ROOT, "00_brain", "taxonomy.md"), encoding="utf-8").read()
QB = open(os.path.join(ROOT, "00_brain", "questions.md"), encoding="utf-8").read()


def sect(start, end):
    return TAX.split(start, 1)[1].split(end, 1)[0]


TYPES = {"need", "pain", "barrier", "question", "tip", "workaround", "comparison", "praise", "signal"}
STAGES = {"inspire", "plan", "compare", "book", "pre_trip", "station", "onboard", "last_mile", "post_trip", "na"}
TOPICS = set(re.findall(r"`([a-z_]+)`", sect("## topic", "## segment")))
SEGS = set(re.findall(r"\| `([a-z_]+)` \|", sect("## segment", "## topic →")))
MARKETS = set(re.findall(r"\| `([a-z_]+)` \|", sect("## market", "Quy tắc")))
ENTS = set(re.findall(r"`([a-z0-9_]+)`", re.sub(r"không(\*\*)? (phải|viết) `[a-z0-9_]+`", "",
                                                 sect("## entity", "## route"))))
ROUTES = set(re.findall(r"`([A-Z]{3})`", sect("## route", "## Changelog")))
QS = set(re.findall(r"\| ([CMI]\d\d) \|", QB))
TRAIN_CODE = re.compile(r"^(se|sp|snt|tn|hd|nh|ht|qb|lc|sh|dh)\d+[a-z]?$")
REQ = ["ev_id", "raw_id", "task_id", "quote", "summary_vi", "type", "stage", "topics", "segment",
       "sentiment", "questions", "author_hash", "posted_at", "lang"]
CJK = ("zh", "ja", "ko")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def load_raws():
    raws = {}
    for f in glob.glob(os.path.join(ROOT, "02_raw", "**", "*.md"), recursive=True):
        if f.endswith("README.md"):
            continue
        t = open(f, encoding="utf-8").read()
        m = re.search(r"^raw_id:\s*(\S+)", t, re.M)
        if m:
            raws[m.group(1)] = norm(t)
    return raws


def check(task, raws):
    errs, ex, n = collections.Counter(), collections.defaultdict(list), 0
    path = glob.glob(os.path.join(ROOT, "03_evidence", "*", f"{task}.jsonl"))
    if not path:
        print(f"== {task}: không thấy file evidence")
        return 1
    for i, line in enumerate(open(path[0], encoding="utf-8"), 1):
        if not line.strip():
            continue
        n += 1
        try:
            e = json.loads(line)
        except ValueError:
            errs["json"] += 1
            ex["json"].append(f"dòng {i}")
            continue
        eid = e.get("ev_id", f"dòng {i}")
        e.setdefault("market", "unknown")  # evidence trước schema v0.2 thiếu market = unknown

        def bad(k, v=""):
            errs[k] += 1
            ex[k].append(f"{eid} ({v})" if v != "" else eid)

        for k in REQ:
            if k not in e:
                bad("thiếu_" + k)
        if "author_role" not in e and int(re.sub(r"\D", "", task) or 0) >= 6:
            bad("thiếu_author_role")  # bắt buộc từ schema v0.3 (task T-006 trở đi)
        if e.get("type") not in TYPES:
            bad("type", e.get("type"))
        if e.get("stage") not in STAGES:
            bad("stage", e.get("stage"))
        tp = e.get("topics") or []
        if not 1 <= len(tp) <= 3:
            bad("số_topic", len(tp))
        for t in tp:
            if t not in TOPICS:
                bad("topic", t)
        if "other" in tp and not e.get("topic_suggest"):
            bad("other_thiếu_topic_suggest")
        if e.get("segment") not in SEGS:
            bad("segment", e.get("segment"))
        if e.get("market") not in MARKETS:
            bad("market", e.get("market"))
        if "author_role" in e and e["author_role"] not in ("op", "reply", "review"):
            bad("author_role", e["author_role"])
        if e.get("origin_hint"):
            if e["origin_hint"] not in MARKETS:
                bad("origin_hint", e["origin_hint"])
            if not e.get("origin_cue"):
                bad("origin_hint_thiếu_cue")
        elif e.get("origin_cue"):
            bad("origin_cue_thiếu_hint", e["origin_cue"])
        for x in e.get("entities") or []:
            if x not in ENTS and not TRAIN_CODE.match(x):
                bad("entity", x)
        for r in e.get("routes") or []:
            if any(p not in ROUTES for p in r.split("-")):
                bad("route", r)
        if not e.get("questions"):
            bad("questions_rỗng")
        for q in e.get("questions") or []:
            if q not in QS:
                bad("question", q)
        if e.get("sentiment") not in (-1, 0, 1):
            bad("sentiment", e.get("sentiment"))
        raw = raws.get(e.get("raw_id"))
        if raw is None:
            bad("raw_không_tồn_tại", e.get("raw_id"))
        elif norm(e.get("quote", "")) not in raw:
            bad("quote_không_khớp_raw", e.get("quote", "")[:50])
        q = e.get("quote", "")
        if str(e.get("lang", "")).startswith(CJK):
            if len(q) > 100:
                bad("quote_dài", f"{len(q)} ký tự")
        elif len(q.replace("[...]", " ").split()) > 50:
            bad("quote_dài", f"{len(q.replace('[...]', ' ').split())} từ")
    total = sum(errs.values())
    print(f"== {task}: {n} evidence, {total} lỗi")
    for k, v in errs.most_common():
        print(f"  {k}: {v}  vd: {', '.join(ex[k][:5])}")
    return 1 if total else 0


if __name__ == "__main__":
    tasks = sys.argv[1:]
    if not tasks:
        sys.exit("Dùng: python3 -I tools/validate_evidence.py T-xxx [T-yyy ...]")
    raws = load_raws()
    sys.exit(max(check(t, raws) for t in tasks))
