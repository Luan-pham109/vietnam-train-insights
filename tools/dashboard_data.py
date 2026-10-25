"""Tính số liệu tiến độ + độ phủ từ repo, xuất JSON cho dashboard.

Chạy: python3 -I tools/dashboard_data.py   (từ gốc repo)
Output: 05_outputs/dashboard/{tasks,coverage,sources,journey,history}.json
history.json được giữ trong repo và cập nhật dòng của ngày chạy.
"""
import datetime as dt
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "05_outputs", "dashboard")
BAD_REVIEW = {"wrong_tag", "quote_mismatch", "irrelevant"}
STAGES = ["inspire", "plan", "compare", "book", "pre_trip", "station", "onboard", "last_mile", "post_trip"]
SEG_GROUPS = ["Nước ngoài", "Expat", "Khách Việt", "Chưa rõ"]
THRESH = {"evidence": 10, "sources": 3, "authors": 5}
FRESH_DAYS = 548  # 18 tháng


def p(*parts):
    return os.path.join(ROOT, *parts)


def table_rows(path):
    """Trả về (section_heading, cells) cho mọi dòng bảng markdown không phải header/separator."""
    section = ""
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("## "):
                section = line[3:].strip()
            if not line.startswith("|") or re.match(r"^\|\s*-", line):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            yield section, cells


def frontmatter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        k, v = line.split(":", 1)
        v = v.split("#", 1)[0].strip().strip('"').strip("'")
        meta[k.strip()] = v
    return meta, m.group(2)


def seg_group(seg):
    if not seg or seg == "unknown":
        return "Chưa rõ"
    if seg.startswith("intl"):
        return "Nước ngoài"
    if seg == "expat":
        return "Expat"
    if seg.startswith("vn"):
        return "Khách Việt"
    return "Chưa rõ"


