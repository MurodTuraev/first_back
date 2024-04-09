import requests
TOKEN = "1757954563:AAGY3vNTo9gpwaBG28kXPciXLMsaklp9e-U"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"


# telegram bot
def make_request(method: str, params: dict = None):
    res = requests.get(f"{BASE_URL}{method}", params=params)
    return res.json()


def get_updates(offset: int = 0):
    return make_request("getUpdates", {"offset": offset})["result"]


def main():
    offset = 0
    while True:
        updates = get_updates(offset)
        for update in updates:
            print(update)
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
                    else:
                        make_request(
                            "sendMessage",
                            {
                                "chat_id": update["message"]["chat"]["id"],
                                "text": "Xatolik!",
                            },
                        )
                    # make_request(
                    #     "sendMessage",
                    #     {
                    #         "chat_id": update["message"]["chat"]["id"],
                    #         "text": update["message"]["text"],
                    #     },
                    # )
            except:
                pass


if __name__ == "__main__":
    main()