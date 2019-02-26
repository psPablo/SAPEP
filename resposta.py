import csv
from v1 import decisao

with open('./operacoesAterrissagem.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=';')
    i = 0
    resultado = []
    for row in readCSV:
        distanciaOcupada = 0;
        if i > 0:
            resultado = decisao.decisao(row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]);
            print(i,';',row[4],';',row[5],';',row[6],';',row[7],';',row[8],';',row[9],';',row[10],';',row[11],';',row[12],';',resultado['distanciaOcupada'],';',resultado['distanciaRequerida'],';',resultado['porcentagemDistanciaRequerida'])
        else:
            print('Name',';',row[4],';',row[5],';',row[6],';',row[7],';',row[8],';',row[9],';',row[10],';',row[11],';',row[12],';distanciaOcupada;distanciaRequerida;porcentagemDistanciaRequerida')
        i = i+1

