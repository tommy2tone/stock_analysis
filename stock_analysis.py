import datetime as dt
import mplfinance as mpf
import pandas as pd
import pandas_datareader.data as web
import yfinance as yfin

yfin.pdr_override()

ticker = input('Enter ticker ID:  ')

start = input('Enter start date (YYYY-MM-DD): ')
end = input('Enter end date (YYYY-MM-DD): ')

# start = dt.datetime(2020, 1, 1)
# end = dt.datetime(2020, 3, 17)

df = web.get_data_yahoo(ticker, start, end)
df.to_csv('{}.csv'.format(ticker))
df = pd.read_csv('{}.csv'.format(ticker), parse_dates=True, index_col=0)


kwargs = dict(type='candle',
              mav=(20, 50),
              volume=True,
              figscale=0.8,
              title='\n{}'.format(ticker),
              ylabel='Price',
              ylabel_lower='Volume',
              style='yahoo')

# apdict = mpf.make_addplot(df['Low'])
mpf.plot(df, **kwargs)
