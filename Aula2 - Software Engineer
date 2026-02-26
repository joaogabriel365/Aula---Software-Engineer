# ====================================
# CONVERSOR DE TEMPERATURA
# Exercício - Engenharia de Software
# ====================================

def celsius_para_fahrenheit(celsius):
    """
    RF01: Converter Celsius para Fahrenheit
    Fórmula: F = (C × 9/5) + 32
    """
    return (celsius * 9/5) + 32


def fahrenheit_para_celsius(fahrenheit):
    """
    RF02: Converter Fahrenheit para Celsius
    Fórmula: C = (F - 32) × 5/9
    """
    return (fahrenheit - 32) * 5/9


# ====================================
# PROGRAMA PRINCIPAL
# ====================================

print("="*40)
print("  CONVERSOR DE TEMPERATURA")
print("="*40)

print("Escolha a conversão:")
print("1 - Celsius → Fahrenheit")
print("2 - Fahrenheit → Celsius")

opcao = input("Digite a opção (1 ou 2): ")

# RNF01: O sistema deve responder imediatamente após a entrada do usuário
# RNF02: Interface simples e intuitiva (menu claro e direto)

if opcao == "1":
    valor = float(input("Digite a temperatura em Celsius: "))
    resultado = celsius_para_fahrenheit(valor)
    print(f"\nResultado: {valor:.2f}°C = {resultado:.2f}°F")

elif opcao == "2":
    valor = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = fahrenheit_para_celsius(valor)
    print(f"\nResultado: {valor:.2f}°F = {resultado:.2f}°C")

else:
    print("\nOpção inválida. Execute o programa novamente.")

print("="*40)