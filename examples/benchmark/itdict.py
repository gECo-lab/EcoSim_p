import random

# iterate over two dicitionaries as stacks 



demanda = {}
letters = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(10):
     key = random.choice(letters)
     value = random.randint(1, 500)
     demanda[key] = value


oferta = {}
for _ in range(10):
     key = random.choice(letters)
     value = random.randint(100, 1000)
     oferta[key] = value

qoj = 0

for di in demanda:
     esta_demanda = 0.0
     qdi = demanda[di]
     print("demanda: ", demanda)
  
     if oferta:
         demanda_nao_satisfeita = True
     else:
         demanda_nao_satisfeita = False
         break  
     while demanda_nao_satisfeita:
        print("oferta: ",oferta)

        if oferta:
           oj = next(iter(oferta))
           qoj = oferta[oj]
        elif qoj == 0:
           demanda_nao_satisfeita = False
        if qdi > qoj:
             esta_demanda += qoj
             demanda[di] -= qoj
             qdi -= qoj
             qoj = 0
             if oferta:
                of = oferta.pop(oj)
        elif qdi == qoj:
             esta_demanda += qdi
             demanda[di] = 0
             oferta[oj] = 0
             qoj = 0 
             demanda_nao_satisfeita = False
             if oferta:
                of = oferta.pop(oj)
        elif qoj > qdi:
             esta_demanda += qdi
             demanda[di] = 0
             oferta[oj] -= qdi 
             qoj -= qdi
             qdi = 0
             demanda_nao_satisfeita = False
        print(di, qdi, oj, qoj, esta_demanda)

print("demanda final: ", demanda) 
print("oferta final: ", oferta)
  
