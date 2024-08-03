import math
import sqlite3

conn = sqlite3.connect('impressao3d.db')

cursor = conn.cursor()


retornoInvestimento = 1.85

def criabanco():
    try:
        cursor.execute("""
        CREATE TABLE PRODUTOS (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                ITEM TEXT NOT NULL,
                VALORVENDA TEXT,
                VALORPRODUCAO TEXT,
                LUCROPCT TEXT,
                MATERIAL TEXT,
                VALORFILKG TEXT,
                CUSTOPINTURA TEXT,
                TEMPOPRODUCAO TEXT,
                TEMPOPRODUCAOMINUTOS TEXT,
                FILAMENTOM TEXT,
                PESO TEXT,
                ALTURACM TEXT,
                TAMANHOPCT TEXT,
                ALTURACAMADA TEXT,
                INFILL TEXT,
                SUPORTE TEXT,
                OUTROS TEXT,
                LINK TEXT
        );
        """)
    except Exception as e:
        ...
criabanco()


def calculaValorVenda(valorProducao,lucro,custoPintura):
    resultado = valorProducao+(valorProducao*lucro)+custoPintura
    return float("%.2f" % round(resultado,2))

def calculaPeso(metros,diametro=1.75):
    resultado = metros * 1.24 * (math.pi * ((diametro / 2) ** 2))

    return float("%.2f" % round(resultado,2))

def calculaCustoMaterial(valorkg,pesog):
    return float("%.2f" % round((float(valorkg)/1000)*float(pesog),2))

def calculaCustoEnergia(kwh,tempomin):
    return float("%.2f" % round(((float(kwh)/1000)*350)*tempomin/60,2))

def calculaCustoManutencao(customaterial):
    return float("%.2f" % round(float(customaterial)*0.15,2))

def calculaCustoFalhas(customaterial):
    return float("%.2f" % round(float(customaterial)*0.10,2))

def calculaCustoAcabamento(customaterial):
    return float("%.2f" % round(float(customaterial)*0.10,2))

def converteHoraEmMinutos(tempo):
    # Divide o horário na parte de horas e minutos
    partes = tempo.split(':')
    horas = int(partes[0])
    minutos = int(partes[1])
    
    # Converte horas para minutos e soma com os minutos
    total_minutos = horas * 60 + minutos
    return int(total_minutos)

def calculaValorProducao(custoMaterial,custoEnergia,custoFalhas,custoManutencao,custoAcabamento):
    valorProducao=(float(custoMaterial)+float(custoEnergia)+float(custoFalhas)+float(custoManutencao)+float(custoAcabamento)+retornoInvestimento)
    valorProducao=float("%.2f" % round(valorProducao,2))
    return valorProducao

def calculaValorVenda(valorProducao,lucro,custopintura):
    valorVenda = valorProducao+(valorProducao*(int(lucro)/100))+float(custopintura)
    valorVenda = float("%.2f" % round(valorVenda,2))
    return valorVenda

def insereProduto(item,lucro,valorkg,custopintura,tempoproducao,material,filamentom,alturacm,tamanhopct,alturacamada,infill,suporte,outros,link):
    if custopintura =="":
        custopintura=0
    pesog = calculaPeso(float(filamentom))
    tempomin = converteHoraEmMinutos(tempoproducao)
    custoMaterial = calculaCustoMaterial(float(valorkg),pesog)
    custoEnergia = calculaCustoEnergia(1,tempomin)
    custoManutencao = calculaCustoManutencao(custoMaterial)
    custoFalhas = calculaCustoFalhas(custoMaterial)
    custoAcabamento = calculaCustoAcabamento(custoMaterial)

    valorProducao = calculaValorProducao(custoMaterial,custoEnergia,custoFalhas,custoManutencao,custoAcabamento)
    
    valorVenda = calculaValorVenda(valorProducao,lucro,custopintura)
    
    print(f'\n\n\n{valorProducao=}\n{valorVenda=}\n{lucro=}\n{custoEnergia=}\n{custoAcabamento=}\n{custoFalhas=}\n{custoMaterial=}\n{custoManutencao=}')
    
    cursor.execute(f"""INSERT INTO PRODUTOS 
                   (ITEM, VALORVENDA, VALORPRODUCAO, LUCROPCT, MATERIAL, VALORFILKG, CUSTOPINTURA, TEMPOPRODUCAO, TEMPOPRODUCAOMINUTOS, FILAMENTOM, PESO, ALTURACM, TAMANHOPCT, ALTURACAMADA, INFILL, SUPORTE, OUTROS, LINK)
                VALUES (
                   '{item}','{valorVenda}','{valorProducao}','{lucro}','{material}','{valorkg}','{custopintura}','{tempoproducao}','{tempomin}','{filamentom}','{pesog}','{alturacm}','{tamanhopct}','{alturacamada}','{infill}','{suporte}','{outros}','{link}')""")
    conn.commit()

def listaProduto(id=None):
    if id:
        cursor.execute(f'select * from PRODUTOS where id ={id}')

    else:
        cursor.execute('select * from PRODUTOS')

    rows = cursor.fetchall()
    # conn.close()
    retorno = []
    for row in rows:
        retorno.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18]])
    return retorno

# def atualizaProduto(id,item,lucro,valorkg,custopintura,tempoproducao,material,filamentom,alturacm,tamanhopct,alturacamada,infill,suporte,outros,link):
#     produtos = listaProduto(id)
    

def atualizaProduto(id,item,lucro,valorkg,custopintura,tempoproducao,material,filamentom,alturacm,tamanhopct,alturacamada,infill,suporte,outros,link):
    
    produtos = listaProduto(id)
    
    if produtos:
        if id:
            if custopintura =="":
                custopintura=0
            pesog = calculaPeso(float(filamentom))
            tempomin = converteHoraEmMinutos(tempoproducao)
            custoMaterial = calculaCustoMaterial(float(valorkg),pesog)
            custoEnergia = calculaCustoEnergia(1,tempomin)
            custoManutencao = calculaCustoManutencao(custoMaterial)
            custoFalhas = calculaCustoFalhas(custoMaterial)
            custoAcabamento = calculaCustoAcabamento(custoMaterial)
            valorProducao = calculaValorProducao(custoMaterial,custoEnergia,custoFalhas,custoManutencao,custoAcabamento)
            valorVenda = calculaValorVenda(valorProducao,lucro,custopintura)
            
            cursor.execute(f'''update PRODUTOS set item="{item}", valorvenda="{valorVenda}",valorproducao="{valorProducao}",
                        custopintura="{custopintura}",tempoproducao="{tempoproducao}",material="{material}",
                        filamentom="{filamentom}",alturacm="{alturacm}",tamanhopct="{tamanhopct}",alturacamada="{alturacamada}",
                        infill="{infill}",suporte="{suporte}",outros="{outros}",link="{link}",VALORFILKG="{valorkg}",lucropct="{lucro}",tempoproducaominutos="{tempomin}"
                        where id ={id}''')
            conn.commit()
    else:
        print("Erro ao atualizar")

# atualizaProduto(id=25,item="aaaaaa",lucro=300,valorkg=90,custopintura=10,tempoproducao="7:00",material="abs",filamentom=7.92,alturacm=12,tamanhopct="120%",alturacamada="0.16",infill="25%",suporte="sim",outros="aa",link="a")

# insereProduto(item="teste1",lucro=200,valorkg=100,custopintura=0,tempoproducao="2:22",material="PLA",filamentom=5.92,alturacm=10,tamanhopct="100%",alturacamada="0.2",infill="15%",suporte="sim",outros="",link="")
# listaProduto()
