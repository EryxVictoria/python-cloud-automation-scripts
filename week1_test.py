import json

raw_log = '{"event": "UserLogin", "user": "admin", "status": "Failed"}'

try:
    data = json.loads(raw_log)
    if data.get("status") == "Failed":
        print(f"ALERT: Failed login detected for user '{data['user']}'.")
except json.JSONDecodeError as e:
    print(f"Error parsing log: {e}")