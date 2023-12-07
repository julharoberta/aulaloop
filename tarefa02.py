# Solicita ao usuário que entre com um valor inteiro entre 1 e 10
while True:
    valor = int(input("Digite um valor entre 1 e 10: "))
    if 1 <= valor <= 10:
        break
    else:
        print("Valor inválido. Tente novamente.")

# Exibe a tabuada do valor lido de 1 a 10
print(f"Tabuada do {valor}:")
for i in range(1, 11):
    resultado = valor * i
    print(f"{valor} x {i} = {resultado}")