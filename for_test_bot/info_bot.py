import json
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import requests
TOKEN = "1757954563:AAGY3vNTo9gpwaBG28kXPciXLMsaklp9e-U"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"

# telegram bot
def make_request(method: str, params: dict = None):
    res = requests.get(f"{BASE_URL}{method}", params=params)
    print(res.url)
    return res.json()


def get_updates(offset: int = 0):
    return make_request("getUpdates", {"offset": offset})["result"]

def make_button():
    keyboard = []
    keyboard.append(
        [

            {
                "text":"📍Manzilimiz",
            },
            {
                "text": "☎️Contact",
            },
            {
                "text": "Biz haqimizda",
            }
        ]
    )

    markup = {"keyboard": keyboard}
    print(markup)
    return json.dumps({"keyboard":keyboard})

def reply_parametr(message_id, chat_id):
    js = {
        "message_id":message_id,
        "chat_id":chat_id,
        # "quote":"afadfdsfdsfdsf"
    }
    return json.dumps(js)

def send_media():
    keyboard = []
    print(os.path)
    keyboard.append(
        {
            "type": "photo",
            "media": f"https://images.app.goo.gl/EHomh4ai2dbWrFQz9",
            # "media": f"{BASE_DIR}.jpg",
        },
    )
    keyboard.append(
        {
            "type": "photo",
            "media": f"https://images.pexels.com/photos/2893685/pexels-photo-2893685.jpeg?auto=compress&cs=tinysrgb&w=800",
            # "media": f"{BASE_DIR}.jpg",
        },
    )
    js = {
        "media": keyboard
    }
    print(keyboard)
    return json.dumps(keyboard)

def main():
    keyboard = [['ES', 'EN']]
    offset = 0
    while True:
        updates = get_updates(offset)
        for update in updates:
            offset = update["update_id"] + 1
            try:
                if update["message"]:
                    text = update["message"]["text"]
                    if text == "/start":
                        make_request(
                            "sendMessage",
                            {
                                "chat_id": update["message"]["chat"]["id"],
                                "text": "Assalomu alaykum hush kelibsiz!",
                                "reply_markup": make_button(),
                                "resize_keyboard": json.dumps(True)
                            },
                        )
                    elif text == "/help":
                        make_request(
                            "sendMessage",
                            {
                                "chat_id": update["message"]["chat"]["id"],
                                "text": "/start\n/help",
                            },
                        )
                    elif text == "📍Manzilimiz":
                        make_request(
                            "sendLocation",
                            {
                                "chat_id": update["message"]["chat"]["id"],
                                "latitude": "41.34126041568732",
                                "longitude": "69.26746784988445",
                                "reply_parameters": reply_parametr(update["message"]["message_id"], update["message"]["chat"]["id"]),
                            },
                        )
                        make_request(
                            "sendMessage",
                            {
                                "chat_id": update["message"]["chat"]["id"],
                                "text": "ул. Адхам Рахмат, Шайхонтахурский р-н, 15/1, Toshkent, Oʻzbekiston",
                            },
                        )
                    elif text == "☎️Contact":
                        make_request(
                            "sendContact",
                            {
                                "chat_id": update["message"]["chat"]["id"],
                                "phone_number": "+998990922697",
                                "first_name": "Murod",
                                "last_name": "Turaev",
                                "vcard": "UIC group IT kompaniyasi qabulxonasi",
                                "reply_parameters": reply_parametr(update["message"]["message_id"], update["message"]["chat"]["id"])
                            },
                        )
                        make_request(
                            "sendMessage",
                            {
                                "chat_id": update["message"]["chat"]["id"],
                                "text": "UIC group IT kompaniyasi qabulxonasi",
                            },
                        )
                    elif text == "Biz haqimizda":
                        # make_request(
                        #     "sendPhoto",
                        #     {
                        #         "chat_id": update["message"]["chat"]["id"],
                        #         "photo": f"https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGhvdG98ZW58MHx8MHx8fDA%3D",
                        #     },
                        # )
                        make_request(
                            "sendMediaGroup",
                            {
                                "chat_id": update["message"]["chat"]["id"],
                                "media": send_media(),
                                "reply_parameters": reply_parametr(update["message"]["message_id"], update["message"]["chat"]["id"])
                            },
                        )
                        make_request(
                            "sendMessage",
                            {
                                "chat_id": update["message"]["chat"]["id"],
                                "text": "UIC group IT kompaniyasining galeriyasi",
                            },
                        )
                    else:
                        make_request(
                            "sendMessage",
                            {
                                "chat_id": update["message"]["chat"]["id"],
                                "media": "Xatolik!",
                            },
                        )

            except Exception as e:
                print(e)
                pass

if __name__ == "__main__":
    main()