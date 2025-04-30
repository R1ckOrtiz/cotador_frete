from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_peso_cubico(comprimento, largura, altura):
    return comprimento * largura * altura * 300

def calcular_valor_frete(peso_considerado, distancia_km, preco_por_kg, preco_por_km):
    return (peso_considerado * preco_por_kg) + (distancia_km * preco_por_km)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        comprimento = float(request.form['comprimento'])
        largura = float(request.form['largura'])
        altura = float(request.form['altura'])
        peso_real = float(request.form['peso_real'])
        distancia_km = float(request.form['distancia_km'])
        preco_por_kg = float(request.form['preco_por_kg'])
        preco_por_km = float(request.form['preco_por_km'])

        peso_cubico = calcular_peso_cubico(comprimento, largura, altura)
        peso_considerado = max(peso_real, peso_cubico)
        valor_frete = calcular_valor_frete(peso_considerado, distancia_km, preco_por_kg, preco_por_km)

        resultado = {
            'peso_cubico': round(peso_cubico, 2),
            'peso_considerado': round(peso_considerado, 2),
            'valor_frete': round(valor_frete, 2)
        }

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
