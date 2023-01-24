
import json
import csv

with open('klop.json') as f:
    output_data = json.load(f)

title = ['id', 'Name', 'Age', 'Phone']

output_data['123456'].append('0989875634')
output_data['234567'].append('0931234567')
output_data['456789'].append('0951534367')
output_data['567895'].append('0631034961')
output_data['789123'].append('0931234567')
output_data['126789'].append('0681999567')


with open('hard.csv', mode='w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(title)
    for key, value in output_data.items():
        writer.writerow([key, *value])





