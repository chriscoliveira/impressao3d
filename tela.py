import matplotlib.pyplot as plt
from PyQt6.QtGui import QPixmap
import calendar
import pandas as pd
from datetime import datetime
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QStringListModel,Qt
from layout import Ui_MainWindow

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton,QMessageBox
import sqlite3
import math

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

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.showMaximized()

        self.frmCad.hide()
        self.frmLista.hide()
        self.frm_listavendido.hide()
        self.frmvenda.hide()
        self.frm_home.show()
        self.exibeResumo()

        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frm_listavendido.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frmvenda.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frmCad.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frmLista.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)

        self.btCalculadora.clicked.connect(self.abreCadastro)
        self.btLista.clicked.connect(self.abreLista)
        self.btVendas.clicked.connect(self.abreVendas)
        self.btGrava.clicked.connect(self.atualizaProduto)
        self.btLimpa.clicked.connect(self.limpacadastro)
        self.btCalcula.clicked.connect(self.calculaProduto)
        self.rbnaopago.clicked.connect(self.load_data_from_db_venda)
        self.rbpago.clicked.connect(self.load_data_from_db_venda)
        self.rbtodos.clicked.connect(self.load_data_from_db_venda)
        self.bt_buscaprod.clicked.connect(self.buscaitemvenda)
        self.bt_pesquisa.clicked.connect(self.load_data_from_db)
        self.bt_listarvendas.clicked.connect(self.listavendas)
        self.btgravavenda.clicked.connect(self.fazVenda)
        self.br_deletar.clicked.connect(self.deletaProduto)
        self.br_deletar2.clicked.connect(self.deletaVenda)
        self.bt_home.clicked.connect(self.abreHome)

        self.tableWidget.cellDoubleClicked.connect(self.printDoubleClickedItem)
        self.tableWidget_vendido.cellDoubleClicked.connect(self.printDoubleClickedItem_venda)

        self.exportPDF()

    def data(self,separado=None):
        current_dateTime = datetime.now()
        if separado:
            return [current_dateTime.day,current_dateTime.month,current_dateTime.year]
        else:
            return f'{current_dateTime.day}/{current_dateTime.month}/{current_dateTime.year}'


# muda telas    
    def abreHome(self):
        self.frmCad.hide()
        self.frmvenda.hide()
        self.frmLista.hide()
        self.frm_home.show()
        self.frm_listavendido.hide()
        self.exibeResumo()
    
    def abreCadastro(self):
        self.frmCad.show()
        self.frmvenda.hide()
        self.frmLista.hide()
        self.frm_home.hide()
        self.frm_listavendido.hide()
        self.limpacadastro()
        self.label_19.setText("Cadastrar Produto")
        self.btGrava.setText("Gravar")

    def abreVendas(self):
        self.frm_listavendido.hide()
        self.frmCad.hide()
        self.frm_home.hide()
        self.frmLista.hide()
        self.frmvenda.show()
        self.limpacadastro()
        self.btgravavenda.setText("Gravar")

    def listavendas(self):
        self.frmCad.hide()
        self.frm_listavendido.show()
        self.frmvenda.hide()
        self.frm_home.hide()
        self.frmLista.hide()
        self.load_data_from_db_venda()

    def abreLista(self):
        self.frmCad.hide()
        self.frm_listavendido.hide()
        self.frmvenda.hide()
        self.frm_home.hide()
        self.frmLista.show()
        self.load_data_from_db()

