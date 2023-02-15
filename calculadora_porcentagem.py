from tkinter import *

janela = Tk()
janela.title("Calculadora de porcentagem")
janela.geometry("400x400")
janela.configure(background='yellow')


fontePadrao = ("Arial", "20")
fonteSecundaria = ("Arial", "15")

def a():     
    texto1 = Label(janela, text="Digite o número da letra b: ", font=fonteSecundaria, bg='yellow')
    texto1.grid(column=12, row=2)
    valor1 = Entry(janela, width=20)    
    valor1.grid(column=12, row=3)

    texto2 = Label(janela, text="Digite o número da letra c: ", font=fonteSecundaria, bg='yellow')
    texto2.grid(column=12, row=4)
    valor2 = Entry(janela, width=20)
    valor2.grid(column=12, row=5)

    texto3 = Label(janela, text="Digite o número da letra d: ", font=fonteSecundaria, bg='yellow')
    texto3.grid(column=12, row=6)
    valor3 = Entry(janela, width=20)
    valor3.grid(column=12, row=7) 
      
    def calcula():
        b = float(valor1.get())
        c = float(valor2.get())
        d = float(valor3.get())
        resultado = (c*b)/d 
        valor_final["text"] = f'''O resultado é {round(resultado,2)}'''
    botao = Button(janela, text="Prosseguir", command=calcula, font=fonteSecundaria, bg='yellow')
    botao.grid(column=12, row=8)
def b():     
    texto1 = Label(janela, text="Digite o número da letra a: ", font=fonteSecundaria, bg='yellow')
    texto1.grid(column=12, row=2)
    valor1 = Entry(janela, width=20)    
    valor1.grid(column=12, row=3)

    texto2 = Label(janela, text="Digite o número da letra c: ", font=fonteSecundaria, bg='yellow')
    texto2.grid(column=12, row=4)
    valor2 = Entry(janela, width=20)
    valor2.grid(column=12, row=5)

    texto3 = Label(janela, text="Digite o número da letra d: ", font=fonteSecundaria, bg='yellow')
    texto3.grid(column=12, row=6)
    valor3 = Entry(janela, width=20)
    valor3.grid(column=12, row=7) 
      
    def calcula():
        a = float(valor1.get())
        c = float(valor2.get())
        d = float(valor3.get())
        resultado = (a*d)/c 
        valor_final["text"] = f'''O resultado é {round(resultado,2)}%'''
    botao = Button(janela, text="Prosseguir", command=calcula, font=fonteSecundaria, bg='yellow')
    botao.grid(column=12, row=8)

def c():     
    texto1 = Label(janela, text="Digite o número da letra a: ", font=fonteSecundaria, bg='yellow')
    texto1.grid(column=12, row=2)
    valor1 = Entry(janela, width=20)    
    valor1.grid(column=12, row=3)

    texto2 = Label(janela, text="Digite o número da letra b: ", font=fonteSecundaria, bg='yellow')
    texto2.grid(column=12, row=4)
    valor2 = Entry(janela, width=20)
    valor2.grid(column=12, row=5)

    texto3 = Label(janela, text="Digite o número da letra d: ", font=fonteSecundaria, bg='yellow')
    texto3.grid(column=12, row=6)
    valor3 = Entry(janela, width=20)
    valor3.grid(column=12, row=7) 
      
    def calcula():
        a = float(valor1.get())
        b = float(valor2.get())
        d = float(valor3.get())
        resultado = (a*d)/b
        valor_final["text"] = f'''O resultado é {round(resultado,2)}'''
    botao = Button(janela, text="Prosseguir", command=calcula, font=fonteSecundaria, bg='yellow')
    botao.grid(column=12, row=8)

def d():     
    texto1 = Label(janela, text="Digite o número da letra a: ", font=fonteSecundaria, bg='yellow')
    texto1.grid(column=12, row=2)
    valor1 = Entry(janela, width=20)    
    valor1.grid(column=12, row=3)

    texto2 = Label(janela, text="Digite o número da letra b: ", font=fonteSecundaria, bg='yellow')
    texto2.grid(column=12, row=4)
    valor2 = Entry(janela, width=20)
    valor2.grid(column=12, row=5)

    texto3 = Label(janela, text="Digite o número da letra c: ", font=fonteSecundaria, bg='yellow')
    texto3.grid(column=12, row=6)
    valor3 = Entry(janela, width=20)
    valor3.grid(column=12, row=7) 
      
    def calcula():
        a = float(valor1.get())
        b = float(valor2.get())
        c = float(valor3.get())
        resultado = (c*b)/a 
        valor_final["text"] = f'''O resultado é {round(resultado,2)}%'''
    botao = Button(janela, text="Prosseguir", command=calcula, font=fonteSecundaria, bg='yellow')
    botao.grid(column=12, row=8)
    
#Primeira tela
#Primeira linha
botao_a = Button(janela, text="a",command=a, font=fontePadrao, bg='light blue')
botao_a.grid(column=12, row=0, padx=5, pady=5)

traco1 = Label(janela, text="-", font=fontePadrao, bg='yellow')
traco1.grid(column=13, row=0, padx=5, pady=5)

botao_b = Button(janela, text="b", command=b, font=fontePadrao, bg='light blue')
botao_b.grid(column=14, row=0, padx=0, pady=0)
porcentagem1 = Label(janela, text="%", font=fontePadrao, bg='yellow')
porcentagem1.grid(column=15, row=0)

#Segunda linha
botao_c = Button(janela, text="c", command=c, font=fontePadrao, bg='light blue')
botao_c.grid(column=12, row=1, padx=5, pady=5)

traco2 = Label(janela, text="-", font=fontePadrao, bg='yellow')
traco2.grid(column=13, row=1, padx=5, pady=5)

botao_d = Button(janela, text="d", command=d, font=fontePadrao, bg='light blue')
botao_d.grid(column=14, row=1, padx=10, pady=10)
porcentagem1 = Label(janela, text="%", font=fontePadrao, bg='yellow')
porcentagem1.grid(column=15, row=1)

#Resultado
valor_final = Label(janela, text="", font=fonteSecundaria, bg='yellow')
valor_final.grid(column=12, row=9, padx=10, pady=10)

janela.mainloop()