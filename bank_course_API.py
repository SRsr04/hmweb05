import aiohttp


class PrivatBankApi:
    BASE_URL = "https://api.privatbank.ua/p24api"

    async def get_exchange_rate(self, date):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.BASE_URL}/pubinfo?json&exchange&coursid=5"
            ) as response:
                data = await response.json()
                return self.parse_exchange_rate(data, date)

    def parse_exchange_rate(self, data, date):
        result = {}
        for currency in data:
            code = currency["ccy"]
            result[code] = {
                "sale": float(currency["sale"]),
                "purchase": float(currency["buy"]),
            }
        return {date: result}
