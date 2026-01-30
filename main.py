import os
import json
from github_writer import run_write_gestalt

def main(request):
    try:
        if request.method == 'GET':
            return ('OK', 200)
        
        data = request.get_json()

        # Security check
        api_key = request.headers.get('Authorization')
        expected_token = os.environ.get("GITHUB_SECRET")
        expected = f"Bearer {expected_token}"
        
        if api_key != expected:
            return ("Unauthorized", 403)

        # Extract gestalt data
        title = data["title"]
        tags = data["tags"]
        tier = data["tier"]
        content = data["content"]

        run_write_gestalt(title, tags, tier, content)

        return ("Gestalt committed", 200)

    except Exception as e:
        return (f"Error: {str(e)}", 500)
