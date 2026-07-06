import os
import urllib.parse


def youtube_search(query):
    query = query.strip()

    if not query:
        return "Kya play karna hai?"

    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)

    os.system(
        f'am start -a android.intent.action.VIEW -d "{url}"'
    )

    return f"{query} YouTube par search kar rahi hoon."
