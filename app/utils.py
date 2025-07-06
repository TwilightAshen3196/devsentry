import httpx
import os

async def search_stackoverflow(error_message: str):
    query = error_message.replace(" ", "+")
    url = f"https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=relevance&q={query}&site=stackoverflow"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()
