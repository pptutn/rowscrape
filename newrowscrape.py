from typing import final
import requests;
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

URL = 'https://rowingmanager.com/regattas/5212/results'
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

results_table = soup.find_all('table', class_="rm_tbl rm_pad_2 rm_border_lite")

# print(len(results_table))
#results_table[i] gives each table, results_table holds all the results tables

# for i in range(len(results_table)):
#     print(results_table[i])
#     print(len(results_table[i]))
#     print('\n')
    

# mercs_count = 0
# boats = []

placing = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
dict_placings = {}

table_rows = soup.find_all('tr')

final_results = {}

for tr in table_rows:
    tds = tr.find_all('td')
    
    # print(len(tds), tds, '\n')
    # lengths are 2, 3, 8 and 5X
    if len(tds) == 2:
        if tds[0].text.strip() != '':
            print('MEDAL: ', tds[0].text)
        else:
            print('CREW: ', tds[1].text)
    elif len(tds) == 9:
        print('\n')
        if tds[0].text.strip() != '':
            print('PLACE: ', tds[0].text)
        print('school: ', tds[1].text)
        print('time: ', tds[6].text, ' margin1: ', tds[7].text, ' margin2', tds[8].text)
    elif len(tds) == 3:
        print('\n')
        print('------------------------------------------')
        print(tds[0].text, ' | ', tds[1].text, ' | ', tds[2].text)
        final_results[tds[0].text.strip()[5:]] = 'test'
    elif len(tds) == 4: # scratched
        print('\n')
        print(tds[3].text.strip())

print(final_results)

    # print(tds, '\n')

    # for i in range(len(tds)):                                           # for each of the rows of table data
    #     if tds[i].text[0:4] == 'Race':                                  # checks for the 'header' so we know which race
    #         print('----------------------')
    #         print(tds[0].text, tds[1].text, tds[2].text)
    #     elif tds[i].text in placing:
    #         if tds[i + 1].text == 'MERCANTILE':
    #             print('\n')
    #             print('PLACE: ', tds[i].text, tds[i+1].text)
    #         # print('')
    #     elif tds[i].text.strip() != '' and (tds[0].text == 'Place') :   # clearing out the lines with just whitespace
            
    #         # print(tds[i].text)
    #         continue




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

