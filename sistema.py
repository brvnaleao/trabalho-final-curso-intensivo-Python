
import numpy as np



def compra():
	compras = True
	
	arrayQtd = []
	arrayCod = []
	while compras == True:
		codItem = int(input("O que você deseja comprar? Selecione o código do item: "))
		qtdItem = int(input("Dite a quantidade: "))
		qtd = int(b[codItem][2]) 
		if qtd>= qtdItem:

			arrayCod.append(codItem)
			arrayQtd.append(qtdItem)
			
			substituir(int(codItem), int(qtdItem))

		else:
			print("quantidade insuficiente no estoque")

		continuar = str(input("Deseja continuar comprando? [S/N]")).upper().strip()

		if continuar =='S':
			tabela()
			compras = True
		else:
			compras = False

	notaFiscal(arrayQtd, arrayCod)


def totalDeLucro():
	
	print("*"*50)
	print("Funcionalidade ainda não implementada")
	print("*"*50)
	print(" ")
	print(" ")

	menu()

def notaFiscal(quantidade, codigo):
	valorParcial = 0.0
	qtd = quantidade
	cd= codigo
	print(cd)
	print(qtd)
	indexx=0
	valorTotal = 0.0
	print("=-"*21)
	print("|{:<14}{:<14}{:<13}|".format("PRODUTO", "VALOR UN.", "TOTAL"))
	print("=-"*21)
	for q in qtd:	
		valorParcial = int(q)*float(b[cd[indexx]][1])
		valorTotal=valorTotal+valorParcial
		
		print("|{:<18}{:<16}{:<7}|".format(b[cd[indexx]][0], b[cd[indexx]][1], valorParcial))
		indexx+=1
	print("|TOTAL: {:34}|".format(valorTotal))
	
	print("=-"*21)
	print(" ")


	menu()



def menu():
	print("*"*30)
	print("1 .... Comprar \n2..... Ver tabela \n3..... Acrescentar itens \n4...... Ver total do lucro \n5..... Sair")
	print("*"*30)
	res = int(input("O que deseja fazer? "))
	
	if res == 1:
		compra()
	elif res == 2:
		tabela()
		menu()
	elif res == 3:
		acrescentar()
	elif res == 4:
		totalDeLucro()

	else:
		print("adeus!")
		exit(1)
	print(" ")
	print(" ")



def acrescentar():
	

	print("Funcionalidade ainda não implementada!")
	print(" ")
	print(" ")
	menu()



def substituir(posicao, quantidadeNova):
	a[posicao*3+2] = int(a[posicao*3+2]) - quantidadeNova
	print(a[posicao*3+2])

def tabela():
	print("=-"*24)
	item=0
	numero=0
	print("|{:<10}{:<14}{:<13}{:<10}|".format("CÓDIGO", "PRODUTO", "PREÇO", "ESTOQUE"))
	while item < len(a):
		print("|{:<7}{:<18}{:<18}{:<4}|".format(numero, a[item], a[item+1], a[item+2]))
		item+=3
		numero+=1
	print("=-"*24)
	print(" ")
	print(" ")


arquivo = open('produtos.txt', 'r')

produtos = arquivo.readlines()


listaProdutos = []
y =[]
for p in produtos:
	linhaProdutos = p.split(",")
	for unidade in range(len(linhaProdutos)):
		if unidade == 0:
			listaProdutos.append(linhaProdutos[unidade])
		elif unidade == 1:
			listaProdutos.append(linhaProdutos[unidade])
		else:
			listaProdutos.append(linhaProdutos[unidade])

listaProdutosEditada = []

for uni in listaProdutos:
    uni = uni.replace('\n', '')
    listaProdutosEditada.append(uni)

#até então temos uma lista com todos os dados separador. agora transformarei essa lista em uma matriz


a = np.array(listaProdutosEditada)
np.shape(a)
tam = int((len(a))/3)

b= np.reshape(a,(tam,3))
arquivo.close()
tabela()
menu()
