from hikkatl.types import Message
from .. import loader, utils
import aiohttp

@loader.tds
class TonPriceMod(loader.Module):
    """Показывает текущий курс TON к рублю"""
    strings = {"name": "TonPrice"}

    async def toncmd(self, message: Message):
        """Проверить текущий курс TON/RUB"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.kraken.com/0/public/Ticker?pair=TONRUB") as response:
                    data = await response.json()
                    price = float(data["result"]["TONRUB"]["c"][0])
                    await utils.answer(
                        message,
                        f"<b>💰 Курс TON/RUB:</b> <code>{price:.2f}</code>"
                    )
        except Exception as e:
            await utils.answer(
                message,
                f"<b>❌ Произошла ошибка:</b> <code>{str(e)}</code>"
            )