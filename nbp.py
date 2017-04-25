'''
class Nbp downloads currency exchange data from nbp web api http://api.nbp.pl/en.html

API Querry string parameters:
{table} – table type (A, B, or C)
	table A of middle exchange rates of foreign currencies,
	table B of middle exchange rates of foreign currencies,
	table C of buy and sell prices of foreign currencies;
{code} – a three- letter currency code (ISO 4217 standard)
{topCount} – a number determining the maximum size of the returned recent data series
{date}, {startDate}, {endDate} – a date in the YYYY-MM-DD format (ISO 8601 standard)
'''

import json, requests

class Nbp(object):
  def __init__(self, table):
    self.url = "http://api.nbp.pl/api/exchangerates"
    self.table_type = table
    self.response = 0
  def get_todays_data(self):
    self.response = requests.get("{}/tables/{}/today?format=json".format(self.url, self.table_type)).json()
  def get_latest_data(self, top_count):
    self.response = requests.get("{}/tables/{}/last/{}?format=json".format(self.url, self.table_type, top_count)).json()
  def get_data_for_a_specific_date(self, date):
    self.response = requests.get("{}/tables/{}/{}?format=json".format(self.url, self.table_type, date)).json()
  def get_data_from_specific_period(self, start_date, end_date):
    self.response = requests.get("{}/tables/{}/{}/{}?format=json".format(self.url, self.table_type, start_date, end_date)).json()

#queries for a paricular currency
  def get_todays_data_for_a_specific_currency(self, code):
    self.response = requests.get("{}/rates/{}/{}/today?format=json".format(self.url, self.table_type, code)).json()
  def get_latest_data_for_a_specific_currency(self, top_count, code):
    self.response = requests.get("{}/rates/{}/{}/last/{}?format=json".format(self.url, self.table_type, code, top_count)).json()
  def get_data_for_a_specific_date_for_a_specific_currency(self, code, date):
    self.response = requests.get("{}/rates/{}/{}/{}?format=json".format(self.url, self.table_type, code, date)).json()
  def get_data_from_specific_period_for_a_specific_currency(self, start_date, end_date, code):
    self.response = requests.get("{}/rates/{}/{}/{}/{}?format=json".format(self.url, self.table_type, code,  start_date, end_date)).json()

#testing all functions
test_nbp = Nbp("A")
top_count = "3"
date = "2016-01-01"
start_date = "2016-11-20"
end_date = "2016-11-29"
code = "USD"


test_nbp.get_todays_data()
print ("\nToday's data\n", test_nbp.response)
test_nbp.get_latest_data(top_count)
print ("\nData from last {} days\n".format(top_count), test_nbp.response)
#test_nbp.get_data_for_a_specific_date(date)
#print ("\nData for {}\n".format(date), test_nbp.response)
test_nbp.get_data_from_specific_period(start_date, end_date)
print ("\nData from {} to {}\n".format(start_date, end_date), test_nbp.response)
test_nbp.get_todays_data_for_a_specific_currency(code)
print ("\nTodays data for {}\n".format(code), test_nbp.response)
test_nbp.get_latest_data_for_a_specific_currency(top_count, code)
print ("\nData from last {} days for {} currency\n".format(top_count, code), test_nbp.response)
#test_nbp.get_data_for_a_specific_date_for_a_specific_currency(code, date)
#print ("\nData for {} for {}\n".format(date, code), test_nbp.response)
test_nbp.get_data_from_specific_period_for_a_specific_currency(start_date, end_date, code)
print ("\nData from {} to {} for {}\n".format(start_date, end_date, code), test_nbp.response)



