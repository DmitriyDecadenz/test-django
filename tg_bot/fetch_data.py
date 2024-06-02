from json import JSONDecodeError
import httpx


class ParseData:
    def __init__(self) -> None:
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

    async def get_transaction_by_id_json_list(self, transaction_id: int):
        response = httpx.get(f'{self.url}/transaction/{transaction_id}/?format=json')
        if response.status_code == 204:
            return None
        try:
            items_info = response.json()
        except JSONDecodeError:
            return None
        return items_info

    async def get_users_transactions_json_list(self, user_id: int) -> list[dict] | None:
        response = httpx.get(f'{self.url}/user/transactions/?forman=json&user={user_id}')
        if response.status_code == 204:
            return None
        try:
            items_info = response.json()
        except JSONDecodeError:
            return None
        return items_info
