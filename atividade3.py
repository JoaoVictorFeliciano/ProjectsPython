
ladoa=float(input("Digite o comprimento do lado A: "))
ladob=float(input("Digite o comprimento do lado B: "))
ladoc=float(input("Digite o comprimento do lado C: "))
if (ladoa + ladob > ladoc) and (ladoa + ladoc > ladob) and (ladob + ladoc > ladoa):
    if ladoa == ladob == ladoc:
        print("Equilátero")
    elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("As medidas informadas não formam um triângulo")

