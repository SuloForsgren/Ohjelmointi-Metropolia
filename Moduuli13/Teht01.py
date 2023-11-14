from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<annettu_arvo>')
def alkuluku(annettu_arvo):
    for i in range(2, int(annettu_arvo)):

        if int(annettu_arvo) % i == 0:
            return {
                "Number": annettu_arvo,
                "isPrime": False,
            }
        
    return {
        "Number": annettu_arvo,
        "isPrime": True,
    }

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)