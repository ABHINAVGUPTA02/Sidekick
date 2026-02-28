from dotenv import load_dotenv

load_dotenv(override=True)

from tools.push_notification_tool import push_notification_tool

def main():
    push_notification_tool("Hello from sidekick!")


if __name__ == "__main__":
    main()
