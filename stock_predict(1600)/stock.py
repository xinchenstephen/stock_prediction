import requests
from bs4 import BeautifulSoup as bs
def get_stock_history_data(stock_code,stock_type):
    stock_url = 'http://quotes.money.163.com/trade/lsjysj_zhishu_{}.html'.format(stock_code)
    print(stock_url)
    headers = {
        'Referer':'http://quotes.money.163.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                     ' Chrome/74.0.3729.131 Safari/537.36'
    }
    respones = requests.get(stock_url,headers = headers).text
    print(respones)
    soup = bs(respones,'lxml')
    start_time = soup.find('input',{'name':'date_start_type'}).get('value').replace('-','')
    end_time = soup.find('input',{'name':'date_end_type'}).get('value').replace('-','')
    stock_code_new = stock_type + stock_code
    print(stock_code_new)
    download_url = "http://quotes.money.163.com/service/chddata.html?code={}&start={}&end={}&fields=TCLOSE;HIGH;LOW;TOPEN;TURNOVER;VOTURNOVER".format(stock_code_new, start_time, end_time)
    data = requests.get(download_url,headers = headers)
    with open('stock_data_{}.csv'.format(stock_code), 'wb') as f:
        for chunk in data.iter_content(chunk_size=10000):
            if chunk:
                f.write(chunk)
    print("{}数据已经下载完成".format(stock_code))


if __name__ == '__main__':
    get_stock_history_data('601601', '0')


