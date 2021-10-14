from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import pyqrcode
from gtts import gTTS

app = Flask(__name__, template_folder='./templates')

def generate_qr_code(url, filename):
    qr = pyqrcode.create(url + '/'+filename+'.mp3')
    qr.svg('./static/qr-codes/'+filename+'.svg', scale=8)
    qr.png('./static/qr-codes/'+filename+'.png', scale=10, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    print(qr.terminal(quiet_zone=1))

def generate_audio(audio_text, filename):
    tts = gTTS(text=audio_text, lang='pt-br')
    tts.save('./static/audio/'+filename+'.mp3')

@app.route('/')
def start_base():
    return render_template('base.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    produto = request.form['produto']
    volume = request.form['volume']
    ibu = request.form['ibu']
    teor_alcoolico = request.form['teorAlcoolico']
    validade = request.form['validade']
    ingredientes = request.form['ingredientes']
    descricao = request.form['descricao']

    message = 'Cerveja ' + produto + '. '
    message += 'Volume de ' + volume + ' mililitros. '
    message += 'IBU ' + ibu + '. '
    message += 'Teor alcóolico de ' + teor_alcoolico + ' por cento. '
    message += 'Validade: ' + validade + '. '
    message += 'Contém: ' + ingredientes + '. '
    message += descricao

    now = datetime.now()
    date_string = now.strftime("%Y%m%d%H%M%S")
    filename = 'qr' + date_string

    url = request.url_root

    # url = 'http://192.168.68.200:5000'
    url += 'static/audio'

    generate_qr_code(url, filename)
    generate_audio(message, filename)

    # print(message)

    return redirect('/static/qr-codes/'+filename+'.png')