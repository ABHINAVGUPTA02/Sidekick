import os
import requests

pushover_url = os.getenv("PUSHOVER_URL")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")

def push_notification(message: str):
    """Pushes a notification to the user"""
    if not pushover_url or not pushover_token or not pushover_user:
        raise ValueError(
            "Pushover config missing. Set PUSHOVER_URL, PUSHOVER_TOKEN, and PUSHOVER_USER in .env"
        )
    requests.post(pushover_url, data={"token": pushover_token, "user": pushover_user, "message": message})