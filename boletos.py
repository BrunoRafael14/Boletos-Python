# Algoritmo para eu guardar boletos que são parcelados
import os

print("O que deseja fazer: ")
print("1 - Adicionar Boleto")
print("2 - Consultar Boletos")
print("3 - Excluir Boletos")
menu = int(input(""))

if menu == 1:
	os.system("cls")
	numero_boleto = int(input("Digite o número do Boleto: "))
	data_boleto = input("Digite a data do vencimento do boleto (XX/XX/XXX) :")
elif menu == 2:
	os.system("cls")
	busca = int(input("Digite o número do Boleto para consulta: "))
elif menu == 3:
	os.system("cls")
	busca = int(input("Digite o número do Boleto para exclusão: "))
