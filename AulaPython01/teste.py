from tkinter import *

#Função para printar os valores os valores.

def valor(self):
    nome = enntry_palavra.get()
    print(nome)
    


#Crinado a janela para digitar os valores.

janela = Tk()
janela.title('Entry')
janela.geometry('400x100')



label_palavra = Label(janela, width=15, height=2, text='Escreva a palavra: ', font=('Arial 15'))
label_palavra.grid(row=0, column=0)
enntry_palavra = Entry(janela, width=25, font=('Arial 10'))
enntry_palavra.grid(row=0, column=1, padx=10, pady=5)

#Pegando os valores com o ENTER.
janela.bind('<Return>', valor)

janela.mainloop()



