#Importaciones necesarias...
from tkinter import *


#Metodo para calcular las operaciones
def Suma():
   global operador
   operador=caja1.get()+'+'
   caja1.delete(0,20)

def Resta():
   global operador
   operador=caja1.get()+'-'
   caja1.delete(0,20)

def Multiplicacion():
   global operador
   operador=caja1.get()+'*'
   caja1.delete(0,20)

def Division():
   global operador
   operador=caja1.get()+'/'
   caja1.delete(0,20)

def calcular(op):
	operador=eval(op+caja1.get())
	caja1.delete(0,20)
	caja1.insert(0,operador)

def limpiar():
	caja1.delete(0,20)

def clickNum(num):
	numero=caja1.get()+num
	caja1.delete(0,20)
	caja1.insert(0,numero)
	numero=''

#Creacion del root
root = Tk()
#Titulo del root
root.title("MiniCalculadora")
#Dimensiones (ancho,alto)
root.geometry("350x450")   
#color de fondo
root.config(bg='SkyBlue4')

#Creacion de una caja de texto para el primer numero
caja1=Entry(root,bd=6,width=15,font=('calibri',20,'bold'))
caja1.place(x=17,y=17)

global operador
operador=''

#Botones para los numeros del 0 al 9
Button(root, text = "1", font=('calibri',10,'bold'),command = lambda:clickNum("1"),width=11,height=3).place(x=17,y=80)
Button(root, text = "2", font=('calibri',10,'bold'),command = lambda:clickNum("2"),width=11,height=3).place(x=107,y=80)
Button(root, text = "3", font=('calibri',10,'bold'),command = lambda:clickNum("3"),width=11,height=3).place(x=197,y=80)
Button(root, text = "4", font=('calibri',10,'bold'),command = lambda:clickNum("4"),width=11,height=3).place(x=17,y=140)
Button(root, text = "5", font=('calibri',10,'bold'),command = lambda:clickNum("5"),width=11,height=3).place(x=107,y=140)
Button(root, text = "6", font=('calibri',10,'bold'),command = lambda:clickNum("6"),width=11,height=3).place(x=197,y=140)
Button(root, text = "7", font=('calibri',10,'bold'),command = lambda:clickNum("7"),width=11,height=3).place(x=17,y=200)
Button(root, text = "8", font=('calibri',10,'bold'),command = lambda:clickNum("8"),width=11,height=3).place(x=107,y=200)
Button(root, text = "9", font=('calibri',10,'bold'),command = lambda:clickNum("9"),width=11,height=3).place(x=197,y=200)
Button(root, text = "0", font=('calibri',10,'bold'),command = lambda:clickNum("0"),width=11,height=3).place(x=107,y=260)



#Botones para las operaciones
botonSuma =  			Button(root, text = "+", font=('calibri',10,'bold'),command = Suma,			width=11,height=3).place(x=17,y=320)
botonResta = 			Button(root, text = "-", font=('calibri',10,'bold'),command = Resta,		 	width=11,height=3).place(x=107,y=320)
botonMultiplicacion = 	Button(root, text = "*", font=('calibri',10,'bold'),command = Multiplicacion,width=11,height=3).place(x=197,y=320)
botonDivicion = 		Button(root, text = "/", font=('calibri',10,'bold'),command = Division,		width=11,height=3).place(x=17,y=380)

#Botones para calcular y limpiar
botonCalcular = Button(root, text = "=", font=('calibri',10,'bold'),command = lambda:calcular(operador),	width=11,height=3).place(x=197,y=380)
botonLimpiar = 	Button(root, text = "C", font=('calibri',10,'bold'),command = limpiar,					width=11,height=3).place(x=107,y=380)

#Cargar el root
root.mainloop()