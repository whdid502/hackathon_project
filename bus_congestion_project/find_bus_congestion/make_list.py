import csv
import os

# f = open('C:\Users\whdid\OneDrive\바탕 화면\2020_08_bus_list_utf_8.csv', encoding='utf-8')
# rdr = csv.reader(f)

# for line in rdr:
#     print(line)

# f.close()

os.chdir(r'C:\Users\whdid\OneDrive\바탕 화면')


# bus_dic_list = []
terminal_list = []
with open('2020.csv', encoding='utf-8') as f:
    rdr = csv.reader(f)

    for line in rdr:
        terminal = line[3]
        terminal_list.append(terminal)
terminal_list = set(terminal_list)
terminal_list = list(terminal_list)
print(terminal_list)
print(len(terminal_list))

# with open('terminal.csv', 'w', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     for val in terminal_list:
#         writer.writerow([val])

with open('terminal.csv', "w", encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in terminal_list:
        writer.writerow(row)

# with open('terminal.csv', "w") as f:
#     writer = csv.writer(f)
#     for row in terminal_list:
#         writer.writerow(row)


# with open('bus_stop','w', newline='') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(bus_stop)

# with open('bus_stop2.csv', 'w') as f:
#     writer = csv.writer(f)
#     for val in bus_stop:
#         writer.writerow([val])