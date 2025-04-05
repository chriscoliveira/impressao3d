import math
kwh=1.00
fonte=350

def calculaEnergia(kwh,fonteW,tempo):
    energia = (kwh/1000*fonte)*(tempo/60)
    #print(f"energia {round(energia,2)}")
    return round(energia,2)

def calculaCustoMaterial(kg,peso):
    custo = (kg/1000)*peso
    #print(f'custo material {round(custo,2)}')
    return round(custo,2)

def converteMinutos(hora):
    if ":" in hora:
        horas, minutos = map(int, hora.split(":"))  # Exemplo: "2:30" (2 horas e 30 minutos)
        total_minutos = horas * 60 + minutos
        #print(f"minutos {total_minutos}")
        return total_minutos  # Saída: 150
    else:
        #print(f"minutos {hora}")
        return hora

def calculaPeso(tipo,metros):
    #print(tipo)
    if tipo == 'ABS':
        tipo =  1.04

    elif tipo == "PLA":
        tipo = 1.24
    #print(tipo)
    # =C6*1,24*(PI()*((1,75/2)^2))

    # Exemplo de valor para C6 (metros de ABS usados)
    peso = metros * tipo * (math.pi * ((1.75 / 2) ** 2))

    #print(f"peso {round(peso,2)}")

    return round(peso,2)

def custoManutencao(custoMaterial):
    custo = custoMaterial * 0.15
    #print(f'custo material {custo}')
    return round(custo,2)

def custoFalha(custoMaterial):
    custo = custoMaterial * 0.10
    #print(f'custo falha {round(custo,2)}')
    return round(custo,2)

def custoAcabamento(custoMaterial):
    custo = custoMaterial * 0.10
    #print(f'custo acabamento {round(custo,2)}')
    return round(custo,2)

def valorProducao(material,valorkg, metragem, tempo):

    peso = calculaPeso(material, metragem)
    tempo = converteMinutos(tempo)
    customaterial = calculaCustoMaterial(valorkg,peso)
    energia = calculaEnergia(kwh,fonte,tempo)
    customanutencao = custoManutencao(customaterial)
    custofalha = custoFalha(customaterial)
    custoacabamento = custoAcabamento(customaterial)
    producao = round(customaterial + energia + customanutencao + custofalha + custoacabamento,2)
    
    print(f'''
Material usado:      {material}
Filamento usado:     {metragem}
Tempo gasto:         {tempo} minutos
Peso total:          {peso}g

Custo do material:   R${customaterial}
Custo de Manutenção: R${customanutencao}
Custo de energia:    R${energia}
Custo de Falhas:     R${custofalha}
Custo de acabamento: R${custoacabamento}
Custo de produção:   R${producao}
''')

    # return material, metragem, peso, tempo, customaterial, customanutencao, energia, custofalha, custoacabamento, producao
    return producao

def valorVenda(valorProducao,lucro,pintura,outrosValores):
    final = valorProducao +(valorProducao * (lucro/100)+ pintura + outrosValores)
    print(f'Valor final para venda R${final}')
    

tipofilamento = input("Qual o filamento sera usado: ")
valorkg = float(input("Qual o valor do Kg do filamento: "))
metros = float(input("Quantos metros foi usado? "))
minutos = input("Qual a duração da impressão? " )
lucro= float(input("qual a porcentagem de lucro? (nao colocar o %) "))
vproducao = valorProducao(tipofilamento,valorkg,metros,minutos)

valorVenda(vproducao,lucro,0,0)