# carrega dados
    def load_data_from_db_venda(self):
        # Conectar ao banco de dados SQLite
        self.tableWidget_vendido.clear()
        
        if self.rbtodos.isChecked():
            # Consulta SQL para selecionar os dados
            cursor.execute("SELECT id_,ID,PRODUTO,COMPRADOR,DATA,VALORVENDA,PAGO,VALORPRODUTO,CUSTO,LUCRO,MATERIAL,ENERGIA,OBS FROM VENDA order by id_ desc")
        if self.rbpago.isChecked():
            # Consulta SQL para selecionar os dados
            cursor.execute("SELECT id_,ID,PRODUTO,COMPRADOR,DATA,VALORVENDA,PAGO,VALORPRODUTO,CUSTO,LUCRO,MATERIAL,ENERGIA,OBS FROM VENDA where pago='sim' order by id_ desc")
        if self.rbnaopago.isChecked():
            # Consulta SQL para selecionar os dados
            cursor.execute("SELECT id_,ID,PRODUTO,COMPRADOR,DATA,VALORVENDA,PAGO,VALORPRODUTO,CUSTO,LUCRO,MATERIAL,ENERGIA,OBS FROM VENDA where pago!='sim' order by COMPRADOR")

        rows = cursor.fetchall()
        numRows = len(rows)
        numCols = len(rows[0]) if numRows > 0 else 0

        self.tableWidget_vendido.setRowCount(numRows)
        self.tableWidget_vendido.setColumnCount(numCols)
        nomeColunas = ["ID_","ID","PRODUTO","COMPRADOR","DATA","VENDIDO","PAGO","VALOR","CUSTO","LUCRO","MATERIAL","ENERGIA","OBS"]
        self.tableWidget_vendido.setHorizontalHeaderLabels(nomeColunas)

        for rowIndex, row in enumerate(rows):
            for colIndex, value in enumerate(row):
                self.tableWidget_vendido.setItem(rowIndex, colIndex, QTableWidgetItem(str(value)))
        self.tableWidget_vendido.resizeColumnsToContents()
    
    def load_data_from_db(self):
        
        if self.ed_pesquisa.text():
            rows = self.listaProduto(produto=self.ed_pesquisa.text())
            
        else:
            rows = self.listaProduto()

        numRows = len(rows)
        numCols = len(rows[0]) if numRows > 0 else 0

        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setColumnCount(numCols)
        nomeColunas = ["ID","ITEM","VALOR R$","CUSTO R$","LUCRO %","MATERIAL","KG R$","PINTURA","HORA","MINUTOS","FILAMENTO M","PESO G","ALTURA CM","PORCENTAGEM","ALTURA CAMADA","INFILL","SUPORTE","OUTROS","LINK"]
        self.tableWidget.setHorizontalHeaderLabels(nomeColunas)

        for rowIndex, row in enumerate(rows):
            for colIndex, value in enumerate(row):
                self.tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(str(value)))
        self.tableWidget.resizeColumnsToContents()

# listagem
    def listaProduto(self,id=None,produto=None):
        
        if produto:
            cursor.execute(f'select * from PRODUTOS where item like "%{produto}%"')

        elif id:
            cursor.execute(f'select * from PRODUTOS where id ={id}')

        else:
            cursor.execute('select * from PRODUTOS')

        rows = cursor.fetchall()
        # conn.close()
        retorno = []
        for row in rows:
            retorno.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18]])
        return retorno
        

    def listaVendido(self,id=None):
        if id:
            cursor.execute(f'select * from VENDA where id_ ={id}')

        else:
            cursor.execute('select * from VENDA order by id_ desc')

        rows = cursor.fetchall()
        # conn.close()
        retorno = []
        for row in rows:
            retorno.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]])
        return retorno

