idadeano=int(input("Insira quantos anos voce tem -> "))
idademes=int(input("Insira quantos meses voce tem -> "))
idadedia=int(input("Insira quantos dias voce tem -> ") )
ano=(int(idadeano * 365 ))
mes=(int(idademes * 30))
idadefinal=(ano+mes+idadedia)
print(f"A sua idade em dias e de {idadefinal} dias. ")