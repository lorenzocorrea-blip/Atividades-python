
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

if a == 0:
    print("Não é uma equação do 2º grau.")
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print("Uma raiz: x =", x)
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("x1 =", x1, "e x2 =", x2)