# clique duplo
    def printDoubleClickedItem(self, row, column):
        first_item = self.tableWidget.item(row, 0)
        if first_item:
            self.frmCad.show()
            self.frmLista.hide()
            self.limpacadastro()

            retorno = self.listaProduto(first_item.text())
            retorno = retorno[0]
            # print(retorno[0],type(retorno))
            self.label_19.setText("Atualizar Produto")
            self.btGrava.setText("Atualizar")
            self.id.setText(str(retorno[0]))
            self.edItem.setText(retorno[1])
            self.lbvenda.setText(retorno[2])
            self.lbproducao.setText(retorno[3])
            self.idlucro.setText(retorno[4])
            self.idMaterial.setText(retorno[5])
            self.idValorKg.setText(retorno[6])
            self.idCustoPintura.setText(retorno[7])
            self.idTempo.setText(retorno[8])
            self.idFilamentom.setText(retorno[10])
            self.lbpeso.setText(retorno[11])
            self.idAltura.setText(retorno[12])
            self.idTamanhopct.setText(retorno[13])
            self.idAlturaCamada.setText(retorno[14])
            self.idInfill.setText(retorno[15])
            self.idSuporte.setText(retorno[16])
            self.idOutros.setText(retorno[17])
            self.idLink.setText(retorno[18])

            # print(f'Double Click - First cell in row {row}: {first_item.text()}')

    def printDoubleClickedItem_venda(self, row):
        first_item = self.tableWidget_vendido.item(row, 0)
        # print(f'{first_item.text()=}')
        if first_item:
            self.frmvenda.show()
            self.frm_listavendido.hide()
            # self.limpacadastro()

            retorno = self.listaVendido(first_item.text())
            # print(retorno)
            retorno = retorno[0]
            
            self.label_20.setText("Atualizar Venda")
            self.btgravavenda.setText("Atualizar Venda")
            self.lb_idVenda.setText(f'{retorno[0]}')
            self.ed_codprod.setText(str(retorno[1]))
            self.lb_nome.setText(retorno[2])
            self.edcomprador.setText(retorno[3])#"ID","PRODUTO","COMPRADOR","DATA","VENDIDO","VALOR","CUSTO","LUCRO","MATERIAL","ENERGIA","PAGO","OBS"
            self.lbdata.setText(retorno[4])
            self.edvenda.setText(retorno[5])
            self.lbvalor.setText(retorno[6])
            self.lbcusto.setText(retorno[7])

            self.tb_customaterial.setText(retorno[9])
            self.lbcustoenergia.setText(retorno[10])
            luc = float("%.2f" % round(float(self.edvenda.text())-float(self.lbcusto.text()),2))
            self.lblucro.setText(f'{luc}')
            pago=retorno[11]
            
            if pago=="sim":
                self.checkpago.setCheckState(Qt.CheckState.Checked)
            else:
                self.checkpago.setCheckState(Qt.CheckState.Unchecked)
            
            self.edobs.setText(retorno[12])
            
            retorno = (self.listaProduto(id=int(self.ed_codprod.text())))[0]
            id,ITEM,VALORVENDA,VALORPRODUCAO,LUCROPCT,MATERIAL,VALORFILKG,CUSTOPINTURA,TEMPOPRODUCAO,TEMPOPRODUCAOMINUTOS,FILAMENTOM,PESO,ALTURACM,TAMANHOPCT,ALTURACAMADA,INFILL,SUPORTE,OUTROS,LINK = retorno
            self.lbtempo.setText(TEMPOPRODUCAOMINUTOS)

            # print(f'Double Click - First cell in row {row}: {first_item.text()}')


    def abre_item_selecionado(self,item):
        id = str(item.text()).split('\t')[0]
        print(id)


# pesquisa

    def buscaitemvenda(self):
        try:
            retorno = (self.listaProduto(id=int(self.ed_codprod.text())))[0]
            id,ITEM,VALORVENDA,VALORPRODUCAO,LUCROPCT,MATERIAL,VALORFILKG,CUSTOPINTURA,TEMPOPRODUCAO,TEMPOPRODUCAOMINUTOS,FILAMENTOM,PESO,ALTURACM,TAMANHOPCT,ALTURACAMADA,INFILL,SUPORTE,OUTROS,LINK = retorno
        
            self.lb_nome.setText(ITEM)
            self.lbvalor.setText("%.2f" % round(float(VALORVENDA),2))
            self.lbcusto.setText("%.2f" % round(float(VALORPRODUCAO),2))
            self.edvenda.setText("%.2f" % round(float(VALORVENDA),2))
            custoenergia = self.calculaCustoEnergia(1,float(TEMPOPRODUCAOMINUTOS))
            customaterial = self.calculaCustoMaterial(float(VALORFILKG),float(PESO))
            self.lblucro.setText("%.2f" % round(float(self.edvenda.text())-float(self.lbcusto.text()),2)) 
            self.lbcustoenergia.setText("%.2f" % round(float(custoenergia),2))
            self.tb_customaterial.setText("%.2f" % round(float(customaterial),2))
            self.lbtempo.setText(TEMPOPRODUCAOMINUTOS)
            self.lbdata.setText(self.data())
        except Exception as e:
            self.enviaMensagem(f'Erro: {e}')
            self.lb_nome.setText("")
            self.lbvalor.setText("")
            self.lbcusto.setText("")
            self.edvenda.setText("")
            self.edcomprador.setText("")
            self.checkpago.setChecked(False)
            self.edobs.setText("")
            self.lblucro.setText("")
            self.tb_customaterial.setText("")
            self.lbdata.setText("")
            self.lbtempo.setText("")
            self.lbcustoenergia.setText("")
        
