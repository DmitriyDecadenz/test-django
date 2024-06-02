from json import JSONDecodeError

import httpx


class ParseWB:
    def __init__(self,) -> None:
        self.url: str = 'http://127.0.0.1:8000/api'

    async def get_transaction_json_list(self) -> list[dict] | None:
        response = httpx.get(f'{self.url}/transactions/?format=json')
        if response.status_code == 204:
            return None
        try:
            items_info = response.json()
        except JSONDecodeError:
            return None
        return items_info

    def get_users_transactions_json_list(self, user_id) -> list[dict] | None:
        response = httpx.get(f'{self.url}/transaction/{user_id}/?forman=json')
        if response.status_code == 204:
            return None
        try:
            items_info = response.json()
        except JSONDecodeError:
            return None
        return items_info


if __name__ == "__main__":
    app = ParseWB()
    print(app.get_users_transactions_json_list(2))