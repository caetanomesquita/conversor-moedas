from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template("index.html")


@app.route("/api/convert")
def api_convert():
    origem = request.args.get("de")
    destino = request.args.get("para")
    valor = request.args.get("valor")

    try:
        url = f"https://api.frankfurter.app/latest?amount={valor}&from={origem}&to={destino}"
        resposta = requests.get(url)
        dados = resposta.json()

        cotacao = dados["rates"][destino]
        return jsonify({"resultado": cotacao})

    except KeyError:
        return jsonify({"erro": f"Não foi possível converter para {destino}. Essa moeda pode não ser suportada."}), 400
    except Exception:
        return jsonify({"erro": "Algo deu errado ao buscar a cotação. Tente novamente."}), 500


if __name__ == "__main__":
    app.run(debug=True)