# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(3000, 602)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(3000, 624))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setMinimumSize(QtCore.QSize(0, 40))
        self.label_14.setMaximumSize(QtCore.QSize(2000, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(620, 55))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_home = QtWidgets.QPushButton(parent=self.frame)
        self.bt_home.setMinimumSize(QtCore.QSize(120, 40))
        self.bt_home.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.bt_home.setFont(font)
        self.bt_home.setObjectName("bt_home")
        self.horizontalLayout_3.addWidget(self.bt_home)
        self.btCalculadora = QtWidgets.QPushButton(parent=self.frame)
        self.btCalculadora.setMinimumSize(QtCore.QSize(120, 40))
        self.btCalculadora.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.btCalculadora.setFont(font)
        self.btCalculadora.setObjectName("btCalculadora")
        self.horizontalLayout_3.addWidget(self.btCalculadora)
        self.btLista = QtWidgets.QPushButton(parent=self.frame)
        self.btLista.setMinimumSize(QtCore.QSize(120, 40))
        self.btLista.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.btLista.setFont(font)
        self.btLista.setObjectName("btLista")
        self.horizontalLayout_3.addWidget(self.btLista)
        self.btVendas = QtWidgets.QPushButton(parent=self.frame)
        self.btVendas.setMinimumSize(QtCore.QSize(120, 40))
        self.btVendas.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.btVendas.setFont(font)
        self.btVendas.setObjectName("btVendas")
        self.horizontalLayout_3.addWidget(self.btVendas)
        self.bt_listarvendas = QtWidgets.QPushButton(parent=self.frame)
        self.bt_listarvendas.setMinimumSize(QtCore.QSize(120, 40))
        self.bt_listarvendas.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.bt_listarvendas.setFont(font)
        self.bt_listarvendas.setObjectName("bt_listarvendas")
        self.horizontalLayout_3.addWidget(self.bt_listarvendas)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_10.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frmCad = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmCad.sizePolicy().hasHeightForWidth())
        self.frmCad.setSizePolicy(sizePolicy)
        self.frmCad.setMinimumSize(QtCore.QSize(600, 400))
        self.frmCad.setMaximumSize(QtCore.QSize(600, 400))
        self.frmCad.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frmCad.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frmCad.setObjectName("frmCad")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frmCad)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_19 = QtWidgets.QLabel(parent=self.frmCad)
        self.label_19.setMinimumSize(QtCore.QSize(450, 0))
        self.label_19.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.frmCad)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(parent=self.frmCad)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 2, 1, 1)
        self.idlucro = QtWidgets.QLineEdit(parent=self.frmCad)
        self.idlucro.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idlucro.setObjectName("idlucro")
        self.gridLayout.addWidget(self.idlucro, 2, 1, 1, 1)
        self.btGrava = QtWidgets.QPushButton(parent=self.frmCad)
        self.btGrava.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.btGrava.setFont(font)
        self.btGrava.setObjectName("btGrava")
        self.gridLayout.addWidget(self.btGrava, 10, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.frmCad)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.frmCad)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 2, 1, 1)
        self.idLink = QtWidgets.QLineEdit(parent=self.frmCad)
        self.idLink.setMaximumSize(QtCore.QSize(400, 16777215))
        self.idLink.setObjectName("idLink")
        self.gridLayout.addWidget(self.idLink, 9, 3, 1, 1)
        self.label_32 = QtWidgets.QLabel(parent=self.frmCad)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 9, 2, 1, 1)
        self.idSuporte = QtWidgets.QLineEdit(parent=self.frmCad)
        self.idSuporte.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idSuporte.setObjectName("idSuporte")
        self.gridLayout.addWidget(self.idSuporte, 9, 1, 1, 1)
        self.edItem = QtWidgets.QLineEdit(parent=self.frmCad)
        self.edItem.setMaximumSize(QtCore.QSize(300, 16777215))
        self.edItem.setObjectName("edItem")
        self.gridLayout.addWidget(self.edItem, 1, 1, 1, 1)
        self.id = QtWidgets.QLabel(parent=self.frmCad)
        self.id.setMinimumSize(QtCore.QSize(10, 0))
        self.id.setText("")
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 12, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.frmCad)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)
        self.idFilamentom = QtWidgets.QLineEdit(parent=self.frmCad)
        self.idFilamentom.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idFilamentom.setObjectName("idFilamentom")
        self.gridLayout.addWidget(self.idFilamentom, 4, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(parent=self.frmCad)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.frmCad)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 2, 1, 1)
        self.btCalcula = QtWidgets.QPushButton(parent=self.frmCad)
        self.btCalcula.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.btCalcula.setFont(font)
        self.btCalcula.setObjectName("btCalcula")
        self.gridLayout.addWidget(self.btCalcula, 10, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.frmCad)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.idValorKg = QtWidgets.QLineEdit(parent=self.frmCad)
        self.idValorKg.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idValorKg.setObjectName("idValorKg")
        self.gridLayout.addWidget(self.idValorKg, 3, 3, 1, 1)
        self.lbproducao = QtWidgets.QLabel(parent=self.frmCad)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbproducao.setFont(font)
        self.lbproducao.setObjectName("lbproducao")
        self.gridLayout.addWidget(self.lbproducao, 2, 3, 1, 1)
        self.idTamanhopct = QtWidgets.QLineEdit(parent=self.frmCad)
        self.idTamanhopct.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idTamanhopct.setObjectName("idTamanhopct")
        self.gridLayout.addWidget(self.idTamanhopct, 6, 3, 1, 1)
        self.idTempo = QtWidgets.QLineEdit(parent=self.frmCad)
        self.idTempo.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idTempo.setObjectName("idTempo")
        self.gridLayout.addWidget(self.idTempo, 5, 3, 1, 1)
        self.idAlturaCamada = QtWidgets.QLineEdit(parent=self.frmCad)
        self.idAlturaCamada.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idAlturaCamada.setObjectName("idAlturaCamada")
        self.gridLayout.addWidget(self.idAlturaCamada, 8, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.frmCad)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.br_deletar = QtWidgets.QPushButton(parent=self.frmCad)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.br_deletar.setFont(font)
        self.br_deletar.setObjectName("br_deletar")
        self.gridLayout.addWidget(self.br_deletar, 10, 3, 1, 1)
        self.lbpeso = QtWidgets.QLabel(parent=self.frmCad)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbpeso.setFont(font)
        self.lbpeso.setObjectName("lbpeso")
        self.gridLayout.addWidget(self.lbpeso, 4, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frmCad)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.idInfill = QtWidgets.QLineEdit(parent=self.frmCad)
        self.idInfill.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idInfill.setObjectName("idInfill")
        self.gridLayout.addWidget(self.idInfill, 7, 3, 1, 1)
        self.idOutros = QtWidgets.QLineEdit(parent=self.frmCad)
        self.idOutros.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idOutros.setObjectName("idOutros")
        self.gridLayout.addWidget(self.idOutros, 8, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.frmCad)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.frmCad)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(parent=self.frmCad)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 2, 1, 1)
        self.idCustoPintura = QtWidgets.QLineEdit(parent=self.frmCad)
        self.idCustoPintura.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idCustoPintura.setObjectName("idCustoPintura")
        self.gridLayout.addWidget(self.idCustoPintura, 5, 1, 1, 1)
        self.btLimpa = QtWidgets.QPushButton(parent=self.frmCad)
        self.btLimpa.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.btLimpa.setFont(font)
        self.btLimpa.setObjectName("btLimpa")
        self.gridLayout.addWidget(self.btLimpa, 10, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.frmCad)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.frmCad)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.idAltura = QtWidgets.QLineEdit(parent=self.frmCad)
        self.idAltura.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idAltura.setObjectName("idAltura")
        self.gridLayout.addWidget(self.idAltura, 7, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.frmCad)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 2, 1, 1)
        self.idMaterial = QtWidgets.QLineEdit(parent=self.frmCad)
        self.idMaterial.setMaximumSize(QtCore.QSize(300, 16777215))
        self.idMaterial.setObjectName("idMaterial")
        self.gridLayout.addWidget(self.idMaterial, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.frmCad)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)
        self.edoutrosvalores = QtWidgets.QLineEdit(parent=self.frmCad)
        self.edoutrosvalores.setObjectName("edoutrosvalores")
        self.gridLayout.addWidget(self.edoutrosvalores, 6, 1, 1, 1)
        self.lbvenda = QtWidgets.QLabel(parent=self.frmCad)
        self.lbvenda.setObjectName("lbvenda")
        self.gridLayout.addWidget(self.lbvenda, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frmCad, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.frmvenda = QtWidgets.QFrame(parent=self.centralwidget)
        self.frmvenda.setMaximumSize(QtCore.QSize(450, 400))
        self.frmvenda.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frmvenda.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frmvenda.setObjectName("frmvenda")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frmvenda)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_27 = QtWidgets.QLabel(parent=self.frmvenda)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 10, 1, 1, 1)
        self.edvenda = QtWidgets.QLineEdit(parent=self.frmvenda)
        self.edvenda.setObjectName("edvenda")
        self.gridLayout_5.addWidget(self.edvenda, 9, 2, 1, 2)
        self.edcomprador = QtWidgets.QLineEdit(parent=self.frmvenda)
        self.edcomprador.setObjectName("edcomprador")
        self.gridLayout_5.addWidget(self.edcomprador, 10, 2, 1, 4)
        self.edobs = QtWidgets.QLineEdit(parent=self.frmvenda)
        self.edobs.setObjectName("edobs")
        self.gridLayout_5.addWidget(self.edobs, 11, 2, 1, 4)
        self.lbcustoenergia = QtWidgets.QLabel(parent=self.frmvenda)
        self.lbcustoenergia.setText("")
        self.lbcustoenergia.setObjectName("lbcustoenergia")
        self.gridLayout_5.addWidget(self.lbcustoenergia, 6, 2, 1, 3)
        self.label_25 = QtWidgets.QLabel(parent=self.frmvenda)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 7, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(parent=self.frmvenda)
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 5, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(parent=self.frmvenda)
        self.label_20.setMinimumSize(QtCore.QSize(430, 0))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 0, 1, 1, 4)
        self.tb_customaterial = QtWidgets.QLabel(parent=self.frmvenda)
        self.tb_customaterial.setText("")
        self.tb_customaterial.setObjectName("tb_customaterial")
        self.gridLayout_5.addWidget(self.tb_customaterial, 5, 2, 1, 3)
        self.label_21 = QtWidgets.QLabel(parent=self.frmvenda)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(parent=self.frmvenda)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 2, 1, 1, 1)
        self.lbvalor = QtWidgets.QLabel(parent=self.frmvenda)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbvalor.setFont(font)
        self.lbvalor.setText("")
        self.lbvalor.setObjectName("lbvalor")
        self.gridLayout_5.addWidget(self.lbvalor, 3, 2, 1, 3)
        self.label_23 = QtWidgets.QLabel(parent=self.frmvenda)
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 4, 1, 1, 1)
        self.checkpago = QtWidgets.QCheckBox(parent=self.frmvenda)
        self.checkpago.setObjectName("checkpago")
        self.gridLayout_5.addWidget(self.checkpago, 9, 4, 1, 1)
        self.ed_codprod = QtWidgets.QLineEdit(parent=self.frmvenda)
        self.ed_codprod.setObjectName("ed_codprod")
        self.gridLayout_5.addWidget(self.ed_codprod, 1, 2, 1, 1)
        self.lbcusto = QtWidgets.QLabel(parent=self.frmvenda)
        font = QtGui.QFont()
        font.setBold(True)
        self.lbcusto.setFont(font)
        self.lbcusto.setText("")
        self.lbcusto.setObjectName("lbcusto")
        self.gridLayout_5.addWidget(self.lbcusto, 4, 2, 1, 3)
        self.lbdata = QtWidgets.QLabel(parent=self.frmvenda)
        self.lbdata.setText("")
        self.lbdata.setObjectName("lbdata")
        self.gridLayout_5.addWidget(self.lbdata, 1, 4, 1, 1)
        self.lblucro = QtWidgets.QLabel(parent=self.frmvenda)
        font = QtGui.QFont()
        font.setBold(True)
        self.lblucro.setFont(font)
        self.lblucro.setText("")
        self.lblucro.setObjectName("lblucro")
        self.gridLayout_5.addWidget(self.lblucro, 7, 2, 1, 3)
        self.label_29 = QtWidgets.QLabel(parent=self.frmvenda)
        self.label_29.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 11, 1, 1, 1)
        self.lb_nome = QtWidgets.QLabel(parent=self.frmvenda)
        self.lb_nome.setText("")
        self.lb_nome.setObjectName("lb_nome")
        self.gridLayout_5.addWidget(self.lb_nome, 2, 2, 1, 3)
        self.label_26 = QtWidgets.QLabel(parent=self.frmvenda)
        self.label_26.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 9, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(parent=self.frmvenda)
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 3, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(parent=self.frmvenda)
        self.label_31.setObjectName("label_31")
        self.gridLayout_5.addWidget(self.label_31, 6, 1, 1, 1)
        self.bt_buscaprod = QtWidgets.QPushButton(parent=self.frmvenda)
        font = QtGui.QFont()
        font.setBold(True)
        self.bt_buscaprod.setFont(font)
        self.bt_buscaprod.setObjectName("bt_buscaprod")
        self.gridLayout_5.addWidget(self.bt_buscaprod, 1, 3, 1, 1)
        self.lbtempo = QtWidgets.QLabel(parent=self.frmvenda)
        self.lbtempo.setText("")
        self.lbtempo.setObjectName("lbtempo")
        self.gridLayout_5.addWidget(self.lbtempo, 13, 1, 1, 1)
        self.lb_idVenda = QtWidgets.QLabel(parent=self.frmvenda)
        self.lb_idVenda.setText("")
        self.lb_idVenda.setObjectName("lb_idVenda")
        self.gridLayout_5.addWidget(self.lb_idVenda, 13, 2, 1, 1)
        self.btgravavenda = QtWidgets.QPushButton(parent=self.frmvenda)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.btgravavenda.setFont(font)
        self.btgravavenda.setObjectName("btgravavenda")
        self.gridLayout_5.addWidget(self.btgravavenda, 12, 1, 1, 3)
        self.br_deletar2 = QtWidgets.QPushButton(parent=self.frmvenda)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.br_deletar2.setFont(font)
        self.br_deletar2.setObjectName("br_deletar2")
        self.gridLayout_5.addWidget(self.br_deletar2, 12, 4, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.frmvenda, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frm_listavendido = QtWidgets.QFrame(parent=self.centralwidget)
        self.frm_listavendido.setMaximumSize(QtCore.QSize(1000, 620))
        self.frm_listavendido.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frm_listavendido.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frm_listavendido.setObjectName("frm_listavendido")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frm_listavendido)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tableWidget_vendido = QtWidgets.QTableWidget(parent=self.frm_listavendido)
        self.tableWidget_vendido.setMinimumSize(QtCore.QSize(960, 400))
        self.tableWidget_vendido.setMaximumSize(QtCore.QSize(960, 400))
        self.tableWidget_vendido.setObjectName("tableWidget_vendido")
        self.tableWidget_vendido.setColumnCount(0)
        self.tableWidget_vendido.setRowCount(0)
        self.tableWidget_vendido.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.tableWidget_vendido, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_2 = QtWidgets.QFrame(parent=self.frm_listavendido)
        self.frame_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.rbtodos = QtWidgets.QRadioButton(parent=self.frame_2)
        self.rbtodos.setChecked(True)
        self.rbtodos.setObjectName("rbtodos")
        self.gridLayout_8.addWidget(self.rbtodos, 0, 0, 1, 1)
        self.rbpago = QtWidgets.QRadioButton(parent=self.frame_2)
        self.rbpago.setObjectName("rbpago")
        self.gridLayout_8.addWidget(self.rbpago, 0, 1, 1, 1)
        self.rbnaopago = QtWidgets.QRadioButton(parent=self.frame_2)
        self.rbnaopago.setObjectName("rbnaopago")
        self.gridLayout_8.addWidget(self.rbnaopago, 0, 2, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.gridLayout_6.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.lbTitulo_2 = QtWidgets.QLabel(parent=self.frm_listavendido)
        self.lbTitulo_2.setMinimumSize(QtCore.QSize(900, 0))
        self.lbTitulo_2.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        self.lbTitulo_2.setFont(font)
        self.lbTitulo_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbTitulo_2.setObjectName("lbTitulo_2")
        self.gridLayout_6.addWidget(self.lbTitulo_2, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frm_listavendido)
        self.frm_home = QtWidgets.QFrame(parent=self.centralwidget)
        self.frm_home.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frm_home.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frm_home.setObjectName("frm_home")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frm_home)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_28 = QtWidgets.QLabel(parent=self.frm_home)
        self.label_28.setMinimumSize(QtCore.QSize(0, 20))
        self.label_28.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_7.addWidget(self.label_28, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lb_grafico = QtWidgets.QLabel(parent=self.frm_home)
        self.lb_grafico.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_grafico.setObjectName("lb_grafico")
        self.horizontalLayout_6.addWidget(self.lb_grafico)
        self.lb_resumo = QtWidgets.QLabel(parent=self.frm_home)
        self.lb_resumo.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lb_resumo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_resumo.setObjectName("lb_resumo")
        self.horizontalLayout_6.addWidget(self.lb_resumo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frm_home)
        self.frmLista = QtWidgets.QFrame(parent=self.centralwidget)
        self.frmLista.setMaximumSize(QtCore.QSize(1000, 620))
        self.frmLista.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frmLista.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frmLista.setObjectName("frmLista")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frmLista)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbTitulo = QtWidgets.QLabel(parent=self.frmLista)
        self.lbTitulo.setMinimumSize(QtCore.QSize(900, 0))
        self.lbTitulo.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        self.lbTitulo.setFont(font)
        self.lbTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbTitulo.setObjectName("lbTitulo")
        self.gridLayout_3.addWidget(self.lbTitulo, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frmLista)
        self.tableWidget.setMinimumSize(QtCore.QSize(960, 400))
        self.tableWidget.setMaximumSize(QtCore.QSize(960, 1400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tableWidget, 2, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(parent=self.frmLista)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ed_pesquisa = QtWidgets.QLineEdit(parent=self.frame_3)
        self.ed_pesquisa.setObjectName("ed_pesquisa")
        self.horizontalLayout_5.addWidget(self.ed_pesquisa)
        self.bt_pesquisa = QtWidgets.QPushButton(parent=self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        self.bt_pesquisa.setFont(font)
        self.bt_pesquisa.setObjectName("bt_pesquisa")
        self.horizontalLayout_5.addWidget(self.bt_pesquisa)
        self.gridLayout_9.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 1, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.frmLista)
        self.gridLayout_10.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 3000, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.edItem, self.idlucro)
        MainWindow.setTabOrder(self.idlucro, self.idMaterial)
        MainWindow.setTabOrder(self.idMaterial, self.idValorKg)
        MainWindow.setTabOrder(self.idValorKg, self.idFilamentom)
        MainWindow.setTabOrder(self.idFilamentom, self.idCustoPintura)
        MainWindow.setTabOrder(self.idCustoPintura, self.idTempo)
        MainWindow.setTabOrder(self.idTempo, self.edoutrosvalores)
        MainWindow.setTabOrder(self.edoutrosvalores, self.idTamanhopct)
        MainWindow.setTabOrder(self.idTamanhopct, self.idAltura)
        MainWindow.setTabOrder(self.idAltura, self.idInfill)
        MainWindow.setTabOrder(self.idInfill, self.idAlturaCamada)
        MainWindow.setTabOrder(self.idAlturaCamada, self.idOutros)
        MainWindow.setTabOrder(self.idOutros, self.idSuporte)
        MainWindow.setTabOrder(self.idSuporte, self.idLink)
        MainWindow.setTabOrder(self.idLink, self.btGrava)
        MainWindow.setTabOrder(self.btGrava, self.btCalcula)
        MainWindow.setTabOrder(self.btCalcula, self.btLimpa)
        MainWindow.setTabOrder(self.btLimpa, self.br_deletar)
        MainWindow.setTabOrder(self.br_deletar, self.ed_codprod)
        MainWindow.setTabOrder(self.ed_codprod, self.bt_buscaprod)
        MainWindow.setTabOrder(self.bt_buscaprod, self.edvenda)
        MainWindow.setTabOrder(self.edvenda, self.checkpago)
        MainWindow.setTabOrder(self.checkpago, self.edcomprador)
        MainWindow.setTabOrder(self.edcomprador, self.edobs)
        MainWindow.setTabOrder(self.edobs, self.btgravavenda)
        MainWindow.setTabOrder(self.btgravavenda, self.br_deletar2)
        MainWindow.setTabOrder(self.br_deletar2, self.rbtodos)
        MainWindow.setTabOrder(self.rbtodos, self.rbpago)
        MainWindow.setTabOrder(self.rbpago, self.rbnaopago)
        MainWindow.setTabOrder(self.rbnaopago, self.tableWidget_vendido)
        MainWindow.setTabOrder(self.tableWidget_vendido, self.ed_pesquisa)
        MainWindow.setTabOrder(self.ed_pesquisa, self.bt_pesquisa)
        MainWindow.setTabOrder(self.bt_pesquisa, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.bt_home)
        MainWindow.setTabOrder(self.bt_home, self.btCalculadora)
        MainWindow.setTabOrder(self.btCalculadora, self.btLista)
        MainWindow.setTabOrder(self.btLista, self.btVendas)
        MainWindow.setTabOrder(self.btVendas, self.bt_listarvendas)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_14.setText(_translate("MainWindow", "Calculadora 3D"))
        self.bt_home.setText(_translate("MainWindow", "Home"))
        self.btCalculadora.setText(_translate("MainWindow", "Caluladora"))
        self.btLista.setText(_translate("MainWindow", "Lista de Produtos"))
        self.btVendas.setText(_translate("MainWindow", "Nova Venda"))
        self.bt_listarvendas.setText(_translate("MainWindow", "Listar Vendas"))
        self.label_19.setText(_translate("MainWindow", "Cadastrar Produto"))
        self.label.setText(_translate("MainWindow", "Peça"))
        self.label_18.setText(_translate("MainWindow", "Valor Produção"))
        self.btGrava.setText(_translate("MainWindow", "Gravar"))
        self.label_8.setText(_translate("MainWindow", "Tamanho %"))
        self.label_10.setText(_translate("MainWindow", "Infill %"))
        self.label_32.setText(_translate("MainWindow", "Link"))
        self.label_13.setText(_translate("MainWindow", "Outros Valores"))
        self.label_17.setText(_translate("MainWindow", "Peso g"))
        self.label_5.setText(_translate("MainWindow", "Tempo Produção"))
        self.btCalcula.setText(_translate("MainWindow", "Calcular"))
        self.label_6.setText(_translate("MainWindow", "Filamento usado"))
        self.lbproducao.setText(_translate("MainWindow", "R$0.00"))
        self.label_7.setText(_translate("MainWindow", "Altura cm"))
        self.br_deletar.setText(_translate("MainWindow", "Deletar"))
        self.lbpeso.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Material"))
        self.label_4.setText(_translate("MainWindow", "Custo Pintura"))
        self.label_3.setText(_translate("MainWindow", "Filamento Kg"))
        self.label_16.setText(_translate("MainWindow", "Valor Venda"))
        self.btLimpa.setText(_translate("MainWindow", "Limpar"))
        self.label_9.setText(_translate("MainWindow", "Altura camada"))
        self.label_15.setText(_translate("MainWindow", "Lucro"))
        self.label_12.setText(_translate("MainWindow", "Outras infos"))
        self.label_11.setText(_translate("MainWindow", "Suporte"))
        self.lbvenda.setText(_translate("MainWindow", "TextLabel"))
        self.label_27.setText(_translate("MainWindow", "Comprador"))
        self.label_25.setText(_translate("MainWindow", "Lucro"))
        self.label_30.setText(_translate("MainWindow", "Custo Material"))
        self.label_20.setText(_translate("MainWindow", "Vender"))
        self.label_21.setText(_translate("MainWindow", "Codigo do Produto"))
        self.label_24.setText(_translate("MainWindow", "Nome"))
        self.label_23.setText(_translate("MainWindow", "Custo Total"))
        self.checkpago.setText(_translate("MainWindow", "Pago"))
        self.label_29.setText(_translate("MainWindow", "Obs"))
        self.label_26.setText(_translate("MainWindow", "Valor Venda"))
        self.label_22.setText(_translate("MainWindow", "Valor Sugerido"))
        self.label_31.setText(_translate("MainWindow", "Gasto Energia"))
        self.bt_buscaprod.setText(_translate("MainWindow", "Buscar"))
        self.btgravavenda.setText(_translate("MainWindow", "Gravar"))
        self.br_deletar2.setText(_translate("MainWindow", "Apagar"))
        self.rbtodos.setText(_translate("MainWindow", "Todos"))
        self.rbpago.setText(_translate("MainWindow", "Pagos"))
        self.rbnaopago.setText(_translate("MainWindow", "Não Pago"))
        self.lbTitulo_2.setText(_translate("MainWindow", "Produtos Vendidos"))
        self.label_28.setText(_translate("MainWindow", "Controle Gastos/Vendas 3D"))
        self.lb_grafico.setText(_translate("MainWindow", "grafico"))
        self.lb_resumo.setText(_translate("MainWindow", "Total vendido"))
        self.lbTitulo.setText(_translate("MainWindow", "Lista de Produto"))
        self.bt_pesquisa.setText(_translate("MainWindow", "Pesquisa"))
