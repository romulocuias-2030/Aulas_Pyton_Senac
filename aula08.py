# Desconto inteligente
valor_compra=float(input("Digite o valor: "))
vip=(input("Cliente Vip, Sim ou Não: "))
    
if valor_compra<100:
    print("Sem desconto")
    
else:
    if valor_compra>=100 and vip=="sim":
        print(f"Desconto de: {valor_compra*0.2:.2f}, \nvalor a pagar: {valor_compra-(valor_compra*0.2):.2f}")
    
    else:
        print(f"Desconto de: {valor_compra*0.1:.2f}, \nvalor a pagar: {valor_compra-(valor_compra*0.1):.2f}")