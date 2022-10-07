import json
import requests
from config import keys

class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        try:
            quote_low = keys[quote.lower()]
        except KeyError:
            raise ConvertionException(f"Не распознана валюта {quote}")

        try:
            base_low = keys[base.lower()]
        except KeyError:
            raise ConvertionException(f"Не распознана валюта {base}")

        if quote_low == base_low:
            raise ConvertionException("Невозможно перевести одинаковые валюты")


        if quote == base:
            raise ConvertionException("Невозможно перевести одинаковые валюты")

        # try:
        #     quote_ticker = keys[quote]
        # except KeyError:
        #     raise ConvertionException(f"Не распознана валюта {quote}")
        #
        # try:
        #     base_ticker = keys[base]
        # except KeyError:
        #     raise ConvertionException(f"Не распознана валюта {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не распознано количество {amount}")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_low}&tsyms={base_low}")
        total_base = json.loads(r.content)[keys[base]]\


        return total_base