# deleta
    def deletaProduto(self):
        id=self.id.text()
        retorno=self.listaProduto(id=id)
        self.confirmadelete("PRODUTO",retorno[0][0],retorno[0][1])

    def deletaVenda(self):
        id=self.lb_idVenda.text()
        retorno=self.listaVendido(id=id)
        self.confirmadeletevenda("VENDA",retorno[0][0],retorno[0][2])
    
    def confirmadelete(self,tabela,id,nome):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle('Aviso!!!')
        msgBox.setText(f'Deseja apagar o item {id}:{nome}')
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msgBox.buttonClicked.connect(self.deletaitem)  # Conecta o sinal buttonClicked ao slot
        msgBox.exec()
    
    def confirmadeletevenda(self,tabela,id,nome):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle('Aviso!!!')
        msgBox.setText(f'Deseja apagar a venda {id}:{nome}')
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msgBox.buttonClicked.connect(self.deletavenda)  # Conecta o sinal buttonClicked ao slot
        msgBox.exec()
    
    def deletaitem(self,button):
        if button.text() == "&OK":
            id=self.id.text()
            nome=self.edItem.text()
            try:
                cursor.execute(f"""DELETE from PRODUTOS where id ={id}""")
                conn.commit()
                self.enviaMensagem(f"O item {id} - {nome}, foi excluido com sucesso!")
                self.abreLista()
            except Exception as e:
                self.enviaMensagem(f"Erro ao apagar o registro!\n{e}")

    def deletavenda(self,button):
        if button.text() == "&OK":
            id=self.lb_idVenda.text()
            nome=self.lb_nome.text()
            # print((f"""DELETE from VENDA where id_ ={id}"""))
            try:
                cursor.execute(f"""DELETE from VENDA where id_ ={id}""")
                conn.commit()
                self.enviaMensagem(f"A venda {id} - {nome}, foi excluido com sucesso!")
                self.listavendas()
            except:
                self.enviaMensagem("Erro ao apagar o registro!")

    def insereVenda(self,ID,PRODUTO,COMPRADOR,DATA,VALORVENDA,VALORPRODUTO,CUSTO,LUCRO,MATERIAL,ENERGIA,PAGO,OBS):
        # print(ID,PRODUTO,COMPRADOR,DATA,VALORVENDA,VALORPRODUTO,CUSTO,LUCRO,MATERIAL,ENERGIA,PAGO,OBS)
        # "ID","PRODUTO","COMPRADOR","DATA","VALORVENDA","VALORPRODUTO","CUSTO","LUCRO","MATERIAL","ENERGIA","PAGO","OBS"
        try:
            VALORVENDA=f'{float(VALORVENDA):.2f}'
            cursor.execute(f"""INSERT INTO VENDA 
                        (ID,PRODUTO,COMPRADOR,DATA,VALORVENDA,VALORPRODUTO,CUSTO,LUCRO,MATERIAL,ENERGIA,PAGO,OBS)
                        VALUES (
                        '{ID}','{PRODUTO}','{COMPRADOR}','{DATA}','{VALORVENDA}','{VALORPRODUTO}','{CUSTO}','{LUCRO}','{MATERIAL}','{ENERGIA}','{PAGO}','{OBS}')""")
            conn.commit()
        except Exception as e:
            self.enviaMensagem(f'{e}')


