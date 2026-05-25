#Feramenta de Conversão Dólar x Real --
def converter(valor_dobr):
    taxa = 5.15
    valor_real = valor_dobr * taxa
    return valor_real
print("Conversor Dólar x Real")
preco = float(input("Digite o Preço do produto em Dólar:"))
resultado = converter(preco)
print(f"O valor em Reais é: {resultado:.2f}")