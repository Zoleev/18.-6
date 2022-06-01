import requests
import json
from extensions import keys


class ApiExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ApiExeption(f'Вы ввели одну и ту же валюту {base} /help')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ApiExeption(f'Неверно указана валюта {quote} /help')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ApiExeption(f'Неверно указана валюта {base} /help')
        try:
            amount = float(amount)
            if amount <= 0:
                raise ApiExeption(f'Введите количество больше нуля {amount} /help')
        except ValueError:
            raise ApiExeption(f'Введите количество цифрой {amount} /help')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount
        return total_base


