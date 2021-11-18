import requests;
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

URL = 'https://rowingmanager.com/regattas/5212/results'
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

results_table = soup.find_all('table', class_="rm_tbl rm_pad_2 rm_border_lite")

# print(results_table)

mercs_count = 0
boats = []




# event_arr contains dictionaries {event_no, event_type, event_entries}
tables = soup.findChildren('tbody')
arr_data = [text for text in tables[0].stripped_strings]
event_arr =[]
for i in range(0, len(arr_data), 3):
    event_dict = {}
    for j in range(i, i+3):
        if j % 3 == 0:
            key='event_no'
        elif j % 2 == 0:
            key='event_type'
        else:
            key='event_entries'
        event_dict[key] = arr_data[j]
    event_arr.append(event_dict)
    # print(event_dict)

    


# new = results_table[0].find_all('td', class_='')
# # print(new)
# # for el in new:
# #     print(lengthel.text == 3)

# for table in results_table:
#     first = table.find('td', class_='rm_nowrap')
#     if "MERCANTILE" in first.text:
#         mercs_count += 1
#         print(first)

#     # info = table.find('tbody')
#     # print(info)

# print('mercs count', mercs_count)

