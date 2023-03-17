from flask import Flask, render_template, redirect, request, flash, send_from_directory
import os
import pandas as pd
import shutil

import funcao
from datetime import datetime



app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwertyu1234'

@app.route ('/')
def home ():
    return  render_template ('app_certificado.html')

@app.route('/certificados', methods=['POST'])
def coleta ():

    nomeempresa = request.form.get('empresa')
    data = request.form.get('datacurso')
    nomeinst = request.form.get('nomeinstrutor')
    regist_inst =  request.form.get('registroinstrutor')
    nomerestec =  request.form.get('nomeresponsavel')
    regist_resp =  request.form.get('registroresponsavel')
    contprog =  request.form.get('conteudo')
    cargh =  request.form.get('cargahorario')
    nomecu =  request.form.get('nomecurso')
    colab =  request.form.get('nomecolab')
    cpf =  request.form.get('cpf')

    corrige = datetime.strptime(data, '%Y-%m-%d')
    data1 = corrige.strftime('%d/%m/%Y')
    
    if os.path.exists('arquivos/certificado/Modelo_de_preenchimento.csv'):

        tab = pd.read_csv('arquivos/certificado/Modelo_de_preenchimento.csv',encoding = 'UTF-8',sep=';')

        n_certificados = len(tab.index)

        for certificado in range(n_certificados):

            for indice, linha in tab.iterrows():
                break
            indice = indice
            colab = (linha['Nome'])
            cpf = (linha['CPF'])

            funcao.canva(colab, cpf, nomecu, data1, cargh, nomeempresa, contprog, nomerestec, regist_resp, nomeinst, regist_inst)

            tab = tab.drop(indice) 

            shutil.move(f'certificado - {colab}.pdf', 'arquivos/certificado/')

    else:

        funcao.canva(colab, cpf, nomecu, data1, cargh, nomeempresa, contprog, nomerestec, regist_resp, nomeinst, regist_inst)

        shutil.move(f'certificado - {colab}.pdf', 'arquivos/certificado/')
    
    pasta = "arquivos/certificado/"
    nome_zip = "certificados.zip"
    
    funcao.zip(nome_zip, pasta)

    funcao.delete(pasta)

    return send_from_directory('', 'certificados.zip', as_attachment=True)



@app.route('/download', methods=['POST'])
def download ():

    return send_from_directory('arquivos/download', 'Modelo_de_preenchimento.csv', as_attachment=True)

@app.route("/upload", methods=['POST'])
def upload():
    
    arquivo = request.files.get('documento')
    nome_arquivo = arquivo.filename.replace(" ","")
    if nome_arquivo == 'Modelo_de_preenchimento.csv':
        arquivo.save(os.path.join('arquivos/certificado', nome_arquivo))
        flash('Arquivo enviado, preencha os campos e gere os certificados!')
    else:
        flash('Erro! arquivo enviado diferente do modelo baixado, faça download do aquivo e envie com o mesmo titulo e extensão')

    return redirect('/')




if __name__ == '__main__':
    app.run(debug=True)