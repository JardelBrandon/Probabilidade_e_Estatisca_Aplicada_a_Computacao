'''
Questão 3): 

A tabela abaixo apresenta uma distribuição de frequência das áreas de 400 lotes:

    Áreas (m²)  | 300 |-- 400 |-- 500 |-- 600 |-- 700 |-- 800 |-- 900 |-- 1.000 |-- 1.100 |-- 1.200
    Nº de Lotes |     14      46      58      76      68      62      48        22        6       
       
Determine:
    a) O limite inferior da quinta classe 
    b) O ponto médio da sétima classe 
    c) A amplitude do intervalo da sexta classe
    d) A frequência da quarta classe 
    e) A frequência relativa da sexta classe 
    f) A frequência acumulada da quinta classe
    g) O número de lotes cuja área não atinge 700 m²
    h) O número de lotes igual ou maior a 800 m²
    i) A porcentagem dos lotes cuja área não atinge 600 m²
    j) A porcentagem dos lotes cuja área é de 500 m², 
    no mínimo, mas inferior a 1.000 m²
'''

print("a) O limite inferior da quinta classe: 700")
print("b) O ponto médio da sétima classe: 950")
print("c) A amplitude do intervalo da sexta classe:", 900-800)
print("d) A frequência da quarta classe: 76")# OU frequência absoluta
print("e) A frequência relativa da sexta classe:", ((62/(14+46+58+76+68+62+48+22+6)* 100)), "%")
print("f) A frequência acumulada da quinta classe:", (14+46+58+76+68))
print("g) O número de lotes cuja área não atinge 700 m²:", (14+46+58+76))
print("h) O número de lotes igual ou maior a 800 m²", (62+48+22+6))
print("i) A porcentagem dos lotes cuja área não atinge 600 m²:", ((14+46+58)/(14+46+58+76+68+62+48+22+6)*100), "%")
print("j) A porcentagem dos lotes cuja área é de 500 m², no mínimo, mas inferior a 1.000 m²:",
      ((58+76+68+62+48)/(14+46+58+76+68+62+48+22+6)*100), "%")