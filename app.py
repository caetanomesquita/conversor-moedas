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
        valor_float = float(valor)

        url = f"https://api.frankfurter.dev/v2/rate/{origem}/{destino}"
        resposta = requests.get(url, timeout=8)
        dados = resposta.json()

        taxa = dados["rate"]
        resultado = round(valor_float * taxa, 4)

        return jsonify({"resultado": resultado})

    except KeyError:
        return jsonify({"erro": f"Não foi possível converter para {destino}. Essa moeda pode não ser suportada."}), 400
    except Exception:
        return jsonify({"erro": "Algo deu errado ao buscar a cotação. Tente novamente."}), 500

if __name__ == "__main__":
    app.run(debug=True)