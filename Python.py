meses = [00,31,28,31,30,31,30,31,31,30,31,30,31]
dia_i = mes_i = ano_i = dia_f = mes_f = ano_f = 0
dia_i = int (input("Digite o dia inicial"))
mes_i = int (input("Digite o mês inicial"))
ano_i = int (input("Digite o ano inicial"))
dia_f = int (input("Digite o dia final"))
mes_f = int (input("Digite o mês final"))
ano_f = int (input("Digite o ano final"))

if (ano_i % 4 == 0) and (ano_i % 100 != 0) or (ano_i % 400 == 0):
    meses[2] = 29
else: meses[2] = 28
    
qt_dias = 0
while (dia_i != dia_f) or (mes_i != mes_f) or (ano_i != ano_f):
    qt_dias = qt_dias + 1
    dia_i = dia_i + 1
    if dia_i > meses[mes_i]:
        mes_i = mes_i + 1
        dia_i = 1
        if mes_i > 12:
            ano_i = ano_i + 1
            mes_i = 1
            if (ano_i % 4 == 0) and (ano_i % 100 != 0) or (ano_i % 400 == 0):
                meses[2] = 29
            else: meses[2] = 28
print ("A nova data é: {:02}/{:02}/{:04}".format(dia_i,mes_i,ano_i))
print ("Se passaram: ", qt_dias, "dias")