from web_scraper.leeds_digital_festival import (
    soup_from_html,
    extract_event_data,
)

HTML_FILE = "web_scraper/all_leeds_events.html"


if __name__ == "__main__":
    s = soup_from_html(HTML_FILE)
    df = extract_event_data(s)
    df.to_csv("formatted_events.csv", index=False)