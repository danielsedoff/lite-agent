import asyncio
from playwright.async_api import async_playwright
from submodules.generate_url import generate_url
from submodules.args_as_text import args_as_text

async def run(playwright):

    user_input = args_as_text()
    url = generate_url(user_input)

#   browser = await playwright.chromium.launch() # ...launch(headless=False)
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
