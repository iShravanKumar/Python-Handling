import requests
import pandas
import matplotlib.pyplot as plt
from log_generator import logging

# API Documentation - https://www.coingecko.com/en/api/documentation

strReq = 'https://api.coingecko.com/api/v3/search/trending'
response = requests.get(strReq)
trendResp = response.json()
trending_dataframe = pandas.DataFrame()
for x in trendResp.values():
    for y in x:
        ID = (y['item']['id'])
        strReq = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=inr".format(ID)
        response = requests.get(strReq)
        temp_response = response.json()
        cPrice = (temp_response[(y['item']['id'])]['inr'])
        strReq = 'https://api.coingecko.com/api/v3/coins/{}/market_chart?vs_currency=INR&days=30'.format(ID)
        response = requests.get(strReq)
        temp_response = response.json()
        temp_list = []
        for i in temp_response['prices']:
            temp_list.append(i[1])
        temp = {'ID': ID, 'Name': (y['item']['name']), 'Symbol': (y['item']['symbol']),
                'Price': cPrice, 'PriceHistory': temp_list}
        trending_dataframe = pandas.concat([trending_dataframe, pandas.DataFrame([temp])], ignore_index=True)
        logging.debug("trendDF for {}".format(ID), trending_dataframe)


def barchart(xax, yax, labels):
    """
    Displays a bar graph plotting the function parameters

    :param xax: XAxis Values, Iterable object
    :param yax: YAxis Values, Iterable object
    :param labels: Tick Labels, Iterable object
    :return: None
    """
    trending_dataframe.plot.bar()
    plt.bar(xax, yax, tick_label=labels)
    plt.xlabel("CRYPTO")
    plt.ylabel("PRICE (INR)")
    plt.title('Price of Trending Cryptos')
    plt.yscale("log")
    plt.show()


def linechart(df):
    """
    Display a line graph plotting the iterable objects in a ndarray

    :param df: ndarray with labels and associated iterable object for plotting
    :return: None
    """
    price_hsl = []
    for ind in df.index:
        sym = df['Symbol'][ind]
        price_hl = (df['PriceHistory'][ind])
        price_hsl.append(price_hl)
        plt.plot(list(range(0, len(price_hl))), price_hl, label=sym)
    plt.xlabel('HOURS')
    plt.ylabel('PRICE (INR)')
    plt.legend()
    plt.title('Price History of Trending Cryptos')
    plt.yscale("log")
    plt.show()


barchart(trending_dataframe['Symbol'], trending_dataframe['Price'], trending_dataframe['Symbol'])
linechart(trending_dataframe)
