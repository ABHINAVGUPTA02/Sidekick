import nest_asyncio
nest_asyncio.apply()

from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser

async def get_playwright_browser():
    return create_async_playwright_browser(headless=False)

async def get_playwright_tools():
    async_browser = await get_playwright_browser()
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
    return toolkit.get_tools()
