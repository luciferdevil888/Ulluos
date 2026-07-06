import os
import urllib.parse


def open_website(site):
    url = site.strip()

    if not url.startswith("http"):
        url = "https://" + url

    os.system(
        f'am start -a android.intent.action.VIEW -d "{url}"'
    )

    return f"{site} open kar rahi hoon."


def google_search(query):
    url = "https://www.google.com/search?q=" + urllib.parse.quote(query)

    os.system(
        f'am start -a android.intent.action.VIEW -d "{url}"'
    )

    return f"{query} Google par search kar rahi hoon."