# atualiza
    def atualizarProduto(self,id,item,lucro,valorkg,custopintura,tempoproducao,material,filamentom,alturacm,tamanhopct,alturacamada,infill,suporte,outros,link):
        
        produtos = self.listaProduto(id=id)
        
        if produtos:
            if id:
                if custopintura =="":
                    custopintura=0
                pesog = self.calculaPeso(float(filamentom))
                tempomin = self.converteHoraEmMinutos(tempoproducao)
                custoMaterial = self.calculaCustoMaterial(float(valorkg),pesog)
                custoEnergia = self.calculaCustoEnergia(1,tempomin)
                custoManutencao = self.calculaCustoManutencao(custoMaterial)
                custoFalhas = self.calculaCustoFalhas(custoMaterial)
                custoAcabamento = self.calculaCustoAcabamento(custoMaterial)
                valorProducao = self.calculaValorProducao(custoMaterial,custoEnergia,custoFalhas,custoManutencao,custoAcabamento)
                valorVenda = self.calculaValorVenda(valorProducao,lucro,custopintura)
                
                cursor.execute(f'''update PRODUTOS set item="{item}", valorvenda="{valorVenda}",valorproducao="{valorProducao}",
                            custopintura="{custopintura}",tempoproducao="{tempoproducao}",material="{material}",
                            filamentom="{filamentom}",alturacm="{alturacm}",tamanhopct="{tamanhopct}",alturacamada="{alturacamada}",
                            infill="{infill}",suporte="{suporte}",outros="{outros}",link="{link}",VALORFILKG="{valorkg}",lucropct="{lucro}",tempoproducaominutos="{tempomin}"
                            where id ={id}''')
                conn.commit()
        else:
            self.enviaMensagem("Erro ao atualizar")

    def atualizaProduto(self):
        id = self.id.text()
        item = self.edItem.text()
        lucro=self.idlucro.text()
        valorkg = self.idValorKg.text().replace(',','.')
        custopintura = self.idCustoPintura.text().replace(',','.')
        tempoproducao = self.idTempo.text().replace(',',':').replace('.',':')
        material = self.idMaterial.text()
        filamentom = self.idFilamentom.text().replace(',','.')
        alturacm = self.idAltura.text().replace(',','.')
        tamanhopct = self.idTamanhopct.text().replace(',','.')
        alturacamada = self.idAlturaCamada.text().replace(',','.')
        infill = self.idInfill.text()
        suporte = self.idSuporte.text()
        outros = self.idOutros.text()
        link = self.idLink.text()

        
        # produtos = listaProduto(id)
        
        # if produtos:
        #     if id:
        if custopintura =="":
            custopintura=0
        pesog = self.calculaPeso(float(filamentom))
        tempomin = self.converteHoraEmMinutos(tempoproducao)
        custoMaterial = self.calculaCustoMaterial(float(valorkg),pesog)
        custoEnergia = self.calculaCustoEnergia(1,tempomin)
        custoManutencao = self.calculaCustoManutencao(custoMaterial)
        custoFalhas = self.calculaCustoFalhas(custoMaterial)
        custoAcabamento = self.calculaCustoAcabamento(custoMaterial)
        valorProducao = self.calculaValorProducao(custoMaterial,custoEnergia,custoFalhas,custoManutencao,custoAcabamento)
        valorVenda = self.calculaValorVenda(valorProducao,lucro,custopintura)
        self.lbproducao.setText(f'{valorProducao:.2f}')
        self.lbvenda.setText(f'{valorVenda:.2f}')
        self.lbpeso.setText(f'{pesog:.2f}')

        # custopintura=f'{custopintura:.2f}'
        valorVenda=f'{valorVenda:.2f}'
        valorProducao=f'{valorProducao:.2f}'
        # print(custopintura,valorProducao,valorVenda)
        if not self.id.text() == "":    
            cursor.execute(f'''update PRODUTOS set item="{item}", valorvenda="{str(valorVenda)}",valorproducao="{valorProducao}",
                        custopintura="{custopintura}",tempoproducao="{tempoproducao}",material="{material}",
                        filamentom="{filamentom}",alturacm="{alturacm}",tamanhopct="{tamanhopct}",alturacamada="{alturacamada}",
                        infill="{infill}",suporte="{suporte}",outros="{outros}",link="{link}",VALORFILKG="{valorkg}",lucropct="{lucro}",tempoproducaominutos="{tempomin}"
                        where id ={id}''')
            conn.commit()
            self.enviaMensagem("Item Atualizado")
            self.limpacadastro()
            self.frmCad.hide()
            self.frmLista.show()
        else:
            # try:
            contagem = self.listaProduto()
            contagem=int(contagem[-1][0])+1
            cursor.execute(f"""INSERT INTO PRODUTOS 
            (ID,ITEM, VALORVENDA, VALORPRODUCAO, LUCROPCT, MATERIAL, VALORFILKG, CUSTOPINTURA, TEMPOPRODUCAO, TEMPOPRODUCAOMINUTOS, FILAMENTOM, PESO, ALTURACM, TAMANHOPCT, ALTURACAMADA, INFILL, SUPORTE, OUTROS, LINK)
            VALUES ( '{contagem}',
            '{item}','{valorVenda}','{valorProducao}','{lucro}','{material}','{valorkg}','{custopintura}','{tempoproducao}','{tempomin}','{filamentom}','{pesog}','{alturacm}','{tamanhopct}','{alturacamada}','{infill}','{suporte}','{outros}','{link}')""")

            conn.commit()
            self.enviaMensagem("Item Cadastrado")
            self.limpacadastro()
            self.frmCad.hide()
            self.frmLista.show()
            # except Exception as e:
            #     print(e)
            # else:
            #     print("Erro ao atualizar")

    def atualizaVenda(self,id_,ID,PRODUTO,COMPRADOR,DATA,VALORVENDA,VALORPRODUTO,CUSTO,LUCRO,MATERIAL,ENERGIA,PAGO,OBS):
        # print(ID,PRODUTO,COMPRADOR,DATA,VALORVENDA,VALORPRODUTO,CUSTO,LUCRO,MATERIAL,ENERGIA,PAGO,OBS)
        # "ID","PRODUTO","COMPRADOR","DATA","VALORVENDA","VALORPRODUTO","CUSTO","LUCRO","MATERIAL","ENERGIA","PAGO","OBS"
        cursor.execute(f"""update VENDA set ID='{ID}',PRODUTO='{PRODUTO}',COMPRADOR='{COMPRADOR}',DATA='{DATA}',VALORVENDA='{VALORVENDA}',VALORPRODUTO='{VALORPRODUTO}',CUSTO='{CUSTO}',LUCRO='{LUCRO}',MATERIAL='{MATERIAL}',ENERGIA='{ENERGIA}',PAGO='{PAGO}',OBS='{OBS}'
                    where id_=={id_}""")
        conn.commit()


