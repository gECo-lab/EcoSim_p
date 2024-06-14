# iterate over two dicitionaries as stacks 

demanda = {'a': 111, 'c': 155, 'd': 493}
oferta = {'x': 100, 'y': 120, 'z': 3320}

demanda_nao_satisfeita = True

for di in demanda:
     esta_demanda = 0.0
     qdi = demanda[di]
     while demanda_nao_satisfeita:
          oj = next(iter(oferta))
          qoj = oferta[oj]
          if qdi > qoj:
               esta_demanda += qoj
               demanda[di] -= qoj
               of = oferta.pop(oj)
          elif qdi == qoj:
               esta_demanda += qoj
               demanda[di] -= qoj
               demanda_nao_satisfeita = False
               of = oferta.pop(oj)
          else:
               esta_demanda += qdi
               demanda[di] = 0
               oferta[oj] -= qdi
               demanda_nao_satisfeita = False
          print(di, qdi, oj, qoj, esta_demanda) 
          print(demanda)
          print(oferta)

  