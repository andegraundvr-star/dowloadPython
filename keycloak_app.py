import json
from datetime import datetime, timezone
from typing import Optional
import jwt
import aiofiles
import anyio
import httpx


class Token:
    def __init__(
            self, filename: str, client_id: str, client_secret: str, base_url: str, realm: str,
    ) -> None:
        self.token = None
        self.expired_timestamp = None
        self.filename = filename
        self.client_id = client_id
        self.client_secret = client_secret
        self.openid_url = f"{base_url}/auth/realms/{realm}/.well-known/openid-configuration"


    async def _is_token_valid(self) -> bool:
        """Проверка что токен сохраненный в памяти валидный"""
        timestamp_now = int(datetime.now(tz=timezone.utc).timestamp())
        return self.expired_timestamp and self.expired_timestamp > timestamp_now + 20


    async def _read_token_from_file(self, filename: str) -> Optional[str]:
        """Достаем токен из файла если токен существует и он валидный"""
        if await anyio.Path(filename).exists():
            async with aiofiles.open(filename) as file:
                content = json.loads(await file.read())
            if content.get("last_update", 0) > int(datetime.now(tz=timezone.utc).timestamp()) + 20:
                return content["token"]
        return None


    async def _fetch_new_token(self, client_id: str, client_secret: str, openid_url: str) -> str:
        """Запрос нового токена из KeyCloak"""
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(url=openid_url)
            response.raise_for_status()

            token_url = response.json().get("token_endpoint")
            data = {
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": "client_credentials",
            }
            response = await client.post(token_url, data=data)
            response.raise_for_status()

            return response.json().get("access_token")


    async def _save_token_to_file(self, filename: str) -> None:
        """Сохранение токена и expired_timestamp в файл"""
        async with aiofiles.open(filename, "w") as file:
            data = {"last_update": self.expired_timestamp, "token": self.token}
            await file.write(json.dumps(data, indent=4, ensure_ascii=False))


    async def get_token(self) -> str:
        """
        Получаем токен. Последовательность:
        1) если токен сохранен в памяти и он валидный -> возвращаем из памяти
        2) если токен не сохранен в памяти или он не валидный, 
            то ищет его в файле -> если файл существует и токен в нем валидный -> возвращает из файла
        3) если файла не существует или токен в нем не валидный, 
            то запрашивает новый токен у Keycloak и обновляет его в файле, и в памяти -> возвращает из памяти
        """
        
        if await self._is_token_valid():
            return self.token

        token_from_file = await self._read_token_from_file(self.filename)
        if token_from_file:
            return token_from_file

        self.token = await self._fetch_new_token(self.client_id, self.client_secret, self.openid_url)
        self.expired_timestamp = jwt.decode(self.token, options={"verify_signature": False})['exp']
        await self._save_token_to_file(self.filename)

        return self.token