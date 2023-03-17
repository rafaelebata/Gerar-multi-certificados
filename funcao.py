from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import shutil
import zipfile
import os

#criar os imputs


def canva(colab,cpf, nomecu, data, cargh, nomeempresa, contprog, nomerestec, regist_resp, nomeinst, regist_inst):
    estilo = ParagraphStyle('Estilo do conteudo',
                            fontName='Helvetica',
                            fontSize=14,
                            leading=20)
    arquivo = canvas.Canvas(f'certificado - {colab}.pdf', pagesize=A4)
    arquivo.drawImage('arquivos/base_dados/modelo_canva.png', 0,0, width=600, height=850)
    arquivo.setFont('Helvetica', 14)
    arquivo.drawString(70, 645, f'{colab}' )
    arquivo.drawString(215, 622, f'{cpf}' )
    arquivo.drawString(70, 595, f'{nomecu}' )
    arquivo.drawString(210, 570, f'{data}' )
    arquivo.drawString(500, 570, f'{cargh}' )
    arquivo.drawString(70, 520, f'{nomeempresa}' )
    p1 = Paragraph( f'{contprog}',estilo)
    p1.wrapOn(arquivo, 470, 250)
    p1.drawOn(arquivo, 70, 200) 
    arquivo.drawString(45, 85, f'{nomerestec}')
    arquivo.drawString(45, 70, f'{regist_resp}' )
    arquivo.drawString(235, 85, f'{nomeinst}' )
    arquivo.drawString(420, 105, f'{colab}' )
    arquivo.drawString(235, 70, f'{regist_inst}' )
    arquivo.save() 

    return 

def zip(nome_zip, pasta):

    with zipfile.ZipFile(nome_zip, "w") as zip:
        for arquivo in os.listdir(pasta):
            caminho_completo = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho_completo):
                zip.write(caminho_completo, arquivo)

    return
        
def delete(pasta):

    for arquivo in os.listdir(pasta):
            caminho_completo = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho_completo):
                os.remove(caminho_completo)

    return

        

#gerar um PDF em A4


#criar pagina web
    #upload de modelo csv
    #dowload de modelo csv


