edadmenor=int(input("Introduce la edad:"))
edadmayor=int(input(>=65))
sexo=input("Hombre")or("Mujer")
cabello=input("Moreno")or("Castaño")or("Rubio")
if(edadmenor<=5)or(edadmayor>=65):
    print("GRATIS")
else:
    print("PAGAR")
if(sexo="Hombre"):
    print("PAGAR")
if(sexo="Mujer")and(cabello="Rubio"):
    print("GRATIS")
if(sexo="Hombre")and(edadmayor>=65):
    print("GRATIS")
if((edadmenor>=5)or(edadmayor<=65))or(cabello=input("Moreno")or("Castaño")or("Rubio"))or(sexo="Hombre"):
    print("PAGAR 0,50")
