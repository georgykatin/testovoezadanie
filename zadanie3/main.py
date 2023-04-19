import requests
from bs4 import BeautifulSoup


def pars(day, month, year, information, total_max_value, total_min_value):
	name_list, value_list = [], []

	if day<10:
		day = f"0{day}"
	if month<10:
		month = f"0{month}"
	
	response = requests.get(f'http://www.cbr.ru/scripts/XML_daily_eng.asp?date_req={day}/{month}/{year})')
	# print(day, month, year)
	soup = BeautifulSoup(response.text, 'xml')

	currency_names = soup.findAll('Name')
	currency_values = soup.findAll('Value')

	if "Error in parameters" in soup.find("ValCurs").text:
		return("try again")

	else:
		for name in currency_names:
			name_list.append(name.text)

		for value in currency_values:
			value = float(str(value.text).replace(",", "."))

			value_list.append(value)

		currency_dict = dict(zip(name_list, value_list))

		minimal = min(currency_dict, key=currency_dict.get)
		maximal = max(currency_dict, key=currency_dict.get)

		if float(total_max_value[0]) < currency_dict[maximal]:
			total_max_value = [currency_dict[maximal], [maximal, f"{day}/{month}/{year}"]]

		if float(total_min_value[0]) > currency_dict[minimal]:
			total_min_value = [currency_dict[minimal], minimal, f"{day}/{month}/{year}"]

		# currency_dict["minimal"]= {minimal:currency_dict[minimal]}
		# currency_dict["maximal"] = {maximal:currency_dict[maximal]}
		information[f"{day}/{month}/{year}"] = currency_dict


		return(information, total_max_value, total_min_value)


def avg_value(information, currency_name):
	i, avg = 0, 0
	for keys in information:
		avg += information[keys][currency_name]
		i += 1
	print(i, avg/i, currency_name)



if __name__ == "__main__":
	information = {}
	j, day, month, year = 0, 11, 11, 2020
	total_max_value, total_min_value = [0], [1000]
	while j != 90:
		pass
		if pars(day, month, year, information, total_max_value, total_min_value) == "try again":
			day = 1
			if month == 12:
				year += 1
				month = 1
			else:	
				month += 1

		else:
			information, total_max_value, total_min_value = pars(day, month, year, information, total_max_value, total_min_value)
			day += 1
			j += 1

	print(total_max_value, total_min_value)
	for currency_name in information['11/11/2020']:
		avg_value(information, currency_name)

	
