import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup


class UkrgasBang:
    def __init__(self, bank_name, url, currencies):
        self.bank_name = bank_name
        self.url = url
        self.currencies = currencies

    def get_bank_name(self):
        return self.bank_name

    @staticmethod
    def get_session():
        connection = requests.session()
        return connection

    def get_proxy_session(self):
        proxy_session = self.get_session()
        proxy_session.proxies = {
            'http': '',  # Enter your proxy setting here for HTTP
            'https': ''  # HTTPS
        }
        # Check requesting ip address
        print(proxy_session.get('http://ip.42.pl/raw').text)
        return proxy_session.get(self.url)

    def get_html(self):
        request = self.get_session()
        return request.get(self.url)

    def CurrencyParser(self):
        html = self.get_html()

        try:
            print(f'Get response code: {html}')
        except ConnectionError as error:
            print(f'Check your Internet Connection! \n\t{error}')

        # Start Parsing
        soup = BeautifulSoup(html.text, 'lxml')
        main_rate_table = soup.find_all('td', class_='val')
        currency_rate = [main_rate_table[idx].text for idx in range(len(main_rate_table))]

        return currency_rate

    def converter(self, parse_return):
        buy = parse_return[0::3]
        sell = parse_return[1::3]

        res = {
            'currency': '',
            'buy': '',
            'sell': '',
        }

        for idx in range(len(self.currencies)):
            res['currency'] = self.currencies[idx]
            res['buy'] = buy[idx]
            res['sell'] = sell[idx]
            print(res)


if __name__ == '__main__':
    print('Launching main script...')
    bank = UkrgasBang(bank_name='UkrGasBank', url='https://www.ukrgasbank.com/kurs/', currencies=('USD', 'EUR', 'RUB',
                                                                                                  'CHF', 'PLN', 'GBP'))
    print(bank.get_bank_name())
    list = bank.CurrencyParser()
    bank.converter(parse_return=list)
