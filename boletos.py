# Algoritmo para eu guardar boletos que são parcelados
import os
import json

contagem = 1

boletos = {}


while contagem == 1:
	print("O que deseja fazer: ")
	print("1 - Adicionar Boleto")
	print("2 - Consultar Boletos")
	print("3 - Excluir Boletos")
	menu = int(input(""))

	if menu == 1:
		os.system("cls")
		busca_endereco = input("Digite o endereço do Imóvel: ")
		busca_numero_boleto = input("Digite o número do Boleto: ")
		busca_data_boleto = input("Digite a data do vencimento do boleto (XX/XX/XXX) :")

		boletos[busca_numero_boleto] = {
			"endereço" : busca_endereco,
			"vencimento do boleto" : busca_data_boleto
		}

		caminho_json = "dados/boletos.json"

		with open(caminho_json, 'w', encoding='utf-8') as arquivo:
			json.dump(boletos, arquivo, ensure_ascii=False, indent=4)

		print("Boleto número {} cadastrado com sucesso!".format(busca_numero_boleto))

	elif menu == 2:
		os.system("cls")
		with open("dados/boletos.json", 'r', encoding='utf-8') as arquivo:
			boletos = json.load(arquivo)

		tipo_pesquisa = int(input("Gostaria de Pesquisar um boleto em específico ou vizualizar todos os boletos ? \n1 - BuscaIndividual \n2 - Busca Geral \n"))
		if tipo_pesquisa == 1:
			busca = input("Digite o número do Boleto para consulta: ")
			if busca in boletos:
				position = boletos[busca]
				print(position) 
			else:
				print("Boleto não cadastrado")
		elif tipo_pesquisa == 2:
			os.system("cls")
			for boleto in boletos:
				dados = boletos[boleto]
				print("Boleto nº: {} \n Endereço: {}\n Vencimento: {} \n--------------------".format(boleto, dados["endereço"], dados["vencimento do boleto"]))
		else:
			print("Opção inválida")

	elif menu == 3:
		os.system("cls")
		#Abrir o arquivo e salvar na variável boletos
		with open("dados/boletos.json", 'r', encoding='utf-8') as arquivo:
			boletos = json.load(arquivo)
		
		#Buscar o boletos e excluir com a função pop()
		busca = input("Digite o número do Boleto para exclusão: ")
		if busca in boletos:
			exclusao = boletos.pop(busca)

		#Abaixo é o comando para salvar a exclusão no arquivo json
		caminho_json = "dados/boletos.json"
		with open(caminho_json, 'w', encoding='utf-8') as arquivo:
			json.dump(boletos, arquivo, ensure_ascii=False, indent=4)

	contagem = int(input("Deseja fazer mais buscas ? \n1 - Sim \n2 - Não \n "))
	os.system("cls")
