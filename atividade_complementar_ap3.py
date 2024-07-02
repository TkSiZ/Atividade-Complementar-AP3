# Membros do Grupo 
# Matheus Takashi Maruoka Vieira
# Rubens Takashi Maruoka Vieira

fita1 = []
fita2 = []
fita3 = []
resultado = "REJEITA"
cabecote1 = 0
cabecote2 = 0
cabecote3 = 0

def inicializaFita1(entrada):
    for i in entrada:
        fita1.append(i)
    fita1.append('\0')

def inicializaFita2():
    fita2.append('\0')

def inicializaFita3():
    fita3.append('\0')

def q14():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == '\x00') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == 'I'):
        fita1.insert(cabecote1, '0')
        cabecote1 += 1
        cabecote2 += 1
        cabecote3 += 1
        q14()
        return 
    
    elif (fita1[cabecote1] == '\x00') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == '\x00'):
        q7()
        return 

    else: 
        return
    
def q13():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == '\x00') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == 'I'):
        fita1.insert(cabecote1, 'I')
        cabecote1 += 1
        cabecote2 += 1
        cabecote3 -= 1
        q13()
        return 
    
    elif (fita1[cabecote1] == '\x00') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == '#'):
        q7()
        return 

    else: 
        return

def q12():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == '\x00') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == '#'):
        fita1.insert(cabecote1, '0')
        q7()
        return 
    
    elif (fita1[cabecote1] == '\x00') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == '\x00'):
        fita1.insert(cabecote1, '0')
        q7()
        return 

    else: 
        return

def q11():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == 'I'):
        cabecote2 += 1
        cabecote3 += 1
        q11()
        return 
    
    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == '\x00'):
        cabecote3 -= 1
        q10()
        return 

    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == '\x00'):
        cabecote1 += 1
        cabecote3 -= 1
        q13()
        return 

    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == 'I'):
        cabecote1 += 1
        q14()
        return 
    
    else: 
        return

def q10():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == 'I'): 
        cabecote2 += 1
        cabecote3 -= 1
        q10()
        return 
    
    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == 'I'):
        cabecote1 += 1
        q13()
        return 
    
    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == '#'):
        cabecote1 += 1
        cabecote3 += 1
        q13()
        return 
    
    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == '#'):
        cabecote1 += 1
        cabecote3 += 1
        q14()
        return 
    
    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == '#'):
        cabecote3 += 1
        q11()
        return 
    
    else: 
        return 

def q9():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == 'I'):
        cabecote2 -= 1
        cabecote3 += 1
        q9()
        return 
    
    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == '\x00'):
        cabecote2 += 1
        cabecote3 -= 1
        q10()
        return

    else:
        return 
    
def q8():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == 'I'):
        cabecote2 -= 1
        cabecote3 += 1
        q8()
        return 
    
    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == '\0'):
        cabecote3 -= 1
        q3()
        return 

    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == 'I'):
        cabecote2 -= 1
        cabecote3 += 1
        q9()
        return

    elif  (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == '\x00'):
        cabecote1 += 1
        q12()
        return 
    
    else:
        return 
    
def q7():
    global resultado 
    resultado = 'ACEITA'
    return;

def q6():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == '\x00') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == 'I'):
        fita1.insert(cabecote1, 'I')
        cabecote1 += 1
        cabecote2 += 1
        cabecote3 += 1
        q6()
        return 
    
    elif (fita1[cabecote1] == '\x00') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == '\x00'):
        cabecote1 += 1
        cabecote2 += 1
        q7()
        return

    elif (fita1[cabecote1] == '\x00') and (fita2[cabecote2] == '#') and (fita3[cabecote3] == '\x00'):
        q7()
        return 
    
    else: 
        return 

def q5():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == '\x00') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == 'I'):
        cabecote2 += 1
        cabecote3 += 1
        q5()
        return
    
    elif (fita1[cabecote1] == '\x00') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == 'I'):
        fita1.insert(cabecote1, 'I')
        cabecote1 += 1
        cabecote2 += 1
        cabecote3 += 1
        q6()
        return 

    else:
        cabecote1 -= 1
        q11()
        return

def q4():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == 'I'):
        cabecote2 -= 1
        cabecote3 -= 1
        q4()
        return 
         
    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == '#'):
        cabecote1 += 1
        cabecote2 += 1
        cabecote3 += 1
        q5()
        return
    
    else: 
        return

def q3():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == 'I'):
        cabecote2 -= 1
        cabecote3 -= 1
        q3()
        return
    
    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == 'I'):
        cabecote2 -= 1
        cabecote3 -= 1
        q4()
        return 
    
    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == 'I') and (fita3[cabecote3] == '#'):
        cabecote3 += 1
        q8()
        return    

    elif (fita1[cabecote1] == ' = ') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == '#'):
        cabecote1 += 1
        q12()
        return 
    
    else: 
        return

def q15():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == 'I') and (fita2[cabecote2] == '#') and (fita3[cabecote3] == '\x00'):
        cabecote1 += 1
        fita3.insert(cabecote3, 'I')
        fita2.insert(0, '\0')
        cabecote2 += 1
        cabecote3 += 1
        q15()
        return

    elif (fita1[cabecote1] == '\x00') and (fita2[cabecote2] == '#') and (fita3[cabecote3] == '\x00'):
        fita1.insert(cabecote1, ' = ')
        cabecote2 -= 1
        cabecote3 -= 1
        q3()
        return 


def q2():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == 'I') and (fita2[cabecote2] == '#') and (fita3[cabecote3] == '\x00'):
        cabecote1 += 1
        fita3.insert(cabecote3, 'I')
        fita2.insert(0, '\0')
        cabecote2 += 1
        cabecote3 += 1
        q15()
        return
    
    else: 
        return

def q1():
    global cabecote1
    global cabecote2
    global cabecote3
    if (fita1[cabecote1] == 'I') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == '\x00'):
        cabecote1 += 1
        fita2.insert(cabecote2, 'I')
        cabecote2 += 1
        q1()
        return
     
    elif(fita1[cabecote1] == '#') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == '\x00'):
        cabecote1 += 1
        fita2.insert(cabecote2, '#')
        fita3.insert(cabecote3, '#')
        cabecote3 += 1
        q2()
        return
    
    else: 
        return

def q0():
    global cabecote1
    global cabecote2
    global cabecote3
    cabecote1 = 0
    cabecote2 = 0
    cabecote3 = 0

    if (fita1[cabecote1] == 'I') and (fita2[cabecote2] == '\x00') and (fita3[cabecote3] == '\x00'):
        cabecote1 += 1
        fita2.insert(cabecote2, 'I')
        cabecote2 += 1
        q1()
        return
    
    else: 
        return

def mostrar():
    global resultado
    del fita1[-1]
    mostrarfita1 = ''.join(fita1)
    print(mostrarfita1, resultado)
    return 

def main():
    entrada = str(input("Input: "))
    inicializaFita1(entrada)
    inicializaFita2()
    inicializaFita3()
    q0()
    mostrar()

    

# Executando maquina de turing
main()