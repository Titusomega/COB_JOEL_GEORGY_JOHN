from forex_python.converter import CurrencyRates
def get_country_currency(country_name):
  try:
    from countryinfo import CountryInfo
  except ImportError:
    print("Please install the countryinfo module using pip: pip install countryinfo")
    return

  country = CountryInfo(country_name)
  currencies = country.currencies()
  if len(currencies) == 0:
    print("No currency information found for country:", country_name)
    return

  currency = currencies[0]
  return currency
a=int(input("If country name enter '1',if currency enter '2' :"))
if a==1:
  country_name = input("Enter the country name(from currency): ")
  ammount=int(input("Enter the ammount"))
  if(ammount.isdigit()!=0):
    to_country_name=input("Enter the country name(to currency): ")
    a1=get_country_currency(country_name)
    a2=get_country_currency(to_country_name)
    c = CurrencyRates()
    print(ammount*c.get_rate(a1, a2),a2)
  else:
    print("Input Error")
elif a==2:
  a1=input("Enter the country currency to convert from : ")
  a2=input("Enter the country currency to convert to : ")
  ammount=int(input("Enter the ammount : "))
  c = CurrencyRates()
  print(ammount * c.get_rate(a1, a2), a2)
else:
  print("Invalid input")