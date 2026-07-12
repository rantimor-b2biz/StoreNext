#!/usr/bin/env python3
"""
Backfill all O-output/W*/final/final-post.md → Firebase mediaPlan/storenext/{week}
Run from the StoreNext repo root:  python T-tools/backfill-media-plan.py
"""
import json, os, re, glob, urllib.request, pathlib

# ── Config ────────────────────────────────────────────────────────────────────
DB_URL    = "https://annual-plan-736ee-default-rtdb.firebaseio.com"
CLIENT_ID = "storenext"
ENV_FILE  = pathlib.Path(__file__).parent.parent / ".env"

# ── Load secret from .env ─────────────────────────────────────────────────────
secret = os.environ.get("FIREBASE_DB_SECRET", "")
if not secret and ENV_FILE.exists():
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("FIREBASE_DB_SECRET="):
            secret = line.split("=", 1)[1].strip().strip('"').strip("'")
            break

if not secret:
    print("ERROR: FIREBASE_DB_SECRET not found in .env or environment.")
    print("Add to .env:  FIREBASE_DB_SECRET=your_secret_here")
    raise SystemExit(1)

# ── Parse helpers ─────────────────────────────────────────────────────────────
def field(content, name):
    m = re.search(rf'\*\*{re.escape(name)}:\*\*\s*(.+)', content)
    return m.group(1).strip() if m else ""

def parse_and_push(post_file):
    parts       = pathlib.Path(post_file).parts
    week        = parts[1]           # e.g. W25
    week_folder = "/".join(parts[:2])

    raw = pathlib.Path(post_file).read_text(encoding="utf-8")

    status_raw  = field(raw, "Status").lower()
    category    = field(raw, "Category")
    publish_str = field(raw, "Publish")
    language    = field(raw, "Language")

    date_match   = re.search(r"(\d{4}-\d{2}-\d{2})", publish_str)
    publish_date = date_match.group(1) if date_match else ""

    body_parts = raw.split("---")
    post_text  = body_parts[1].strip() if len(body_parts) > 1 else raw

    hook = ""
    for line in post_text.split("\n"):
        ln = line.strip()
        if ln and not ln.startswith("#") and not ln.startswith("**"):
            hook = ln
            break

    posts_data  = []
    visual_file = f"{week_folder}/process/visual-data.json"
    if os.path.exists(visual_file):
        vd = json.loads(pathlib.Path(visual_file).read_text(encoding="utf-8"))
        posts_data = vd.get("posts", [])
        if not hook and posts_data:
            hook = posts_data[0].get("hook", "")
        if not category and posts_data:
            category = posts_data[0].get("category", "")

    payload = {
        "week":        week,
        "publishDate": publish_date,
        "publishStr":  publish_str,
        "category":    category,
        "language":    language,
        "status":      status_raw if status_raw in ("approved", "published") else "approved",
        "hook":        hook,
        "postText":    post_text,
        "posts":       posts_data,
    }

    body = json.dumps(payload).encode("utf-8")
    url  = f"{DB_URL}/mediaPlan/{CLIENT_ID}/{week}.json?auth={secret}"
    req  = urllib.request.Request(url, data=body, method="PUT",
                                  headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        print(f"  ✓  {week}  →  HTTP {resp.status}  ({category or 'no category'})")

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    files = sorted(glob.glob("O-output/W*/final/final-post.md"))
    if not files:
        print("No final-post.md files found. Run from the StoreNext repo root.")
        raise SystemExit(1)

    print(f"Syncing {len(files)} post(s) to Firebase mediaPlan/{CLIENT_ID}/...\n")
    ok, err = 0, 0
    for f in files:
        try:
            parse_and_push(f)
            ok += 1
        except Exception as e:
            print(f"  ✗  {f}: {e}")
            err += 1

    print(f"\nDone — {ok} synced, {err} errors.")
    if ok:
        print("Open plan.rantimor.com → Media Plan tab — data should appear now.")
