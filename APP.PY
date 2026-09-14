#ENTRADA:
NOME_OBJETO = input ("Prezado cliente, por favor insira qual foi a sua compra conosco:")
VALOR_OBJETO = float (input ("Agora, insira o valor pago:"))
#PROCESSAMENTO E SAÍDAS:
if VALOR_OBJETO < 200:
    DESCONTO_05 = float (VALOR_OBJETO * 0.05)
    VALOR_C_DESCONTO_5 = float (VALOR_OBJETO - DESCONTO_05)
    print("Você acaba de receber um desconto de 5%, sua compra que antes era no valor de" , VALOR_OBJETO , "agora sairá no valor final de:" , VALOR_C_DESCONTO_5 , "R$")
elif VALOR_OBJETO < 300 :
     DESCONTO_10 = float (VALOR_OBJETO * 0.10)
     VALOR_C_DESCONTO_10 = float (VALOR_OBJETO - DESCONTO_10)
     print("Você acaba de receber um desconto de 10%, sua compra que antes era no valor de" , VALOR_OBJETO , "agora sairá no valor final de:" , VALOR_C_DESCONTO_10 , "R$")
elif VALOR_OBJETO >= 300:
     DESCONTO_15 = float (VALOR_OBJETO * 0.15)
     VALOR_C_DESCONTO_15 = float (VALOR_OBJETO - DESCONTO_15)
     print("Parabéns! Você acaba de receber um desconto de 15%, sua compra que antes era no valor de" , VALOR_OBJETO , "agora sairá no valor final de:" , VALOR_C_DESCONTO_15 , "R$")