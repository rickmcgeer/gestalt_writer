import os
import json
from write_gestalt import write_gestalt as run_write_gestalt

def write_gestalt(request):
    try:
        data = request.get_json()

        # Security check
        incoming_token = data.get("token")
        expected_token = os.environ.get("GITHUB_SECRET")
        if incoming_token != expected_token:
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
