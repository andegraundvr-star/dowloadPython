import asyncio
from datetime import datetime, timezone
import os
from pathlib import Path

import dotenv
import httpx
from api import API
from keycloak_app import Token


async def main(base_url: str, cert_path: str, token_obj: Token) -> None:
    """Пример GET, POST и DELETE запросов (limit - сколько сигналов, offset - с какого по счету начать)

    Подробнее в https://api-merch.magnit.ru/docs или https://api-merch.magnit.ru/redoc
    """
    async with httpx.AsyncClient(base_url=base_url, verify=cert_path) as client:
        api = API(client=client)
        token: str = await token_obj.get_token()
        
        date_of_visit_shop = datetime.now(tz=timezone.utc).date()
        shop_code = "111111"
        
        print(await api.get_problems_codes(token=token))
        print(await api.get_signals(token=token, dt=date_of_visit_shop, limit=10, offset=0))
        print(await api.post_merchandisers_schedules(token=token, dt=date_of_visit_shop, shop_code=shop_code))
        await asyncio.sleep(5)
        print(await api.get_merchandisers(token=token))
        print(await api.delete_merchandisers_schedules(token=token, dt=date_of_visit_shop, shop_code=shop_code))



if __name__ == "__main__":
    # Заполните .env, установить зависимости, затем запустите main.py

    BASE_DIR = Path(__file__).resolve().parent
    dotenv.load_dotenv(BASE_DIR / ".env", override=True)

    asyncio.run(
        main(
            base_url=str(os.getenv("API_BASE_URL")),
            cert_path=str(os.getenv("CERT_PATH")),
            token_obj=Token(
                filename="api_merch_token.json",
                client_id=str(os.getenv("CLIENT_ID")),
                client_secret=str(os.getenv("CLIENT_SECRET")),
                base_url=str(os.getenv("KEYCLOAK_BASE_URL")),
                realm=str(os.getenv("KEYCLOAK_REALM"))
            ),
        ),
    )