from dotenv import load_dotenv

load_dotenv(override=True)

import asyncio
import textwrap

from tools.push_notification_tool import push_notification_tool
from tools.playwright_tools import get_playwright_tools

# async def run_playwright_tools():
#     tools = await get_playwright_tools()
#     tool_dict = {tool.name:tool for tool in tools}

#     navigate_tool = tool_dict.get("navigate_browser")
#     extract_text_tool = tool_dict.get("extract_text")

        
#     await navigate_tool.arun({"url": "https://en.wikipedia.org/wiki/The_Beatles"})
#     text = await extract_text_tool.arun({})
#     return textwrap.fill(text)

def main():
    # push_notification_tool("Hello from sidekick!")
    
    # text = asyncio.run(run_playwright_tools())
    # print(textwrap.fill(text))
    print("Hello from sidekick!")

if __name__ == "__main__":
    main()