# vende
    def fazVenda(self):
        id,nome,valor,custo,customaterial,lucro,vdata,venda,comprador,obs,pago="","","","","","","","","","",""
        if self.edvenda.text() =="" or self.edcomprador.text() =="" or self.ed_codprod.text()=="":
            ...
        else:
            
            luc = float(self.edvenda.text().replace(',','.'))-float(self.lbcusto.text().replace(',','.'))
            self.lblucro.setText(f'{luc}')
            id = self.ed_codprod.text()
            nome = self.lb_nome.text()
            valor  = self.lbvalor.text().replace(',','.')
            # valor = f'{valor:.2f}'
            custo = self.lbcusto.text().replace(',','.')
            # custo = f'{custo:.2f}'
            customaterial = self.tb_customaterial.text().replace(',','.')
            # customaterial = f'{customaterial:.2f}'
            lucro = self.lblucro.text().replace(',','.')
            vdata = self.lbdata.text()
            venda = self.edvenda.text().replace(',','.')
            venda = f'{float(venda):.2f}'
            comprador = self.edcomprador.text()
            obs = self.edobs.text()
            id_=self.lb_idVenda.text()
            energia = self.calculaCustoEnergia(1,int(self.lbtempo.text()))
            if self.checkpago.isChecked(): 
                pago = "sim"
            else:
                pago="nao"
            # try:
            if self.btgravavenda.text()=="Gravar":    
                self.insereVenda(id,nome,comprador,vdata,venda,valor,custo,lucro,customaterial,energia,pago,obs)
                self.enviaMensagem("Cadastro de venda feito!")
                self.frm_listavendido.show()
                self.frmvenda.hide()
                self.limpacadastro()
                self.load_data_from_db_venda()
            else:
                # print(id_,id,nome,comprador,vdata,venda,valor,custo,lucro,customaterial,energia,pago,obs)
                self.atualizaVenda(id_,id,nome,comprador,vdata,venda,valor,custo,lucro,customaterial,energia,pago,obs)
                self.enviaMensagem("Atualização da venda feito!")
                self.frm_listavendido.show()
                self.frmvenda.hide()
                self.limpacadastro()
                self.load_data_from_db_venda()
            # except Exception as e:
            #     self.enviaMensagem(f'{e}')

