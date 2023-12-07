# Solicita ao usuário que entre com os dois valores
primeiro = int(input("Digite o primeiro valor: "))
ultimo = int(input("Digite o último valor: "))

# Verifica se o último é menor que o primeiro para determinar a direção da contagem
if ultimo < primeiro:
    # Contagem decrescente
    for i in range(primeiro, ultimo - 1, -1):
        print(i)
else:
    # Contagem crescente
    for i in range(primeiro, ultimo + 1):
        print(i)