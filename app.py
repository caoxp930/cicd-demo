from flask import Flask
from datetime import datetime
import subprocess

app = Flask(__name__)

# Get list of changed files in current commit
def get_changed_files():
    try:
        res = subprocess.check_output(
            ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"],
            text=True
        )
        lines = res.strip().splitlines()
        return lines if lines else ["No file changes detected"]
    except Exception as e:
        return [f"Failed to read changed files: {str(e)}"]

# Get short & full git commit hash as version tag
def get_git_commit_label():
    try:
        short_hash = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            text=True
        ).strip()
        full_hash = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            text=True
        ).strip()
        return f"Short Commit ID: {short_hash} | Full Commit Hash: {full_hash}"
    except Exception as e:
        return f"Failed to get commit version: {str(e)}"

@app.route("/")
def hello():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_label = get_git_commit_label()
    changed_files = get_changed_files()
    file_html = "<br>".join([f"✅ {f}" for f in changed_files])

    page_content = f"""
Feature Test: PR Merge Auto Build & Deploy Success<br>
————————————————————<br>
Current Access Time: {now}<br>
Deployment Version Label(Git Commit): {commit_label}<br>
————————————————————<br>
Changed Files From This Merge Commit:<br>
{file_html}
<p style="color:red">New Version Test: 2026 Demo Update, Used to Distinguish Old & New Deployment Versions 1</p>
    """
    return page_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)