# outros
    def calculaProduto(self):
        id = self.id.text()
        item = self.edItem.text()
        lucro=self.idlucro.text()
        valorkg = self.idValorKg.text()
        custopintura = self.idCustoPintura.text()
        tempoproducao = self.idTempo.text()
        material = self.idMaterial.text()
        filamentom = self.idFilamentom.text()
        alturacm = self.idAltura.text()
        tamanhopct = self.idTamanhopct.text()
        alturacamada = self.idAlturaCamada.text()
        infill = self.idInfill.text()
        suporte = self.idSuporte.text()
        outros = self.idOutros.text()
        link = self.idLink.text()

        
        # produtos = listaProduto(id)
        
        # if produtos:
        #     if id:
        if custopintura =="":
            custopintura=0
        pesog = self.calculaPeso(float(filamentom))
        tempomin = self.converteHoraEmMinutos(tempoproducao)
        custoMaterial = self.calculaCustoMaterial(float(valorkg),pesog)
        custoEnergia = self.calculaCustoEnergia(1,tempomin)
        custoManutencao = self.calculaCustoManutencao(custoMaterial)
        custoFalhas = self.calculaCustoFalhas(custoMaterial)
        custoAcabamento = self.calculaCustoAcabamento(custoMaterial)
        valorProducao = self.calculaValorProducao(custoMaterial,custoEnergia,custoFalhas,custoManutencao,custoAcabamento)
        valorVenda = self.calculaValorVenda(valorProducao,lucro,custopintura)
        self.lbproducao.setText(str(valorProducao))
        self.lbvenda.setText(str(valorVenda))
        self.lbpeso.setText(str(pesog))
        self.btgravavenda.clicked.connect(self.fazVenda)
        # print(f'{custoAcabamento=},{custoEnergia=},{custoFalhas=}{custoManutencao=},{custoMaterial=},{custopintura=}')

    def enviaMensagem(self,mensagem):
        QMessageBox.about(self, "Aviso!", mensagem)

    def limpacadastro(self):
        self.id.setText("")
        self.edItem.setText("")
        self.idMaterial.setText("")
        self.idValorKg.setText("")
        self.idCustoPintura.setText("")
        self.idTempo.setText("")
        self.idFilamentom.setText("")
        self.idAltura.setText("")
        self.idTamanhopct.setText("")
        self.idAlturaCamada.setText("")
        self.idInfill.setText("")
        self.idSuporte.setText("")
        self.idOutros.setText("")
        self.idLink.setText("")
        self.idlucro.setText("")
        self.lbproducao.setText("")
        self.lbvenda.setText("")
        self.lbpeso.setText("")
        self.ed_codprod.setText("")
        self.lb_nome.setText("")
        self.lbvalor.setText("")
        self.lbcusto.setText("")
        self.lbcustoenergia.setText("")
        self.tb_customaterial.setText("")
        self.lblucro.setText("")
        self.edvenda.setText("")
        self.edcomprador.setText("")
        self.lbtempo.setText("")
        self.lb_idVenda.setText("")
        self.edobs.setText("")
        self.checkpago.setCheckState(Qt.CheckState.Unchecked)

#calculos para a impressao
    def calculaValorVenda(self,valorProducao,lucro,custoPintura):
        resultado = valorProducao+(valorProducao*(int(lucro)/100))+float(custoPintura)
        
        return float(f"{resultado:.2f}")

    def calculaPeso(self,metros,diametro=1.75):
        resultado = metros * 1.24 * (math.pi * ((diametro / 2) ** 2))

        return float("%.2f" % round(resultado,2))

    def calculaCustoMaterial(self,valorkg,pesog):
        return float("%.2f" % round((float(valorkg)/1000)*float(pesog),2))

    def calculaCustoEnergia(self,kwh,tempomin):
        return float("%.2f" % round(((float(kwh)/1000)*350)*tempomin/60,2))

    def calculaCustoManutencao(self,customaterial):
        return float("%.2f" % round(float(customaterial)*0.15,2))

    def calculaCustoFalhas(self,customaterial):
        return float("%.2f" % round(float(customaterial)*0.10,2))

    def calculaCustoAcabamento(self,customaterial):
        return float("%.2f" % round(float(customaterial)*0.10,2))

    def converteHoraEmMinutos(self,tempo):
        # Divide o horário na parte de horas e minutos
        partes = tempo.split(':')
        horas = int(partes[0])
        minutos = int(partes[1])
        
        # Converte horas para minutos e soma com os minutos
        total_minutos = horas * 60 + minutos
        return int(total_minutos)

    def calculaValorProducao(self,custoMaterial,custoEnergia,custoFalhas,custoManutencao,custoAcabamento):
        valorProducao=(float(custoMaterial)+float(custoEnergia)+float(custoFalhas)+float(custoManutencao)+float(custoAcabamento)+retornoInvestimento)
        valorProducao=float("%.2f" % round(valorProducao,2))
        return valorProducao

    # def calculaValorVenda(self,valorProducao,lucro,custopintura):
    #     valorVenda = valorProducao+(valorProducao*(int(lucro)/100))+float(custopintura)
    #     valorVenda = float("%.2f" % round(valorVenda,2))
    #     return valorVenda

