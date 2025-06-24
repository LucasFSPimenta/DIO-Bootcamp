menu = """

[d] Depositar
[s] Sacar  
[e] Extrato
[q] Sair 

=> """

LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500

saldo_atual = 600
depósito_1 = 0
depósito_2 = 0
depósito_3 = 0
depositos_feitos = 0
deposito = 0
saque = 0
saques_feitos = 0
valor_sacado_1 = 0
valor_sacado_2 = 0 
valor_sacado_3 = 0 

extrato = ""


while True:
    
    opcao_escolhida = input(menu)
    
    if opcao_escolhida in ["d", "s" , "e", "q"]:
        
        if opcao_escolhida == "d":
            deposito = float(input("Quanto Deseja Depositar?"))
            
            if deposito > 0:
                saldo_atual = saldo_atual + deposito
                depositos_feitos += 1
                print(f"Você depositou R${deposito: .2f} e seu saldo atual é R${saldo_atual: .2f}")
                extrato += f" Depósito: R$ {deposito: .2f}"
                
            else:
                print("O valor informado é inválido")        
            
            
        elif opcao_escolhida == "s":
            saque = float(input("Quanto deseja sacar?"))
            
            if saque < 0:
                print("Valor inválido. Digite novamente")
            
            elif saque > saldo_atual:
                print("Você não possui saldo suficiente para esta transação")
                
            elif saque > LIMITE_POR_SAQUE:
                print("Voce não pode sacar mais do que R$500,00 por operação")   
                
            elif saques_feitos >= LIMITE_SAQUES:
                print("Você já realizou 3 saques hoje. Tente novamente amanhã!")
                
            else:
                saques_feitos += 1
                saldo_atual = saldo_atual - saque
                print(f"Você sacou R${saque: .2f} e o seu saldo atual é R${saldo_atual: .2f}")
                extrato += f" Saque: R$ {saque: .2f}"
            
        elif opcao_escolhida == "q":
            print("Obrigado por usar o banco XYZ")   
            break 
        
        elif opcao_escolhida == "e":
            print("\n=========================EXTRATO===========================")
            print({extrato})
            print(f"\nSaldo atual:{saldo_atual}")
            
        
        
    else:
        print("Opção inválida. Tente novamente")      

        