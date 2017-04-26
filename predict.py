'''
function pull_data downloads currency exchange rates
inputs:
	string, currency code: a three- letter currency code (ISO 4217 standard)
	string, a number determining how many weeks back the linear extrapolation is calculated from
output:
	list, currency exchange rate for a particular currency for last X days


function linear_extrapolation uses linear extrapolation to calculate future exchange rate
inputs:
	currency_code, string, A week in the future for which we count the exchange rate (plus predict_week)
	recent_days, string, currency code: a three- letter currency code (ISO 4217 standard)
	predict_week, string, a number determining how many weeks back the linear extrapolation is calculated from
output:
	float, currency exchange rate for next X week
'''

#requirement scikit-learn, matplotlib - optional

#Data in nbp api is splited into 2 tables
table_A = ['THB', 'USD', 'AUD', 'HKD', 'CAD', 'NZD', 'SGD', 'EUR', 'HUF', 'CHF', 'GBP', 'UAH', 'JPY', 'CZK', 'DKK', 'ISK', 'NOK', 'SEK', 'HRK', 'RON', 'BGN', 'TRY', 'ILS', 'CLP', 'PHP', 'MXN', 'ZAR', 'BRL', 'MYR', 'RUB', 'IDR', 'INR', 'KRW', 'CNY', 'XDR']

table_B = ['AFN', 'MGA', 'PAB', 'ETB', 'VEF', 'BOB', 'CRC', 'SVC', 'NIO', 'GMD', 'MKD', 'DZD', 'BHD', 'IQD', 'JOD', 'KWD', 'LYD', 'RSD', 'TND', 'MAD', 'AED', 'STD', 'BSD', 'BBD', 'BZD', 'BND', 'FJD', 'GYD', 'JMD', 'LRD', 'NAD', 'SRD', 'TTD', 'XCD', 'SBD', 'VND', 'AMD', 'CVE', 'AWG', 'BIF', 'XOF', 'XAF', 'XPF', 'DJF', 'GNF', 'KMF', 'CDF', 'RWF', 'EGP', 'GIP', 'LBP', 'SDG', 'SYP', 'GHS', 'HTG', 'PYG', 'ANG', 'PGK', 'LAK', 'MWK', 'ZMW', 'AOA', 'MMK', 'GEL', 'MDL', 'ALL', 'HNL', 'SLL', 'SZL', 'LSL', 'AZN', 'MZN', 'NGN', 'ERN', 'TWD', 'PEN', 'MRO', 'TOP', 'MOP', 'ARS', 'DOP', 'COP', 'UYU', 'BWP', 'GTQ', 'IRR', 'YER', 'QAR', 'OMR', 'SAR', 'KHR', 'BYN', 'LKR', 'MVR', 'MUR', 'NPR', 'PKR', 'SCR', 'KGS', 'TJS', 'UZS', 'KES', 'SOS', 'TZS', 'UGX', 'BDT', 'WST', 'KZT', 'MNT', 'VUV', 'BAM']


import json, requests
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


def pull_data(currency_code, days):
  if currency_code in table_A:
    table_type = "A"
  if currency_code in table_B:
    table_type = "B"
  else:
    print ("Wrong currency")
  response = requests.get("http://api.nbp.pl/api/exchangerates/rates/{}/{}/last/{}?format=json".format(table_type, currency_code, days)).json()
  data = []
  for rates in response["rates"]:
    data.append(rates["mid"])
  return data

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

def linear_extrapolation(currency_code, recent_days, predict_week):
  x = np.array(list(range(0, int(recent_days))))
  y = pull_data(currency_code, recent_days)
  model = LinearRegression()
  model.fit(x.reshape(len(x), 1), y)
#  To plot data
#  coeff = model.coef_
#  print (coeff)
#  plt.scatter(x, y, color='b')
#  plt.scatter(predict_week, model.predict(predict_week), color='r')
#  plt.show()
  return model.predict(predict_week)

#testing 
print (linear_extrapolation("SZL", "10", 12))



