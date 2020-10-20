from bs4 import BeautifulSoup


def viewers_from_html(htmlpath):
    with open(htmlpath) as f:
        text = f.readlines()
    text = "".join(text)

    soup = BeautifulSoup(text, "html.parser")
    rows = soup.findAll("p", class_="sc-fzoiQi iRvkjU")
    print([row.string for row in rows])


if __name__ == "__main__":
    viewers_from_html("web_scraper/strike.html")