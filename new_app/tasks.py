from celery import shared_task
from time import sleep
import requests
from bs4 import BeautifulSoup
from new_app.models import OlxHome

@shared_task()
def get_data_from_olx():
    html = requests.get("https://www.olx.uz/nedvizhimost/kvartiry/prodazha/").text
    soup = BeautifulSoup(html, "html.parser")

    homes = soup.select(".css-oukcj3 > .css-1sw7q4x > a > .css-qfzx1y > .css-1venxj6 > .css-1apmciz")

    for home in homes:
        app = OlxHome()
        app.name = home.findChildren()[1].text.strip()
        app.summHome=home.findChildren()[2].text.strip()
        app.accept=home.findChildren()[3].text.strip()
        app.save()
