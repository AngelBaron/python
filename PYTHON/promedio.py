res = ""
promedio=0

while(res !="1"):
    cal=0
    print("INGRESA EL NOMBRE DEL ALUMNO \n")
    
    nombre = input()
    
    for i in range(6):
        if(i==0):
            materia = "ESTRUCUTRA DE DATOS"
        elif(i==1):
            materia="ALGORITMICA"
        elif(i==2):
            materia="COMPILADORES"
        elif(i==3):
            materia="BASE DE DATOS"
        elif(i==4):
            materia="ARQ. DE COMPUTADORAS"
        elif(i==5):
            materia="ESTADISTICA"
        elif(i==6):
            materia="PROGRAMACION"
        
        print("COLOCA LA CALIFICACION DE LA MATERIA: \n",materia)
        cal += float(input())
    promedio= cal/6 

    
    if(promedio>=8):
        print("El alumno ",nombre," aprobó con la calificacion de ", promedio)
    else:
        print("El alumno ",nombre," no aprobó con la calificación de ", promedio)

    print("quieres integrar a otro alumno \n SI = cualquier tecla \n NO = 1")
    res= input()
    


