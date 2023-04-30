
compra = { "Pomes" : {"Qty": 5, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66} }
print(type(compra))
print(compra)
print('\n')

# Afegeix alguna fruita més:
compra['Taronges'] = {'Qty': 10, '€': 0.53}
print(compra)
print('\n')

# Quant han costat les peres en total?
preu_peres = compra['Peres']['Qty'] * compra['Peres']['€']
print ('Les peres han costat ' + str(preu_peres) + ' €.\n')

# Quantes fruites hem comprat en total?
tot_frutas = []
for fruta in compra:
    tot_frutas.append(compra[fruta]['Qty'])
sum_frut = sum(tot_frutas)
print('En total hem comprat ' + str(sum_frut) + ' frutas.\n')

# Quina és la fruita més cara?
preus = []
for i in compra:
    preus.append(compra[i]['€'])
mes_car = max(preus)

for j in compra:
    if  compra[j]['€'] == mes_car:
        print('la fruita mes cara son les ' + str(j) + '.\n')