def main():
    today = dt.date.today()
    os.makedirs(OUT, exist_ok=True)

    # --- Question bank
    questions = []
    for section, c in table_rows(p("00_brain", "questions.md")):
        if re.fullmatch(r"[CMI]\d{2}", c[0]):
            questions.append({"q_id": c[0], "group": section.split(" - ")[-1], "question": c[1],
                              "priority": c[2], "decision": c[3] if len(c) > 3 else ""})

    # --- Source map
    sources = []
    for _, c in table_rows(p("00_brain", "source-map.md")):
        code = c[0].strip("`")
        if code and code != "Mã nguồn" and len(c) >= 6:
            sources.append({"source": code, "name": c[1], "wave": int(c[5]) if c[5].isdigit() else None})

    # --- Raw
    raw_by_id, raw_by_source, raw_by_task = {}, {}, {}
    for fp in glob.glob(p("02_raw", "*", "*", "*.md")):
        meta, _ = frontmatter(fp)
        src = meta.get("source") or fp.split(os.sep)[-3]
        raw_by_id[meta.get("raw_id", os.path.basename(fp)[:-3])] = src
        raw_by_source[src] = raw_by_source.get(src, 0) + 1
        t = meta.get("task_id")
        if t:
            raw_by_task[t] = raw_by_task.get(t, 0) + 1

    # --- Evidence
    evidence = []
    for fp in glob.glob(p("03_evidence", "*", "*.jsonl")):
        with open(fp, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    ev = json.loads(line)
                except json.JSONDecodeError:
                    continue
                ev["_task"] = ev.get("task_id") or os.path.basename(fp)[:-6]
                ev["_source"] = raw_by_id.get(ev.get("raw_id"), "unknown")
                evidence.append(ev)

    def usable(ev):
        if ev.get("review") in BAD_REVIEW:
            return False
        try:
            age = (today - dt.date.fromisoformat(str(ev.get("posted_at"))[:10])).days
        except ValueError:
            return True
        return age <= FRESH_DAYS

    good = [e for e in evidence if usable(e)]

    # --- Tasks
    tasks = []
    for fp in sorted(glob.glob(p("01_tasks", "T-*.md"))):
        meta, body = frontmatter(fp)
        tid = meta.get("task_id", os.path.basename(fp)[:-3])
        title = re.search(r"^# \S+ - (.+)$", body, re.M)
        blocked = re.search(r"Chờ (T-\d+) reviewed", body)
        evs = [e for e in evidence if e["_task"] == tid]
        checked = [e for e in evs if e.get("review")]
        bad = [e for e in checked if e.get("review") in BAD_REVIEW]
        tasks.append({
            "task_id": tid,
            "title": title.group(1).strip() if title else tid,
            "source": meta.get("source", ""),
            "priority": meta.get("priority", ""),
            "status": meta.get("status", "open"),
            "blocked_by": blocked.group(1) if blocked else "",
            "claimed_at": meta.get("claimed_at", ""),
            "submitted_at": meta.get("submitted_at", ""),
            "raw": raw_by_task.get(tid, 0),
            "evidence": len(evs),
            "checked": len(checked),
            "error_rate": round(len(bad) / len(checked), 3) if checked else None,
        })
    status_of = {t["task_id"]: t["status"] for t in tasks}
    for t in tasks:
        if t["blocked_by"] and status_of.get(t["blocked_by"]) == "reviewed":
            t["blocked_by"] = ""

    # --- Coverage per question
    coverage = []
    for q in questions:
        evs = [e for e in good if q["q_id"] in (e.get("questions") or [])]
        n_ev = len(evs)
        n_src = len({e["_source"] for e in evs})
        n_auth = len({e.get("author_hash") for e in evs if e.get("author_hash")})
        n_intl = sum(1 for e in evs if seg_group(e.get("segment")) == "Nước ngoài")
        score = min(n_ev / THRESH["evidence"], 1) + min(n_src / THRESH["sources"], 1) + min(n_auth / THRESH["authors"], 1)
        if n_ev == 0:
            level = "none"
        elif n_ev >= THRESH["evidence"] and n_src >= THRESH["sources"] and n_auth >= THRESH["authors"]:
            level = "medium"
        else:
            level = "low"
        coverage.append({**{k: q[k] for k in ("q_id", "group", "question", "priority")},
                         "evidence": n_ev, "sources": n_src, "authors": n_auth, "intl_evidence": n_intl,
                         "score": round(score / 3, 3), "level": level})

    # --- Sources progress
    task_status_by_source = {}
    for t in tasks:
        task_status_by_source.setdefault(t["source"], []).append(t["status"])
    src_rows = []
    for s in sources:
        sts = task_status_by_source.get(s["source"], [])
        if not sts:
            state = "chưa giao"
        elif all(x == "reviewed" for x in sts):
            state = "đã duyệt"
        elif any(x in ("in_progress", "submitted", "rework") for x in sts):
            state = "đang chạy"
        else:
            state = "đã giao"
        src_rows.append({**s, "state": state, "raw": raw_by_source.get(s["source"], 0),
                         "evidence": sum(1 for e in good if e["_source"] == s["source"])})

    # --- Journey coverage stage x segment group
    journey = []
    for st in STAGES:
        for g in SEG_GROUPS:
            journey.append({"stage": st, "segment": g,
                            "evidence": sum(1 for e in good if e.get("stage") == st and seg_group(e.get("segment")) == g)})

    # --- History (giữ trong repo)
    hist_path = os.path.join(OUT, "history.json")
    try:
        with open(hist_path, encoding="utf-8") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []
    p0 = [c for c in coverage if c["priority"] == "P0"]
    row = {
        "date": today.isoformat(),
        "raw": len(raw_by_id),
        "evidence": len(evidence),
        "evidence_usable": len(good),
        "authors": len({e.get("author_hash") for e in good if e.get("author_hash")}),
        "questions_medium": sum(1 for c in coverage if c["level"] == "medium"),
        "p0_medium": sum(1 for c in p0 if c["level"] == "medium"),
        "p0_total": len(p0),
        "questions_total": len(coverage),
        "coverage_score": round(sum(c["score"] for c in coverage) / len(coverage), 3) if coverage else 0,
        "tasks_reviewed": sum(1 for t in tasks if t["status"] == "reviewed"),
        "tasks_total": len(tasks),
    }
    history = [h for h in history if h.get("date") != row["date"]] + [row]
    history.sort(key=lambda h: h["date"])

    for name, data in [("tasks", tasks), ("coverage", coverage), ("sources", src_rows),
                       ("journey", journey), ("history", history)]:
        with open(os.path.join(OUT, f"{name}.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
    print(json.dumps(row, ensure_ascii=False))


if __name__ == "__main__":
    main()
