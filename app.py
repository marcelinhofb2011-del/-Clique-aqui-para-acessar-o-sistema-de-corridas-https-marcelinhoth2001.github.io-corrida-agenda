from flask import Flask, render_template_string, request

app = Flask(__name__)

# Lista para armazenar corridas
corridas = []

# HTML da página (formulário + lista de corridas)
HTML = """
<!doctype html>
<html>
  <head>
    <title>Corrida Particular</title>
    <style>
      body { font-family: Arial; margin: 40px; }
      input, select { padding: 8px; width: 250px; margin: 5px; }
      button { padding: 10px 20px; background: green; color: white; border: none; }
      table { border-collapse: collapse; margin-top: 20px; width: 100%; }
      th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
      th { background: #f2f2f2; }
    </style>
  </head>
  <body>
    <h1>🚗 Sistema de Corrida Particular</h1>
    <form method="post">
      <label>Origem:</label><br>
      <input type="text" name="origem" required><br>
      <label>Destino:</label><br>
      <input type="text" name="destino" required><br>
      <label>Distância (km):</label><br>
      <input type="number" name="km" step="0.1" required><br>
      <label>Data:</label><br>
      <input type="date" name="data" required><br>
      <label>Hora:</label><br>
      <input type="time" name="hora" required><br>
      <label>Forma de pagamento:</label><br>
      <select name="pagamento">
        <option>Dinheiro</option>
        <option>Pix</option>
        <option>Cartão</option>
      </select><br><br>
      <button type="submit">Agendar Corrida</button>
    </form>

    {% if valor %}
      <h2>💰 Valor da corrida: R$ {{ valor }}</h2>
    {% endif %}

    {% if corridas %}
      <h2>📋 Corridas Agendadas</h2>
      <table>
        <tr>
          <th>Data</th>
          <th>Hora</th>
          <th>Origem</th>
          <th>Destino</th>
          <th>Distância (km)</th>
          <th>Valor (R$)</th>
          <th>Pagamento</th>
        </tr>
        {% for c in corridas %}
        <tr>
          <td>{{ c.data }}</td>
          <td>{{ c.hora }}</td>
          <td>{{ c.origem }}</td>
          <td>{{ c.destino }}</td>
          <td>{{ c.km }}</td>
          <td>{{ c.valor }}</td>
          <td>{{ c.pagamento }}</td>
        </tr>
        {% endfor %}
      </table>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    valor = None
    if request.method == "POST":
        origem = request.form["origem"]
        destino = request.form["destino"]
        km = float(request.form["km"])
        data = request.form["data"]
        hora = request.form["hora"]
        pagamento = request.form["pagamento"]
        valor = round(km * 2.0, 2)  # R$ 2,00 por km

        # Adiciona corrida à lista
        corrida = {
            "origem": origem,
            "destino": destino,
            "km": km,
            "valor": valor,
            "data": data,
            "hora": hora,
            "pagamento": pagamento
        }
        corridas.append(corrida)

    return render_template_string(HTML, valor=valor, corridas=corridas)

if __name__ == "__main__":
    app.run(debug=True)
