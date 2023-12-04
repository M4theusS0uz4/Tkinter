from tkinter import*
import string
import random
from tkinter import messagebox

#Cores
cor= "#444466" #preto
cor1= "#feffff"#branco
cor2= "#f05a43"#vermelho
janela=Tk()
janela.title("Gerador de Senhas")
janela.geometry("350x400")
janela.config(bg=cor1)

#Criando partes
parte_cima = Frame(janela, width=350, height=50,bg=cor1, padx=0, relief='flat')
parte_cima.grid(row= 0,column=0,sticky=NSEW)


parte_baixo = Frame(janela, width=350, height=350,bg=cor,padx=0, relief='flat')
parte_baixo.grid(row= 1,column=0,sticky=NSEW)


#Frame de cima
nome_gera =Label(parte_cima, text="GERADOR DE SENHAS", height= 1,width=20,bg=cor1, fg=cor, anchor=NW, font=('Ivy 16 bold'),padx= 0)
nome_gera.pack()
linha_cima =Label(parte_cima, text="", height= 1,width=350,bg=cor2, fg=cor, anchor=NW, font=('Ivy 1'),padx= 0)
linha_cima.pack()



#função Gerar Senha
def gerar():
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = "123456789101112131415"
    simbolos = "{}(),*-/,@"

    global combinar

    if estado1.get() == alfabeto_maior:
        combinar= alfabeto_maior
    else:
        pass
    if estado2.get()== alfabeto_menor:
        combinar+=alfabeto_menor
    else:
        pass
    if estado4.get() == numeros:
        combinar+= numeros
    else:
        pass
    if estado3.get() == simbolos:
        combinar+= simbolos
    else:
        pass

    comprimento = int(spin.get())
    senha = "".join(random.sample(combinar, comprimento))
    gerar_senha['text'] = senha

    def copiar_senha():
        info = senha
        parte_baixo.clipboard_clear()
        parte_baixo.clipboard_append(info)

        messagebox.showinfo("Sucesso", "A senha foi copiada com sucesso!")

    #Botão copy
    gerar_copiar =Button(parte_baixo, text="Copiar",command= copiar_senha, height= 2,width=7,overrelief=SOLID, bg=cor1, fg=cor, anchor=CENTER, font=('Ivy 10 bold'),padx= 0)
    gerar_copiar.grid(row=0,column=1,sticky=NW,padx= 5,pady=5, columnspan= 1) 

#Frame baixo
gerar_senha =Label(parte_baixo, text="- - - - -", height= 2,width=32,bg=cor1, fg=cor, anchor=CENTER, font=('Ivy 10 bold'),padx= 0)
gerar_senha.grid(row=0,column=0, columnspan=1,sticky=NSEW,padx=5,pady=10)


gerar_info =Label(parte_baixo, text="Número total de dígitos", height= 1,bg=cor1, fg=cor, anchor=NW, font=('Ivy 10 bold'),padx= 0)
gerar_info.grid(row=1,column=0, columnspan=2,sticky=NSEW,padx=5,pady=1)

var= IntVar()
var.set(8)
spin = Spinbox(parte_baixo,from_= 0, to=20,width= 5, textvariable=var)
spin.grid(row=2,column=0, columnspan=2,sticky=NW,padx=5,pady=8)

alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = "123456789101112131415"
simbolos = "{}(),*-/,@"

parte_caracters = Frame(parte_baixo, width=350, height=210,bg=cor, padx=0, relief='flat')
parte_caracters.grid(row= 3,column=0,sticky=NSEW, columnspan=3)
#Parte letras maíusculas
estado1=  StringVar()
estado1.set(False)
check_1 = Checkbutton(parte_caracters, width=1, var= estado1, onvalue= alfabeto_maior, offvalue=OFF, relief= FLAT, bg=cor1)
check_1.grid(row=0, column=0,sticky=NW, padx= 5, pady=5)
gerar_info =Label(parte_caracters, text="ABC letras maíusculas", height= 1,bg=cor1, fg=cor, anchor=NW, font=('Ivy 10 bold'),padx= 0)
gerar_info.grid(row=0,column=1,sticky=NW,padx=2,pady=5)

#Parte letras mínusculas
estado2=  StringVar()
estado2.set(False)
check_2 = Checkbutton(parte_caracters, width=1, var= estado2, onvalue= alfabeto_menor, offvalue=OFF, relief= FLAT, bg=cor1)
check_2.grid(row=1, column=0,sticky=NW, padx= 5, pady=5)
gerar_info =Label(parte_caracters, text="abc letras mínusculas", height= 1,bg=cor1, fg=cor, anchor=NW, font=('Ivy 10 bold'),padx= 0)
gerar_info.grid(row=1,column=1,sticky=NW,padx=2,pady=5)

#Parte símbolos
estado3=  StringVar()
estado3.set(False)
check_3 = Checkbutton(parte_caracters, width=1, var= estado3, onvalue= simbolos, offvalue=OFF, relief= FLAT, bg=cor1)
check_3.grid(row=2, column=0,sticky=NW, padx= 5, pady=5)
gerar_info =Label(parte_caracters, text="@-, Símbolos", height= 1,bg=cor1, fg=cor, anchor=NW, font=('Ivy 10 bold'),padx= 0)
gerar_info.grid(row=2,column=1,sticky=NW,padx=2,pady=5)

#Parte números
estado4=  StringVar()
estado4.set(False)
check_4 = Checkbutton(parte_caracters, width=1, var= estado4, onvalue= numeros, offvalue=OFF, relief= FLAT, bg=cor1)
check_4.grid(row=3, column=0,sticky=NW, padx= 5, pady=5)
gerar_info =Label(parte_caracters, text="123 Números", height= 1,bg=cor1, fg=cor, anchor=NW, font=('Ivy 10 bold'),padx= 0)
gerar_info.grid(row=3,column=1,sticky=NW,padx=2,pady=5)

#Botão
gerar_botao =Button(parte_caracters,command=gerar, text="Gerar Senha", height= 1,width=32,overrelief=SOLID, bg=cor2, fg=cor1, anchor=CENTER, font=('Ivy 10 bold'),padx= 0)
gerar_botao.grid(row=5,column=0,sticky=NSEW,padx= 40,pady=20, columnspan= 5) 






janela.mainloop()