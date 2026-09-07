#tal vez avance un poco mas de lo ideal pero la verdad estaba muy divertido profe y sentia que estaba entregando algo muy vacio asi que estudie un poco por mi parte para poder hacer unas cosas en el codigo jajaja, 
# asi tal vez me da tiempo de hacer la otra parte que queria hacer para mi proyecto

def mostrar_menu () :
    print("1,-calcular calorias comida")
    print("2,-calcular dieta semana")
    print("3,-salir")
    opcion=int(input("selecciona una opcion"))

    return opcion
def calculo_de_calorias(comida, gramos) :
    calorias_comida= comidas[comida]["calorias"]
    total=(calorias_comida/100)* gramos
    return total
def calculo_de_proteinas(comida, gramos) :

    proteinas_comida= comidas[comida]["proteina"]
    total=(proteinas_comida/100)* gramos
    return total
def mantenimiento_diarioH(altura, peso, años) :
   TMB=(10*peso)+(6.25*altura)-(5*años)+5
   return TMB
def mantenimiento_diarioM (altura, peso, años) :
   TMB=(10*peso)+(6.25*altura)-(5*años)-161


   return TMB
#mi diccionario esta basado en cantidades de 100gr e ire agregando mas alimentos con el tiempo esto es solo para el avance
comidas={
    "pollo":{
        "calorias": 167,
        "proteina": 31
    },
    "carne molida":{
       "calorias": 265,
       "proteina": 20
    },
    "arroz":{
       "calorias": 130,
       "proteina": 2
    }

}

opcion=mostrar_menu()


if opcion== 1 :
 calorias=0
 proteina=0

 agregar_otra_comida= "si"

 while agregar_otra_comida== "si":
    comida= input("que alimento deseas calcular? ")
    gramos= float(input("cuantos gramos consumiste? "))
    tu_total= calculo_de_calorias(comida, gramos)
    tu_totalp=calculo_de_proteinas(comida, gramos)
    calorias+= tu_total
    proteina+= tu_totalp
    agregar_otra_comida= input("te gustaria agregar otro alimento? (si/no): ")


 print ("tus calorias son", calorias, "y tus proteinas son", proteina )


#no se me ocurrio algo mas eficiente que poner el calculo en ambas porque no sabia como hacerlo
if opcion==2:
   meta_calorica=0 
   altura= float(input("cuantos cm mides? "))
   peso= float(input("cual es tu peso actual? "))
   años= int(input("cuantos años tienes? "))
   imc=(peso*10000)/altura**2
   genero=input("cual es tu genero? (hombre/mujer):")
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
        if protes== "no" :
             print("gracias por utilizar la calculadora")
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
        if protes== "no" :
         print("gracias por utilizar la calculadora")

   
         

        

     #me gustaria ver si se puede hacer un poco mejor algunas cosas pero ya aprovechare para preguntarle el martes