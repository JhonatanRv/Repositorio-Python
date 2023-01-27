#vo = int(input("Entre com a velocidade: "))
#a = int(input("Entre com o tempo: "))
#t = int(input("Entre com a aceleração: "))

#vf = vo + a * t

#print ("A velocidade final é igual a: ", vf)

#so = int(input("Entre com o espaço: "))
#vo = int(input("Entre com o velocidade: "))
#a = int(input("Entre com a aceleração: "))
#t = int(input("Entre com a tempo: "))

#s = so + vo * t + (a* t * t)/2


s = float(input("Entre com o espaço: "))
so = float(input("Entre com o espaço final: "))
t = float(input("Entre com o tempo: "))
to = float(input("Entre com a tempo final: "))

if (t == to):
    print("Insira um valor diferente")
else:
    print ("V é igual a: ", ((s - so) / (t - to)))