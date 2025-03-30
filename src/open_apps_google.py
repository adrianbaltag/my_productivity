"""Open a list of URLs in the default web browser with a delay between each one."""

import asyncio
import webbrowser

my_urls = [
    "https://www.google.com/search?q=python+programming",
    "https://www.youtube.com/",
    "https://www.linkedin.com/",
    "https://www.facebook.com/",
    "https://www.instagram.com//",
]


async def open_urls(urls):
    """Open a list of URLs in the default web browser with a delay between each one.
    Args:
        urls (list): List of URLs to open.

    """

    for url in urls:
        # open the url in a new webbrowser
        webbrowser.open_new(url)
        # webbrowser.open(url)
        await asyncio.sleep(1)  #  wait 1s before opening the next URL


if __name__ == "__main__":
    asyncio.run(open_urls(my_urls))
