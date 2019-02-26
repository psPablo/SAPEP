def gradientePista(distanciaPistaMin,gradient):
    return (distanciaPistaMin * ((gradient * 0.1)))

def tempoFlare(tempoFlare):
    return tempoFlare*200

def excessoAltura(altura):
    if altura > 50:
        return ((altura-50)/10)*200
    else:
        return 0

def implementacaoDispositivosDesacelaracao(tempo):
    if tempo > 2:
        return (tempo - 2)*200
    else:
        return 0

def aumentoPista(distanciaRequerida,distanciaAvaliadaDisponivel):
    return (distanciaRequerida/distanciaAvaliadaDisponivel)*100

def excessoVelocidade(distanciaRequerida,porcentagemAumentoVelocidade):
      calc = (porcentagemAumentoVelocidade/10)* 0.2 * distanciaRequerida
      return calc


def ventoCalda(distanciaRequerida,ventoCalda):
    return (ventoCalda/10) * 0.21 * distanciaRequerida

def dispositivoFrenagemMaxima(distanciaRequerida,frenagemMaxima):
    if int(frenagemMaxima) == 1:
        return distanciaRequerida * 0.2
    return 0

def condicaoPista(distanciaRequerida,statusPista):
    if int(statusPista) == 1:
        return (distanciaRequerida)*(0.15)
    return 0
