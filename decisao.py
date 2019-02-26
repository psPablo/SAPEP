from v1 import  processamento  as p

def decisao(_distanciaAvaliadaDisponivel,_gradientePista,_tempoFlare,_excessoAltura,_implementacaoDispositivoDesacelaracao,_excessoVelocidade,_ventoCalda,_dispostivoFrenageMaxima,_codicaoPista):
    distanciaPistaMin = float(_distanciaAvaliadaDisponivel) * 0.6
    gradiente = p.gradientePista(distanciaPistaMin,float(_gradientePista))
    tf = p.tempoFlare(float(_tempoFlare))
    ea = p.excessoAltura(float(_excessoAltura))
    ev = p.excessoVelocidade(distanciaPistaMin+gradiente,float(_excessoVelocidade))
    vc = p.ventoCalda(distanciaPistaMin+gradiente+ev,float(_ventoCalda))
    totalParcial = gradiente+tf+ea+ev+vc+distanciaPistaMin
    idd = p.implementacaoDispositivosDesacelaracao(float(_implementacaoDispositivoDesacelaracao))
    totalParcial = totalParcial + idd
    dfm = p.dispositivoFrenagemMaxima(totalParcial,int(_dispostivoFrenageMaxima))
    totalParcial = totalParcial+dfm
    cp = p.condicaoPista(totalParcial,int(_codicaoPista))
    totalParcial = totalParcial + cp
    total = totalParcial
    distanciaOcupada = gradiente+tf+ea+ev+vc+idd+dfm+cp
    distanciaRequerida = total
    porcentagemDistanciaRequerida = p.aumentoPista(distanciaRequerida,float(_distanciaAvaliadaDisponivel))
    return {'distanciaOcupada':distanciaOcupada,'distanciaRequerida':distanciaRequerida,'porcentagemDistanciaRequerida':porcentagemDistanciaRequerida}



