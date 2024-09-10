opcao = 0

menuInicial = """
[1] - depositar
[2] - sacar
[3] - extrato
[4] - saques restantes
[5] - sair
==>"""

saldo = 0
limite = 500
extrato = ""
saques = 0
limiteSaques = 3

def depositar(saldo,extrato): 
    try: 
        valor = float(input("valor a depositar:"))
        if  valor > 0:            
            saldo += valor
            extrato +=  f"deposito de R${valor:.2f}\n"
            print(f"valor depositado: R${valor:.2f}")
            print(f"saldo = R${saldo:.2f}")
        else: print("valor do deposito precisa ser positivo")
        return saldo, extrato
    except ValueError: print("valor precisa ser um numero")

def sacar(saldo, extrato):
    try:
        valor = float(input("valor a sacar:"))
        if  valor > saldo: 
            print ("saldo insuficiente")
            return saldo, extrato
        
        if  valor > 0 and valor <= 500:
            saldo -= valor
            extrato +=  f"saque de R${valor:.2f}\n" 
            print(f"valor sacado: R${valor:.2f}")
            print(f"saldo = R${saldo:.2f}") 
        elif valor > 500:
            print("valor do saque precisa ser ate R$500,00")          
        else: print("valor do saque nao pode ser negativo")
        return saldo, extrato
    except ValueError: print("valor precisa ser um numero")

while opcao != 5:
    
    try:
        opcao = int(input(menuInicial))

        if  opcao == 1: 
            result = depositar(saldo, extrato)  
            saldo = result[0] 
            extrato = result [1] 

        elif opcao == 2:
            if saques >= 3:
                print("limite de saques atingido")
            else:
                result = sacar(saldo, extrato)
                saldo = result[0]
                extrato = result [1]
                saques += 1

        elif opcao == 3:
            print("\n=============EXTRATO=============")
            print("Não foram realizadas movimentações" if not extrato else extrato)
            print(f"\nSaldo: R${saldo:.2f}") 
            print("=================================")

        elif opcao == 4:

            print(f"saques realizados:{saques}")  

    except ValueError: print("valor precisa ser um numero")