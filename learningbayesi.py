from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]

cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

dados = [porco1, porco2, porco3, cachorro1,cachorro2,cachorro3]

marcacoes = [1,1,1,-1,-1,-1]

modelo.fit(dados, marcacoes)

misterioso1 = [1,1,1]
misterioso2 = [1,0,0]
misterioso3 = [1,0,1]

testes = [misterioso1, misterioso2, misterioso3]
marcacoes_teste = [-1, 1, -1]

resultado = modelo.predict(testes)

diferencas = resultado - marcacoes_teste

tot = 0

for num in diferencas:
    if num == 0:
        tot = tot+1

acertos = [tot]

taxa_de_acerto = 100.0 * len(acertos) / len(testes)

print(taxa_de_acerto)
