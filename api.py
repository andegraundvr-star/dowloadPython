from datetime import date
import httpx


class API:
    def __init__(self, client: httpx.AsyncClient) -> None:
        self.client = client


    async def get_problems_codes(self, token: str):
        """Получение коды проблем"""
        headers = {"User-Agent": "", "Authorization": f"Bearer {token}"}
        response: httpx.Response = await self.client.get(url="/problems/codes", headers=headers)
        if response.status_code == 200:
            return response.json()
        return response.text
    
    async def get_merchandisers(self, token: str):
        """Получение коды проблем"""
        headers = {"User-Agent": "", "Authorization": f"Bearer {token}"}
        response: httpx.Response = await self.client.get(url="/merchandisers", headers=headers)
        if response.status_code == 200:
            return response.json()
        return response.text

    async def post_merchandisers_schedules(self, token: str, dt: date, shop_code: str):
        """Загрузка графиков посещения мерчандайзеров"""
        headers = {"User-Agent": "", "Authorization": f"Bearer {token}"}
        data = {
            "schedules": [
                {
                    "date": str(dt),
                    "shop_code": str(shop_code),
                    "shop_name": "string",
                    "merch_name": "string",
                    "merch_phone": "string",
                    "duration": 0,
                    "agency": "string",
                    "gr20": "string"
                }
            ]
        }
        response: httpx.Response = await self.client.post(url="/merchandisers/schedules", headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        return response.text
    
    
    async def delete_merchandisers_schedules(self, token: str, dt: date, shop_code: str):
        """Удаление графиков посещения мерчандайзеров. Будут удалены все графики соответствующие дате и коду магазина"""
        headers = {"User-Agent": "", "Authorization": f"Bearer {token}"}
        response: httpx.Response = await self.client.delete(url=f"/merchandisers/schedules/{str(dt)}/{str(shop_code)}", headers=headers)
        if response.status_code == 200:
            return response.json()
        return response.text

    async def get_signals(self, token: str, dt: date, limit: int, offset: int):
        """Получение сигналов"""
        headers = {"User-Agent": "", "Authorization": f"Bearer {token}"}
        params = {"limit": limit, "offset": offset}
        response: httpx.Response = await self.client.get(url=f"/signals/{str(dt)}", params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        return response.text

    # сюда можете добавить остальное запросы из API_BASE_URL/docs