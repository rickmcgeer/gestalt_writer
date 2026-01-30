import requests
import json
import os

# Use environment variable for security
GITHUB_TOKEN = os.environ.get("GITHUB_PAT")
REPO_OWNER = "rickmcgeer"
REPO_NAME = "aiko-chats"
WORKFLOW_FILENAME = "write_gestalt.yml"
BRANCH = "main"

def run_write_gestalt(title, tags, tier, content):
    api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/{WORKFLOW_FILENAME}/dispatches"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    payload = {
        "ref": BRANCH,
        "inputs": {
            "title": title,
            "tags": ",".join(tags),
            "tier": str(tier),
            "content": content
        }
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(payload))

    if response.status_code != 204:
        raise Exception(f"GitHub dispatch failed: {response.status_code}\n{response.text}")
