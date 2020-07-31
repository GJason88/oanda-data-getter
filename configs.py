# Your Oanda API Key
API_KEY = 'Bearer YOUR KEY HERE'

HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
    }
    
# format: Currency1_Currency2
INSTRUMENT = 'EUR_USD'

# e.g. 'S5', 'M15', 'H1', 'D', 'W', 'M'
# https://developer.oanda.com/rest-live-v20/instrument-df/ for full options
GRANULARITY = 'M15'

# format: '2016-06-01T15:00:00.000000000Z'
# leave None if using COUNT
FROM_DATE = None

# format: '2016-10-17T15:00:00.000000000Z'
# leave None for present time
TO_DATE = None

# (1 - 5000) must be in quotes e.g. '100'
# leave None if using dates, else fill with number of past candlesticks you want up to present time
COUNT = '100'

# 'practice' or 'trade'
ACCOUNT_TYPE = 'practice'


# DO NOT EDIT
PARAMS = {
    'from': FROM_DATE,
    'to': TO_DATE,
    'count': COUNT,
    'granularity': GRANULARITY
}