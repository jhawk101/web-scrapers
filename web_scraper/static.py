from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from tqdm import tqdm

EVENTS_URL = "https://leedsdigitalfestival.org/events/"


def static_scraper(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def soup_from_html(filepath):
    with open(filepath) as f:
        text = f.readlines()
    text = "".join(text)
    text = re.sub(" +", " ", text)
    text = re.sub("\n", "", text)
    soup = BeautifulSoup(text, "html.parser")
    return soup


def extract_event_data(beautSoup):
    h2 = beautSoup.findAll("h2")
    titles = [i.a.string for i in h2 if len(i.contents) == 3]
    links = [i.a.attrs["href"] for i in h2 if len(i.contents) == 3]

    h3 = beautSoup.findAll("h3")
    dates = [i.contents[0] for i in h3 if len(i) > 1]
    times = [i.contents[2].string for i in h3 if len(i) > 1]

    events = pd.DataFrame(
        data={
            "event_title": titles,
            "date": dates,
            "time": times,
            "link": links,
        }
    )

    categories = beautSoup.findAll("nav", class_="archive-event__categories")

    event_categories = []
    for event in categories:
        event_categories.append(
            [i.string for i in event.contents if i.string != " "]
        )

    events["categories"] = event_categories
    events["category_count"] = [len(i) for i in event_categories]
    events["primary_category"] = [i[0] for i in event_categories]

    return events


def add_event_descriptions():
    df = pd.read_csv("formatted_events.csv")
    df["description"] = None

    for index in tqdm(df.index):
        soup = static_scraper(df.link[index])
        content = soup.findAll("div", class_="standard-content")
        description = [i.string for i in content[0].contents if i != "\n"]
        df.loc[index, "description"] = str(description)

    df.to_csv("updated_events.csv", index=False)
