import turtle

tela = turtle.Screen()
tela.bgcolor("light green")

caneta = turtle.Turtle()
caneta.color("white")
caneta.speed(2001)
caneta.fillcolor("red")
caneta.begin_fill()
caneta.ht()

caneta.forward(400)
caneta.left(90)
caneta.forward(300)
caneta.left(90)
caneta.forward(800)
caneta.left(90)
caneta.forward(300)
caneta.left(90)
caneta.forward(400)
caneta.left(90)
caneta.end_fill()

caneta.penup()
caneta.forward(260)
caneta.left(90)
caneta.forward(400)
caneta.pendown()
caneta.left(180)

caneta.fillcolor("white")
caneta.begin_fill()
caneta.forward(40)
caneta.right(90)
caneta.forward(3)
caneta.right(90)
caneta.forward(40)
caneta.end_fill()

caneta.penup()
caneta.left(90)
caneta.forward(50)
caneta.left(90)
caneta.pendown()
caneta.fillcolor("white")
caneta.begin_fill()
caneta.forward(40)
caneta.right(90)
caneta.forward(3)
caneta.right(90)
caneta.forward(40)
caneta.end_fill()

caneta.penup()
caneta.left(90)
caneta.forward(50)
caneta.left(90)
caneta.pendown()
caneta.fillcolor("white")
caneta.begin_fill()
caneta.forward(40)
caneta.right(90)
caneta.forward(3)
caneta.right(90)
caneta.forward(40)
caneta.end_fill()

caneta.penup()
caneta.left(90)
caneta.forward(50)
caneta.left(90)
caneta.pendown()
caneta.fillcolor("white")
caneta.begin_fill()
caneta.forward(40)
caneta.right(90)
caneta.forward(3)
caneta.right(90)
caneta.forward(40)
caneta.end_fill()

caneta.penup()
caneta.left(90)
caneta.forward(50)
caneta.left(90)
caneta.pendown()
caneta.fillcolor("white")
caneta.begin_fill()
caneta.forward(40)
caneta.right(90)
caneta.forward(3)
caneta.right(90)
caneta.forward(40)
caneta.end_fill()


caneta.penup()
caneta.forward(-800)
caneta.fillcolor("white")
caneta.begin_fill()
caneta.pendown()
caneta.forward(40)
caneta.right(90)
caneta.forward(3)
caneta.right(90)
caneta.forward(40)
caneta.end_fill()

caneta.penup()
caneta.left(90)
caneta.forward(50)
caneta.left(90)
caneta.fillcolor("white")
caneta.begin_fill()
caneta.forward(40)
caneta.right(90)
caneta.forward(3)
caneta.right(90)
caneta.forward(40)
caneta.end_fill()

caneta.penup()
caneta.left(90)
caneta.forward(50)
caneta.left(90)
caneta.fillcolor("white")
caneta.begin_fill()
caneta.forward(40)
caneta.right(90)
caneta.forward(3)
caneta.right(90)
caneta.forward(40)
caneta.end_fill()

caneta.penup()
caneta.left(90)
caneta.forward(50)
caneta.left(90)
caneta.fillcolor("white")
caneta.begin_fill()
caneta.forward(40)
caneta.right(90)
caneta.forward(3)
caneta.right(90)
caneta.forward(40)
caneta.end_fill()

caneta.penup()
caneta.left(90)
caneta.forward(50)
caneta.left(90)
caneta.fillcolor("white")
caneta.begin_fill()
caneta.forward(40)
caneta.right(90)
caneta.forward(3)
caneta.right(90)
caneta.forward(40)
caneta.end_fill()

caneta.home()
caneta.forward(-15)
caneta.left(90)
caneta.penup()

txt = input("Digite o seu nome")
texto = str(txt)
num = int(len(texto))
num2 = int(num)


print(num)
print(num2)
print(texto)
print(txt)

tamanho = int((140000//num2)/170)
if tamanho < 250:
    fonte = ("Arial", tamanho, "italic")
    
    if tamanho < 170 and tamanho > 130:
            tamanho = tamanho*0.25
    elif tamanho <= 130 and tamanho > 90:
            tamanho = tamanho*0.8
    elif tamanho < 90 and tamanho > 50:
            tamanho = tamanho*3
    else:
            fonte2 = ("Arial", 65, "italic")
            caneta.write("muitos caracteres!!!", False, "center", fonte2)
    caneta.forward(tamanho)
    print(tamanho)
    print(fonte)
    caneta.write(texto, False, "center", fonte)
else:
    print(tamanho)
    fonte2 = ("Arial", 65, "italic")
    caneta.write("muitos caracteres!!!", False, "center", fonte2)
