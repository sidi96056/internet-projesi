from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('OBS.html')

@app.route('/login')
def login():
    return render_template('giris.html')

@app.route('/register')
def register():
    return render_template('kayit_ol.html')

@app.route('/dashboard')
def dashboard():
    return render_template('duyurlar.html')

@app.route('/gunluk/ekle')
def gunluk_ekle():
    return render_template('gunluk_ekle.html')

@app.route('/Akademik/Yönetim')
def Akademik_Yönetim():
    return render_template('Akademik_Yönetim.html')

@app.route('/Güvenlik/ve/Uyumluluk')
def Güvenlik_ve_Uyumluluk():
    return render_template('Güvenlik_ve_Uyumluluk.html')

@app.route('/Kayıt/ve/Kayıt/Yenileme')
def Kayıt_ve_Kayıt_Yenileme():
    return render_template('Kayıt_ve_Kayıt_Yenileme.html')

if __name__ == '__main__':
    app.run(debug=True) 