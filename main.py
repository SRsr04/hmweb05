import asyncio
from datetime import date, timedelta
from bank_course_API import PrivatBankApi
from show_cur import CurrencyPrinter


class CurrencyFetcher:
    def __init__(self):
        self.api = PrivatBankApi()
        self.printer = CurrencyPrinter()

    async def fetch_currency_for_days(self, days):
        end_date = date.today()
        start_date = end_date - timedelta(days=days)

        results = []
        current_date = end_date
        while current_date >= start_date:
            formatted_date = current_date.strftime("%d.%m.%Y")
            result = await self.api.get_exchange_rate(formatted_date)
            results.append(result)
            current_date -= timedelta(days=1)

        return results


def main(days):
    fetcher = CurrencyFetcher()
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(fetcher.fetch_currency_for_days(days))

    printer = CurrencyPrinter()
    printer.print_results(results)


if __name__ == "__main__":
    main(2)
