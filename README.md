PandasTA
========

This is a script to do technical analysis on stock data from Yahoo Finance.

It use python-pandas to read historical stock data, 
and then use TA-lib to calculate several essential technical analysis indicators.

The input is simple list of ticker names.
The output is pandas' panel data structure which contains all relevant information.

## TA inductors
1. SMA - simple moving average
2. BB_upper, BB_center, BB_lower - bollinger bands 
3. BB_per, BB_width - bollinger bands percentage and width
4. CCI - Commodity Channel Index
5. MACD, MACD_signal, MACD_hist - Moving Average Convergence/Divergence
6. MFI - Money Flow Index
7. MOM - Momentum
8. RSI - Relative Strength Index
9. Will - Williams' %R
10. DCPeriod, DCPhase - Hilbert Transform - Dominant Cycle Period and Phase

# requirements
1. pandas
2. TA-Lib

# Example 
	tickers = ['AAPL', "AMZN", "SOHU", "WMT"]
	panel = load(tickers)
	print panel
	print panel.minor_xs('AAPL')[['Close', 'BB_per', "MACD_Hist"]].tail()


	<class 'pandas.core.panel.Panel'>
	Dimensions: 22 (items) x 126 (major_axis) x 4 (minor_axis)
	Items axis: Open to DCPhase
	Major_axis axis: 2013-07-22 00:00:00 to 2014-01-17 00:00:00
	Minor_axis axis: AAPL to WMT

				Close    BB_per  MACD_Hist
	Date                                   
	2014-01-13  535.73  0.362429  -3.609874
	2014-01-14  546.39  0.864649  -2.604802
	2014-01-15  557.36  0.931808  -1.143649
	2014-01-16  554.25  0.729639  -0.369175
	2014-01-17  540.67  0.308106  -0.733028