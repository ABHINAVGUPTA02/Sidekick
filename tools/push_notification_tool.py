# This is a tool that is used to push notifications to the user
from utils.push_notification import push_notification

def push_notification_tool(message: str):
    print(f"Pushing notification: {message} from tool")
    push_notification(message)
    return "Notification pushed successfully"