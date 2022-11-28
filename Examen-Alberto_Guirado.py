'''
1-Crea una función que NO reciba ningún parámetro y que imprima por pantalla las opciones: 1-Sumar 2-Salir
2-Crea una función que reciba dos números y devuelva la suma de estos números.
3-El programa principal tiene que mostrar el menú de la función y hasta que se pulse la opción 2-Salir el programa tiene que funcionar.
4-Si se pulsa la opción 1, el programa pide al usuario dos números y con la ayuda de la función sumar mostrar por pantalla el resultado.
5-Cuando el usuario introduce dos números se puede equivocar e introducir caracteres con lo que el programa se interrumpe. Realiza los cambios necesarios para controlar estos errores.
6-Sube los cambios a tu repositorio y copia la dirección en la entrega del examen.
'''

num3 = 0

#1

def menu():
    print("1-sumar, 2-Salir")


#2

def sumar(num1:int,num2:int):
    return num1+num2





while num3!=2:
        try:
            menu()
            num3=int(input("Dime una opción:\n"))
            if num3==1:
                print("Vamos a realizar la suma de dods números")
                num1=int(input("Dime el primer número:\n"))
                num2=int(input("Dime el primer número:\n"))
                result =sumar(num1+num2)
                print(f"La suma de {num1} + {num2} = {result}")
        except:
            print("El programa solo admite números, por favor intentelo de nuevo. \nGracias")

print("Has salido del programa.")


