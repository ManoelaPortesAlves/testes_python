import json

f = open('dados.json')

data = json.load(f)

salesDict = {}
vendaTotalMensal = 0
totalDiasDeVenda = 0
faturamentoDiarioUltrapassou = []

#  Inserindo os dias de venda e seus valores no dict salesDict
for i in data:
    if i['dia'] not in salesDict.keys() and i['valor'] != 0.0:
        salesDict[i['dia']] = i['valor']

#  Contando o total de venda mensal
for item in salesDict.keys():
    vendaTotalMensal += salesDict[item]

#  Contando todos os dias de venda
for key, value in salesDict.items():
    totalDiasDeVenda += 1

#  Verificando os dias em que a venda foi maior que a média mensal
for item in salesDict.keys():
    if salesDict[item] > (vendaTotalMensal / totalDiasDeVenda):
        faturamentoDiarioUltrapassou.append(item)

#  Achando o dia com mais e menos vendas
max_key = [key for key, value in salesDict.items() if value == max(salesDict.values())]
min_key = [key for key, value in salesDict.items() if value == min(salesDict.values())]

print('Dia de maior venda: ', max_key)
print('Dia de menor venda: ', min_key)
print('Venda total mensal: ', str(round(vendaTotalMensal, 2)))
print('Total dias de venda: ', totalDiasDeVenda)
print('Media de venda mensal: ', str(round((vendaTotalMensal / totalDiasDeVenda), 2)))
print('Dias em que o faturamento diario ultrapassou a media mensal: ', faturamentoDiarioUltrapassou)

f.close()





