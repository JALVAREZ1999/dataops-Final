
#Función para calcular el área de un circulo

def calcular_area(base, altura):
    return 0.5 * base * altura

base = float(input("Ingrese base en metros: "))
altura = float(input("Ingrese altura en metros: "))

area = calcular_area(base, altura)
print(f'El área del triángulo es: {area}')
