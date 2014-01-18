import pandas as pd
from pandas.io.data import DataReader
from datetime import datetime, timedelta
import talib

def load(tickers, start=datetime.now()-timedelta(days=180), 
			end=datetime.now()):
	"""load data from yahoo finance and do technique analysis

	Args:
		tickers (list) : list of valid stock tickers
		start (datetime) : historical data start date
		end (datetime) : historical data end date

	Returns:
		panel (pandas.panel) : a 3-dimensional data structure 
			Item axis : including Open, Close, High, Volume and 
			MACD, etc. TA indicators. 
			Major axis: historical datetime index
			minor axis: tickers
	"""
	panel = DataReader(tickers, "yahoo", start, end)
	panelCopy = panel.transpose(2, 1, 0, copy=True)
	smaDf = pd.DataFrame(index=panel.major_axis)
	BBUDf = pd.DataFrame(index=panel.major_axis)
	BBDDf = pd.DataFrame(index=panel.major_axis)
	BBMDf = pd.DataFrame(index=panel.major_axis)
	CCIDf = pd.DataFrame(index=panel.major_axis)
	MACDDf = pd.DataFrame(index=panel.major_axis)
	MACDSDf = pd.DataFrame(index=panel.major_axis)
	MACDHDf = pd.DataFrame(index=panel.major_axis)
	MFIDf = pd.DataFrame(index=panel.major_axis)
	MOMDf = pd.DataFrame(index=panel.major_axis)
	RSIDf = pd.DataFrame(index=panel.major_axis)
	StochSlowDf = pd.DataFrame(index=panel.major_axis)
	RSIDf = pd.DataFrame(index=panel.major_axis)
	WillDf = pd.DataFrame(index=panel.major_axis)
	HilbertPeriodDf = pd.DataFrame(index=panel.major_axis)
	HilbertPhaseDf = pd.DataFrame(index=panel.major_axis)

	for (t, df) in panelCopy.iteritems():
	    smaDf[t] = talib.SMA(df.Close)
	    BBUDf[t], BBMDf[t], BBDDf[t] = talib.BBANDS(df.Close)
	    CCIDf[t] = talib.CCI(df.High, df.Low, df.Close)
	    MACDDf[t], MACDSDf[t], MACDHDf[t] = talib.MACD(df.Close)
	    MFIDf[t] = talib.MFI(df.High, df.Low, df.Close, df.Volume)
	    MOMDf[t] = talib.MOM(df.Close)
	    RSIDf[t] = talib.RSI(df.Close)
	    WillDf[t] = talib.WILLR(df.High, df.Low, df.Close)
	    HilbertPeriodDf[t] = talib.HT_DCPERIOD(df.Close)
	    HilbertPhaseDf[t] = talib.HT_DCPHASE(df.Close)
	    
	    
	panel['SMA'] = smaDf
	panel['BB_upper'] = BBUDf
	panel['BB_center'] = BBMDf
	panel['BB_lower'] = BBDDf
	panel['BB_per'] = (panel.Close - panel.BB_lower) / (
						panel.BB_upper - panel.BB_lower)
	panel['BB_width'] = (panel.BB_upper - panel.BB_lower) / panel.BB_center
	panel['CCI'] = CCIDf
	panel['MACD'] = MACDDf
	panel['MACD_signal'] = MACDSDf
	panel['MACD_hist']= MACDHDf
	panel['MFI'] = MFIDf
	panel['MOM'] = MOMDf
	panel['RSI'] = RSIDf
	panel['Will'] = WillDf
	panel['DCPeriod'] = HilbertPeriodDf
	panel['DCPhase'] = HilbertPhaseDf
	return panel

if __name__ == '__main__':
	tickers = ['AAPL', "AMZN", "SOHU", "WMT"]
	panel = load(tickers)
	print panel
	print panel.minor_xs('AAPL')[['Close', 'BB_per', "MACD_hist"]].tail()
