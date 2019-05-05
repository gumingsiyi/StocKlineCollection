import tushare as ts
import time
ts.set_token('79d5bb96199b4f1b383ec349c52568ae3a1978bbbb427d141c930893')


# const var
PATH = ''


# 5min kline
def get_5min_data(stock_code, start_date):
    # get end date
    end_time = time.strftime('%Y-%m-%d')
    print(end_time)
    # get the data
    df = ts.get_hist_data(stock_code, ktype='5', end=end_time)
    print(df)
    return df


# get stock list
def get_stock_list():
    pro = ts.pro_api()
    data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name')
    # print(data)
    return data['symbol']


# the entrance of main function
def main():
    stock_list = get_stock_list()

    for stock_code in stock_list:
        # TODO find which date to start

        # get data
        df = get_5min_data(stock_code, '')
        print(df)
        time.sleep(0.5)

    # write data into file


if __name__ == '__main__':
    main()
