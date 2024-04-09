from celery import shared_task
from time import sleep
import requests
from bs4 import BeautifulSoup
from new_app.models import OlxHome
import logging

logger = logging.getLogger(__name__)

@shared_task()
def get_data_from_olx():
    html = requests.get("https://www.olx.uz/nedvizhimost/kvartiry/prodazha/").text
    soup = BeautifulSoup(html, "html.parser")

    homes = soup.find(attrs={"class": "listing-grid-container"})
    logger.info("Starts")
    logger.info(homes)
    for home in homes.find_all(attrs={"type": "list"}):
        app = OlxHome.objects.create(
            name = home.text,
        )
        logger.info(home.findChildren()[1].text.strip())

