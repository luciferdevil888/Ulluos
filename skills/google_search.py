import os
import urllib.parse


def google_search(query):
    query = query.strip()

    if not query:
        return "Kya search karna hai?"

    url = "https://www.google.com/search?q=" + urllib.parse.quote(query)

    os.system(
        f'am start -a android.intent.action.VIEW -d "{url}"'
    )

    return f"{query} Google par search kar rahi hoon."
