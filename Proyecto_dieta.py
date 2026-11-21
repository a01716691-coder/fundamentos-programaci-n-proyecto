import json


with open("alimentos.json", "r", encoding="utf-8") as diccionario:
    datos_comida= json.load(diccionario)
    comidas=datos_comida["comidas"]

with open("perfiles.json","r",encoding="utf-8") as archivo:
    datos_perfiles=json.load(archivo)
    perfiles=datos_perfiles["perfiles"]

def pide_numero(mensaje):
    numero=0
    while numero<=0:
        try:
            numero=float(input(mensaje))
            if numero<=0:
                print("el digito que ingresaaste tiene que ser mayor a 0")
        except ValueError:
            print("favor de solo escribir numeros en este apartado")
            numero=0
    return numero

def mostrar_menu () :
    print("1,-calcular calorias comida")
    print("2,-calcular dieta semana")
    print("3,-agregar comida al diccionario")
    print("4,-salir")
    opcion=int(input("selecciona una opcion"))

    return opcion
def calculo_de_calorias(comida, gramos) :
    if comida in comidas:
        calorias_comida= comidas[comida]["calorias"]
        total=(calorias_comida/100)* gramos
    else:
         print("esta comida no se encuentra en el diccionario actual, favor de buscar su informacion y agregarla")
    return total

def calculo_de_proteinas(comida, gramos) :
    if comida in comidas:
        proteinas_comida= comidas[comida]["proteina"]
        total=(proteinas_comida/100)* gramos
    else:
             print("esta comida no se encuentra en el diccionario actual, favor de buscar su informacion y agregarla")
    return total
def mantenimiento_diarioH(altura, peso, años) :
   TMB=(10*peso)+(6.25*altura)-(5*años)+5
   return TMB
def mantenimiento_diarioM (altura, peso, años) :
   TMB=(10*peso)+(6.25*altura)-(5*años)-161


   return TMB

def agrega_comida(nombre, calorias, proteina):
    if nombre in comidas:
        print("ese alimento ya esta en el diccionario")
    else:
        comidas[nombre]={"calorias":calorias,"proteina":proteina}
        with open("alimentos.json","w",encoding="utf-8") as diccionario:
            json.dump(datos_comida,diccionario,indent=4,ensure_ascii=False)
        print(nombre, "se agrego al diccionario")

def mostrar_alimentos():
     print("alimentos disponibles")
     for nombre in comidas:
          print("-", nombre)
    

def agrega_(nombre, calorias, proteina):
    if nombre in comidas:
        print("ese alimento ya esta en el diccionario")
    else:
        comidas[nombre]={"calorias":calorias,"proteina":proteina}
        with open("alimentos.json","w",encoding="utf-8") as diccionario:
            json.dump(datos_comida,diccionario,indent=4,ensure_ascii=False)
        print(nombre, "se agrego al diccionario")


def pide_de_lista(mensaje,opciones):
    respuesta=mensaje
    while respuesta not in opciones:
        respuesta=input(mensaje).lower()
        if respuesta not in opciones:
            print("opcion no valida, favor de escribir una dentro de la lista")
            mostrar_alimentos()
    

opcion=mostrar_menu()



if opcion== 1 :
 calorias=0
 proteina=0

 agregar_otra_comida= "si"

 while agregar_otra_comida== "si":
    mostrar_alimentos()
    lista_nombres=[]
    opciones=lista_nombres
    for nombre in comidas:
        lista_nombres.append(nombre)
    comida=pide_de_lista(("que alimento deseas calcular? "),(opciones) )
    #mensaje=float(input("cuantos gramos consumiste? "))
    gramos=pide_numero("cuantos gramos consumiste? ")
    tu_total= calculo_de_calorias(comida, gramos)
    tu_totalp=calculo_de_proteinas(comida, gramos)
    calorias+= tu_total
    proteina+= tu_totalp
    agregar_otra_comida= input("te gustaria agregar otro alimento? (si/no): ")


    print ("tus calorias son", calorias, "y tus proteinas son", proteina )
    mostrar_menu()

