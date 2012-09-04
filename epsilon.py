# -*- coding: utf-8 *-*
"""Script que halla el Epsilon de la maquina"""
import datetime

import wx

import math

class Biseccion:
	def __init__(self, ecuacion, a, b):
		self.ecuacion = ecuacion
		self.traducirEcua(ecuacion)
		self.a = a
		self.b = b
		self.retu = "";
	def setAorB(self):
		if self.isPos(self.Fa) and self.isPos(self.FPn):
			#ambos son positivos
			self.a = self.pn
		elif self.isPos(self.Fa)==False and self.isPos(self.FPn)==False:
			#mbos son negativos
			self.a = self.pn
		else:
			self.b = self.pn
			#diferente signo
	def isPos(self,x):
		retu = False
		if x > 0:
			retu = True
		else:
			retu = False
		return retu
	def setFa(self):
		x = self.a
		print "str a:"+str(self.a)
		temp = self.ecuacionTraducida.replace("x",str(self.a))
		print self.a
		print temp
		exec temp
		print y
		#exec self.ecuacionTraducida
		print y
		self.Fa = y
	def setFPn(self):
		x = self.pn
		temp = self.ecuacionTraducida.replace("x",str(self.pn))
		exec temp
		#exec self.ecuacionTraducida
		self.FPn = y
	def setPn(self):
		self.pn = (self.a+self.b)/2
	def getPn():
		return self.pn
	def getFPn(self):
		return self.FPn
	def traducirEcua(self,ecuacion):
		self.ecuacionTraducida = ecuacion#"y = math.sqrt(x)-math.cos(x)"#en mi caso particular falta hacer la traduccion
	def setVar(self,x):
		self.x = x
	def printTable(self,iteracion):
		#print str(iteracion)+" | "+str(self.a)+" | "+str(self.b)+" | "+str(self.pn)+" | "+str(self.FPn)+" | \n"
		return str(iteracion)+" | "+str(self.a)+" | "+str(self.b)+" | "+str(self.pn)+" | "+str(self.FPn)+" | \n"

