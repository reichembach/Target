import json

fname = 'dados.json'
str_data = open(fname).read()
json_data = json.loads(str_data)

min = 0
max = 0
i = 0
total = 0
for item in json_data:
    if item['valor'] == 0:
        continue
    total = total + item['valor']
    i = i + 1
    if min == 0 or item['valor'] < min:
        min = item['valor']
        diamin = item['dia']
    if max == 0 or item['valor'] > max:
        max = item['valor']
        diamax = item['dia']
med = total / i
dias = 0
for item in json_data:
    if item['valor'] > med:
        dias = dias + 1
print('Menor faturamento foi dia', diamin, 'com um valor de', min)
print('Maior faturamento foi dia', diamax, 'com um valor de', max)
print('Sendo a média mensal de', round(med),
      ', o número de dias no mês em que o valor de faturamento foi superior a essa média foi:', dias, 'dias')
