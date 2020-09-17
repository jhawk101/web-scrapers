from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt



"""
Would need to work out login or oauth2 for this:

url = "https://flow.polar.com/training/analysis/5130593026"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
"""


def average_speeds_from_html(htmlpath):
    with open(htmlpath) as f:
        text = f.readlines()
    text = "".join(text)

    soup = BeautifulSoup(text, "html.parser")
    rows = soup.findAll("div", class_="lap-row ManRowDiv")

    avg_speeds = [
        i.contents[9].string for i in rows if i.contents[3].string == "Work"
    ]
    avg_speeds = [float(i.split()[0]) for i in avg_speeds]

    print(
        f"Average speed for this training session was {sum(avg_speeds)/len(avg_speeds):0.2f}km.h"
    )
    
    fig, ax = plt.subplots()
    ax.plot(avg_speeds)
    plt.savefig("web_scraper/plots/fig.jpg")


average_speeds_from_html("web_scraper/polar_activity.html")
