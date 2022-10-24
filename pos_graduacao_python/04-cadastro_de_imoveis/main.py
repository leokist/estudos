"""
Pós-Graduação em Desenvolvimento de Sistemas com Python
    INTERFACE GRÁFICA COM O USUÁRIO EM PYTHON ESP
                      MAPA
       ALUNO: LEONARDO HENRIQUE MARIN KIST
"""


from PyQt5 import uic, QtWidgets
import sqlite3
import interface

#cadastro do imovel
def cadastrar():
    tipo_neg = interface.cb_TipoNeg.currentText()
    status = interface.cb_Status.currentText()
    end = interface.lineEdit_End.text()
    num = interface.lineEdit_Num.text()
    comp = interface.lineEdit_Comp.text()
    cep = interface.lineEdit_Cep.text()
    estado = interface.lineEdit_Est.text()
    cidade = interface.lineEdit_Cidade.text()
    bairro = interface.lineEdit_Bairro.text()
    tipo_imovel = interface.cb_TipoImovel.currentText()
    desc = interface.textEdit_Desc.toPlainText()
    caract = interface.textEdit_Caract.toPlainText()
    preco = interface.lineEdit_Preco.text()
    obs = interface.lineEdit_Obs.text()
    cond = interface.lineEdit_Cond.text()
    
   
    try:
        banco = sqlite3.connect('imoveis.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS imoveis (cod text, tipo_neg text, status text, end text, num text, comp text, cep text, estado text, cidade text, bairro text, tipo_imovel text, desc text, caract text, preco text, obs text, cond text)")
        
        #CODIFICÇAÃO AUTOMÁTICA
        #verifica se a tabela está vazia
        cursor.execute("SELECT COUNT(*) FROM imoveis")
        check = cursor.fetchall()
        if check[0][0]==0:
            cod = "%05i" % 1
            interface.lineEdit_ID.setText(cod)
            interface.label_10.setText("CADASTRADO COM SUCESSO")
        else:
            #verifica qual é o último item da tabela e aumenta em 1
            cursor.execute("SELECT * FROM imoveis ORDER BY cod DESC LIMIT 1")
            x = cursor.fetchone()[0]
            cod = str("%05i" % (int(x) + 1))
            
            #exibe o código cadastrado na caixa de texto
            interface.lineEdit_ID.setText(cod)
            interface.label_10.setText("CADASTRADO COM SUCESSO")

        cursor.execute("INSERT INTO imoveis VALUES('"+cod+"','"+tipo_neg+"','"+status+"','"+end+"','"+num+"','"+comp+"','"+cep+"','"+estado+"','"+cidade+"','"+bairro+"','"+tipo_imovel+"','"+desc+"','"+caract+"','"+preco+"','"+obs+"','"+cond+"')")
        banco.commit()
        banco.close()
    except sqlite3.Error as erro:
        print("Erro ao inserir os dados") 

def pesquisar():
    id = interface.lineEdit_ID.text()
    
    banco = sqlite3.connect('imoveis.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM imoveis WHERE cod = '"+id+"' ")
    result = cursor.fetchall()

    if result==[]:
        interface.label_10.setText("NENHUM CADASTRO ENCONTRADO")
        interface.cb_TipoNeg.setCurrentText("")
        interface.cb_Status.setCurrentText("")
        interface.lineEdit_End.setText("")
        interface.lineEdit_Num.setText("")
        interface.lineEdit_Comp.setText("")
        interface.lineEdit_Cep.setText("")
        interface.lineEdit_Est.setText("")
        interface.lineEdit_Cidade.setText("")
        interface.lineEdit_Bairro.setText("")
        interface.cb_TipoImovel.setCurrentText("")
        interface.textEdit_Desc.setText("")
        interface.textEdit_Caract.setText("")
        interface.lineEdit_Preco.setText("")
        interface.lineEdit_Obs.setText("")
        interface.lineEdit_Cond.setText("")
    else:
        interface.label_10.setText("CADASTRO ENCONTRADO")
        interface.cb_TipoNeg.setCurrentText(result[0][1])
        interface.cb_Status.setCurrentText(result[0][2])
        interface.lineEdit_End.setText(result[0][3])
        interface.lineEdit_Num.setText(result[0][4])
        interface.lineEdit_Comp.setText(result[0][5])
        interface.lineEdit_Cep.setText(result[0][6])
        interface.lineEdit_Est.setText(result[0][7])
        interface.lineEdit_Cidade.setText(result[0][8])
        interface.lineEdit_Bairro.setText(result[0][9])
        interface.cb_TipoImovel.setCurrentText(result[0][10])
        interface.textEdit_Desc.setText(result[0][11])
        interface.textEdit_Caract.setText(result[0][12])
        interface.lineEdit_Preco.setText(result[0][13])
        interface.lineEdit_Obs.setText(result[0][14])
        interface.lineEdit_Cond.setText(result[0][15])
    
    banco.commit()
    banco.close()  

def excluir():
    id = interface.lineEdit_ID.text()
    
    banco = sqlite3.connect('imoveis.db')
    cursor = banco.cursor()
    cursor.execute("DELETE FROM imoveis WHERE cod LIKE '"+id+"' ")
    result = cursor.fetchall()

    interface.label_10.setText("CADASTRO DELETADO COM SUCESSO")
    interface.cb_TipoNeg.setCurrentText("")
    interface.cb_Status.setCurrentText("")
    interface.lineEdit_End.setText("")
    interface.lineEdit_Num.setText("")
    interface.lineEdit_Comp.setText("")
    interface.lineEdit_Cep.setText("")
    interface.lineEdit_Est.setText("")
    interface.lineEdit_Cidade.setText("")
    interface.lineEdit_Bairro.setText("")
    interface.cb_TipoImovel.setCurrentText("")
    interface.textEdit_Desc.setText("")
    interface.textEdit_Caract.setText("")
    interface.lineEdit_Preco.setText("")
    interface.lineEdit_Obs.setText("")
    interface.lineEdit_Cond.setText("")
    interface.lineEdit_ID.setText("")

    banco.commit()
    banco.close()

app = QtWidgets.QApplication([])
interface=uic.loadUi("interface.ui")

interface.cb_TipoNeg.addItems(["","Venda","Locação","Venda/Locação"])
interface.cb_Status.addItems(["","Disponível","Locado","Vendido", "À Liberar"])
interface.cb_TipoImovel.addItems(["","Apartamento","Casa","Terreno"])
interface.lineEdit_ID.setMaxLength(5)

interface.pushButton.clicked.connect(cadastrar)
interface.bt_Consultar.clicked.connect(pesquisar)
interface.pushButton_2.clicked.connect(excluir)

interface.show()
app.exec()