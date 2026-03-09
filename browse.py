import asyncio
from playwright.async_api import async_playwright
from generate_url import generate_url
import sys

async def run(playwright):

    user_input = " ".join(sys.argv[1:])

    if not user_input.strip():
        print("No commandline arguments. Query is expected in commandline arguments.")
        print("arg0: clear -- clear context and quit.")
        sys.exit()

    url = generate_url(user_input)

#    browser = await playwright.chromium.launch() # ...launch(headless=False)
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto(url)
    print(await page.title())

    links = await page.locator("a").evaluate_all(
        "elements => elements.map(el => el.href)"
    )

    for link in links:
        print(link)

    await context.close()
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == "__main__":
    asyncio.run(main())
