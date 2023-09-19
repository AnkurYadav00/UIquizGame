import requests

AMOUNT = 10
TYPE = "boolean"
OPEN_TRIVIA_API_ENDPOINT = f"https://opentdb.com/api.php"


class fetch_questions:
    def __init__(self):
        self.question_data = []
        self.parameters = {
            "amount": AMOUNT,
            "type": TYPE
        }

    def questions(self):
        response = requests.get(url=OPEN_TRIVIA_API_ENDPOINT, params=self.parameters)
        response.raise_for_status()
        self.question_data = response.json()['results']
