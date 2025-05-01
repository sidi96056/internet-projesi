from flask import Flask, render_template ,request 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('obb.htm')

@app.route('/login')
def login():
    return render_template('giris.html')

@app.route('/register')
def register():
    return render_template('kayit_ol.html')

@app.route('/dashboard')
def dashboard():
    return render_template('duyurlar.html')

@app.route('/Akademik')
def Akademik():
    return render_template('Akademik.html')

@app.route('/Uyumluluk')
def Uyumluluk():
    return render_template('Uyumluluk.html')

@app.route('/Yenileme')
def Yenileme():
    return render_template('Yenileme.html')

if __name__ == '__main__':
    app.run(debug=True) 