class Window(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(800, 600))
		self.contenido = wx.TextCtrl(self, style=wx.TE_READONLY|wx.TE_MULTILINE)
		self.CreateStatusBar()

		menu_epsilon = wx.Menu()
		menu_biseccion = wx.Menu()
		menu_herramientas = wx.Menu()

		menu_generar = menu_epsilon.Append(wx.ID_SAVE,"Generar Epsilon")
		menu_limpiar = menu_herramientas.Append(2,"Limpiar Pantalla")
		menu_ecua = menu_biseccion.Append(3,"Ingresar Ecuacion ")
		menu_exit = menu_herramientas.Append(wx.ID_EXIT, "Salir")

		menubar = wx.MenuBar()
		menubar.Append(menu_epsilon, "Epsilon")
		menubar.Append(menu_biseccion, "Biseccion")
		menubar.Append(menu_herramientas, "Herramientas")
		self.SetMenuBar(menubar)

		self.Bind(wx.EVT_MENU, self.on_generar,menu_generar)
		self.Bind(wx.EVT_MENU, self.on_limpiar,menu_limpiar)
		self.Bind(wx.EVT_MENU, self.on_biseccion,menu_ecua)
		self.Bind(wx.EVT_MENU, self.on_exit, menu_exit)

		self.Centre(True)
		self.Show(True)
	def on_generar(self,event):
		#self.contenido = wx.TextCtrl(self, style=wx.TE_READONLY)
		epsilon = self.epsilon()
		self.contenido.SetValue(epsilon)
		self.contenido.Show()
		self.contenido2.Hide()
		self.contenido3.Hide()
		self.contenido4.Hide()
		self.contenido2.Hide()
		self.contenido3.Hide()
		self.contenido4.Hide()
	def on_limpiar(self,event):
		self.contenido.SetValue("")
		self.contenido.Show()
		self.contenido2.Hide()
		self.contenido3.Hide()
		self.contenido4.Hide()
		self.contenido2.Hide()
		self.contenido3.Hide()
		self.contenido4.Hide()
	def epsilon(self):
		tempEpsilon = float(1)
		i=0
		while float(1)+float(tempEpsilon) != float(1):
			i+=0
			tempEpsilonReal = tempEpsilon
			tempEpsilon = float(tempEpsilon) / float(2)
		i = 0
		tempEpsilon = 1.0
		while tempEpsilon+1.0>1.0:
			i += 1
			tempEpsilon = tempEpsilon/2.0
		i = 0
		tempFloatEpsilon = float(1)
		while tempFloatEpsilon+float(1.0)>float(1.0):
			i += 1
			tempFloatEpsilon = tempFloatEpsilon/float(2.0)
		return "Double"+str(tempEpsilon)+"\nFloat: "+str(tempFloatEpsilon)+"\nEpsilon sugerido por python: "+str(tempEpsilonReal)
	def on_exit(self, event):
		self.Close(True)
	def on_evalbiseccion(self,event):
		wx.MessageBox('Evaluando ...', 'Info', wx.OK | wx.ICON_INFORMATION)
		ecuacion = str(self.contenido2.GetValue())
		a = float(self.contenido3.GetValue())
		b = float(self.contenido4.GetValue())
		nitera = float(self.contenido5.GetValue())
		bisecc = Biseccion(ecuacion,a,b)
		self.contenido.Show()
		self.contenido2.Hide()
		self.contenido3.Hide()
		self.contenido4.Hide()
		self.contenido2.Hide()
		self.contenido3.Hide()
		self.contenido4.Hide()
		i = 0
		fpn = 99.9
		while fpn!=0.0:
			i += 1
			bisecc.setPn()
			bisecc.setFa()
			bisecc.setFPn()
			echo = bisecc.printTable(i)
			self.contenido.AppendText(echo)
			bisecc.setAorB()
			fpn = bisecc.getFPn()
			if nitera!=0.0:
				if i==nitera:
					break
	def on_biseccion(self,event):
		#self.labelContenido = wx.StaticText(self, size=(200, 50), id= -1,pos=(100, 0),label="Ecuacion")
		self.contenido.Hide()
		self.contenido2 = wx.TextCtrl(self, size=(200, 50), id= -1,pos=(150, 0))
		self.contenido3 = wx.TextCtrl(self, size=(200, 50), id= -1, pos=(150, 55))
		self.contenido4 = wx.TextCtrl(self, size=(200, 50), id= -1, pos=(150, 110))
		self.contenido5 = wx.TextCtrl(self, size=(200, 50), id= -1, pos=(150, 170))
		self.button = wx.Button(self, id = -1, label="Evaluar", pos=(100, 230), size=(130, 50)) 
		self.lab2 = wx.StaticText(self, id = -1, pos=(10, 10), size=(130, 50),label="Ecuacion: ",style= wx.BOLD) 
		self.lab3 = wx.StaticText(self, id = -1, pos=(10, 65), size=(130, 50),label="Limite Inferior: ") 
		self.lab4 = wx.StaticText(self, id = -1, pos=(10, 120), size=(130, 50),label="Limite Superior: ") 
		self.lab5 = wx.StaticText(self, id = -1, pos=(10, 180), size=(130, 50),label="N. Iteraciones: ") 
		self.contenido2.AppendText("Ecuacion")
		self.contenido3.AppendText("Primer Limite")
		self.contenido4.AppendText("Segundo Limite")
		self.contenido5.AppendText("0")

		self.Bind(wx.EVT_BUTTON, self.on_evalbiseccion,self.button)
		#Ayudita
		pnl1 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER,pos=(400, 10), size=(350, 500))
		self.lab3 = wx.StaticText(pnl1, id = -1, pos=(10, 10), size=(200, 50),label="AYUDA") 
		self.lab3 = wx.StaticText(pnl1, id = -1, pos=(10, 25), size=(400, 400),label="Para Generar Ecuaciones Tenga encuenta:\nRaiz: math.sqrt(x)"+"\nLogaritmo: math.log(x[, base])"+"\nRaiz Cuadrada: math.sqrt(x[, base])"+"\nPotencias: math.pow(x[, int])"+"\nArc Coseno: math.acos(x)"+"\nCos: math.cos(x)"+"\nSeno: math.sin(x)"+"\nArc Seno: math.asin(x)"+"\nTan: math.tan(x)"+"\nPI: math.pi"+"\ne: math.e\n\nPara ingresar numeros enteros a las ecuacion debe ingresarlos con puntos 1 = 1.0 en la ecuacion debe anteponer y=\nEjemplos de ecuaciones: \n\ty=3.0*(x+1.0)*(x-(1.0/2.0))*(x-1.0)\n\ty = math.sqrt(x)-math.cos(x)") 
		self.lab3 = wx.StaticText(pnl1, id = -1, pos=(10, 400), size=(200, 200),label="No Iteraciones = 0 --> Genera Todas las Iteraciones") 
		#ENDAyudita
		wx.MessageBox('Ingrese Su Ecuacion', 'Info', wx.OK | wx.ICON_INFORMATION)
		self.contenido2.SetFocus()
app = wx.App(False)
frame = Window(None, "Epsilon")
app.MainLoop()