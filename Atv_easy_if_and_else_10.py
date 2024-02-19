turno = input("Qual turno você estuda?  M-matutino ou V-vespertino ou N-noturno: ")

if turno == "M" or turno == "matutino":
    print("Bom dia!")
elif turno == "V" or turno == "vesperino":
    print("Boa noite!")
else:
    print("Valor inválido")