# home
    def exibeResumo(self):
        data_ = self.data(separado=True)
        data_inicio = f'{data_[2]}-{data_[1]}-01'
        ultimodia = calendar.monthrange(data_[0],data_[1])
        data_fim = f'{data_[2]}-{data_[1]}-{ultimodia[1]}'
        
        # totalvenda mes
        df = pd.read_sql_query("SELECT * from venda", conn)
        df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')
        df['VALORVENDA'] = pd.to_numeric(df['VALORVENDA'])
        df['CUSTO'] = pd.to_numeric(df['CUSTO'])
        df['ENERGIA'] = pd.to_numeric(df['ENERGIA'])
        df['MATERIAL'] = pd.to_numeric(df['MATERIAL'])
        
        

        mask = (df['DATA'] >= data_inicio) & (df['DATA'] <= data_fim)
        df_filtrado = df.loc[mask]
        vendames=df_filtrado['VALORVENDA'].sum()
        energiames=df_filtrado["ENERGIA"].sum()
        customes=df_filtrado["CUSTO"].sum()

        # total pago
        mask1 = df['PAGO']=="sim"
        df_filtrado1 = df.loc[mask1]
        pagomes=df_filtrado1['VALORVENDA'].sum()
        
        # total nao pago
        mask2 = df['PAGO']!="sim"
        df_filtrado2 = df.loc[mask2]
        naopagomes=df_filtrado2['VALORVENDA'].sum()
        
        # total vendido
        vendido = df["VALORVENDA"].sum()
        totalgasto = df["CUSTO"].sum()
        totalmaterial = df["MATERIAL"].sum()
        totalenergia = df["ENERGIA"].sum()
        lucrototal=float(vendido)-float(totalgasto)
        # lucrototal="0"

        self.lb_resumo.setText(f"""Total
Venda R${vendido:.2f}
Custo de produção R${totalgasto:.2f}
Energia gasta R${totalenergia:.2f}
Filamento gasto R${totalmaterial:.2f}
Lucro R${lucrototal:.2f}

Dentro do mes
Venda mes '{data_[1]}' : R${vendames:.2f}
Total pago: R${pagomes:.2f}
Total não pago: R${naopagomes:.2f}
Custo produção R$ {customes:.2f}
Energia gasta R${energiames:.2f}""")


        titulo = ['Pago','Não Pago']
        valores = [pagomes,naopagomes]
        colors = ['green', 'red', 'lightcoral', 'lightskyblue']       
        def func(pct, allvalues):
            absolute = round(pct/100.*sum(allvalues), 1)
            return f'{absolute}'
        explode = (0.1, 0, 0, 0)
        plt.pie(valores,  colors=colors, autopct=lambda pct: func(pct, valores), startangle=140, textprops={'color': 'black'})#, 'fontsize': 12})
        plt.legend(titulo,loc="upper right")
        plt.plot(250,250)
        plt.savefig('grafico_de_pizza.png', dpi=100, format='png', bbox_inches='tight', pad_inches=0.2, )
        # plt.show()
        pixmap = QPixmap('grafico_de_pizza.png')

        # pixmap = pixmap.scaled(300, 300)
        self.lb_grafico.setPixmap(pixmap)

    def exportPDF(self):
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
        from reportlab.lib import colors
        pdf = SimpleDocTemplate("dataframe.pdf", pagesize=letter)

        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ])

        df = pd.read_sql_query("SELECT * from PRODUTOS", conn)
        # df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')
        df['VALORVENDA'] = pd.to_numeric(df['VALORVENDA'])
        df['VALORPRODUCAO'] = pd.to_numeric(df['VALORPRODUCAO'])
        df['CUSTOPINTURA'] = pd.to_numeric(df['CUSTOPINTURA'])
        df['VALORFILKG'] = pd.to_numeric(df['VALORFILKG'])
        # df['MATERIAL'] = pd.to_numeric(df['MATERIAL'])
        df.head()

        # df.setStyle(table_style)

        pdf_table = []
        pdf_table.append(df)

        # pdf.build(pdf_table)

    
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
