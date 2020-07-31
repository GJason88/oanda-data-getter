import pandas as pd
import requests
from configs import HEADERS, PARAMS, ACCOUNT_TYPE, INSTRUMENT

def get_user_input():
    response = input('Enter "m" for mid pricing or "ba" for bid/ask pricing data\n')
    if (response == 'm'):
        export_mid_data()
    elif (response == 'ba'):
        export_ba_data()
    else:
        print('invalid input')
        get_user_input

def export_mid_data():
    try:
        r = requests.get("https://api-fx{}.oanda.com/v3/instruments/{}/candles?price=M".format(ACCOUNT_TYPE, INSTRUMENT), headers=HEADERS, params=PARAMS).json()
        df = pd.DataFrame(([candle['time'], candle['mid']['o'], candle['mid']['h'], candle['mid']['l'], candle['mid']['c'], candle['volume']] for candle in r['candles']), 
        columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
    
        df.to_csv('mid_data.csv', index=False)
        print('mid data exported to "mid_data.csv"')

    except:
        print('request failed, likely that candlestick count is out of range (max=5000)')    

def export_ba_data():
    try:
        r = requests.get("https://api-fx{}.oanda.com/v3/instruments/{}/candles?price=BA".format(ACCOUNT_TYPE, INSTRUMENT), headers=HEADERS, params=PARAMS).json()
        df = pd.DataFrame(([candle['time'], candle['bid']['o'], candle['bid']['h'], candle['bid']['l'], candle['bid']['c'], 
        candle['ask']['o'], candle['ask']['h'], candle['ask']['l'], candle['ask']['c'], candle['volume']] for candle in r['candles']), 
        columns=['Time', 'Open Bid', 'High Bid', 'Low Bid', 'Close Bid', 'Open Ask', 'High Ask', 'Low Ask', 'Close Ask', 'Volume'])
        
        df.to_csv('bid_ask_data.csv', index=False)
        print('bid/ask data exported to "bid_ask_data.csv"')

    except:
        print('request failed, likely that candlestick count is out of range (max=5000)')

get_user_input()