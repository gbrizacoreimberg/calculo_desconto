print (str("Calculadora de Desconto"))

valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra < 200:
    percentual_desconto = 5
elif valor_compra < 300:
    percentual_desconto = 10
else:
    percentual_desconto = 15

valor_desconto = valor_compra * percentual_desconto / 100
valor_final = valor_compra - valor_desconto

print(f"Porcentagem de desconto: {percentual_desconto}%")
print(f"Valor do desconto em reais: R$ {valor_desconto:.2f}")
print(f"Valor final a ser pago: R$ {valor_final:.2f}")