#estoy intentando agregar algo pero no me sale por eso lo estoy dejando asi una disculpa
if opcion==2:
   meta_calorica=0 
   #registro=print("ya tienes un perfil registrado?: (si/no)")
   #if registro=="si":
   #registro=pide_de_lista(("ya tienes un perfil registrado?: (si/no)"), ["si","no"])
   #nombre=input("como te llamas? ").lower()
  # if registro=="si" and nombre in perfiles:
   #     altura=perfiles[nombre]["altura"]
    ##   genero=perfiles[nombre]["genero"] 
   #else:         
   altura= pide_numero("cuantos cm mides? ")
   peso=pide_numero("cual es tu peso actual? ")
   años= pide_numero("cuantos años tienes? ")
   imc=(peso*10000)/altura**2
   genero=input("cual es tu genero? (hombre/mujer):").lower()
   if genero== "hombre":
    TMB=mantenimiento_diarioH(altura, peso, años)
    actividad=input("que tanta actividad fisica haces? (1, 2, 3, 4, 5):")
    if actividad== "1" :
        total=TMB*1.2
    if actividad=="2":
          total=TMB*1.375
    if actividad=="3" :
           total=TMB*1.55
    if actividad== "4":
           total=TMB*1.725
    if actividad=="5":
           total=TMB*1.9
    meta_calorica=+ total
    
    print ("tus calorias de mantenimiento son", meta_calorica)

   if genero== "mujer" :
        TMB=mantenimiento_diarioM(altura, peso, años)
        actividad=input("que tanta actividad fisica haces? (1, 2, 3, 4, 5):")
        if actividad== "1" :
               total=TMB*1.2
        if actividad=="2":
                 total=TMB*1.375
        if actividad=="3" :
                  total=TMB*1.55
        if actividad== "4":
                  total=TMB*1.725
        if actividad=="5":
                  total=TMB*1.9
        meta_calorica=+ total
           
        print ("tus calorioas de mantenimiento son", meta_calorica)
   etapa= input("en que etapa de tu dieta estas? (volumen/definicion):")
   if etapa=="volumen" :
        if imc<18.5 :  
             calorias_totales=meta_calorica+600
             print("debido a tu IMC haremos un aumento mayor y tus calorias diarias seran", calorias_totales, "favor de reevaluar en dos semanas")
        if imc>18.5:
         calorias_totales= meta_calorica+400
         print("para continuar con un volumen productivo deberas aumentar tu ingesta diaria a", calorias_totales, "calorias diarias")
        protes=input("te gustaria saber cuantas proteinas deberias estar comiendo diariamente? (si/no):") 
        if protes=="si" :
                 proteinas_diarias=peso*2
                 print("deberias estar comiendo", proteinas_diarias, "gr de proteina diaria")
                 mostrar_menu()
        if protes== "no" :
             print("gracias por utilizar la calculadora")
             mostrar_menu()
   if etapa=="definicion":
        if imc>25.0 :
             calorias_totales=meta_calorica-600
             print("debido a tu IMC haremos una definicion un poco mas agresiva y tus calorias diarias seran", calorias_totales, "favor de reevaluar en dos semanas")
        if imc<25.0:
         calorias_totales= meta_calorica-300
         print("para definir tendras que bajar a", calorias_totales, "calorias diarias")
        protes=input("te gustaria saber cuantas proteinas deberias estar comiendo diariamente? (si/no):") 
        if protes=="si" :
         proteinas_diarias=peso*2.5
         print("deberias estar comiendo", proteinas_diarias, "gr de proteina diaria")
         mostrar_menu()
        if protes== "no" :
         print("gracias por utilizar la calculadora")
         mostrar_menu()
if opcion==3:
    nombre=input("como se llama el alimento? ").lower()
    calorias=pide_numero("cuantas calorias tiene por 100 gramos? ")
    proteina=pide_numero("cuantos gramos de proteina tiene por 100 gramos? ")
    agrega_comida(nombre, calorias, proteina) 
    mostrar_menu()
if opcion==4:
     print("Muchas gracias por utilizar este programa")
   
         

        

