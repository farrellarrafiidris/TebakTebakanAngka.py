from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize global variables
angka_rahasia = None
percobaan = 0

def reset_game():
    global angka_rahasia, percobaan
    angka_rahasia = random.randint(1, 100)
    percobaan = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global percobaan
    message = ''
    if request.method == 'POST':
        angka_tebakan = int(request.form['angka_tebakan'])
        percobaan += 1
        if angka_tebakan < angka_rahasia:
            message = "Angka tebakan terlalu kecil!"
        elif angka_tebakan > angka_rahasia:
            message = "Angka tebakan terlalu besar!"
        else:
            message = f'Selamat, Anda berhasil menebak angka dalam {percobaan} percobaan!'
            reset_game()
    return render_template('index.html', message=message)

if __name__ == '__main__':
    import random
    reset_game()
    app.run(debug=True)
