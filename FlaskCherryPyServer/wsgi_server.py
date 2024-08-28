from flask import Flask, jsonify, request
import cherrypy

# Criação do aplicativo Flask
app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Servidor rodando com WSGI e CherryPy"}), 200

@app.route('/hello', methods=['GET'])
def hello():
    nome = request.args.get('nome', 'mundo')
    return jsonify({"message": f"Olá, {nome}!"}), 200

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    soma = num1 + num2
    return jsonify({"resultado": soma}), 200

if __name__ == '__main__':
    # Configuração para o CherryPy
    cherrypy.config.update({
       'server.socket_host': '0.0.0.0', # Define o host para todas as interfaces de rede
       'server.socket_port': 5000,      # Define a porta do servidor
       'log.screen': True               # Exibe logs no console
   })

    # Monta o aplicativo Flask como um servidor WSGI (Web Server Gateway Interface) no cherryPy
    cherrypy.tree.graft(app.wsgi_app, "/")

    # Inicia o servidor CherryPy
    cherrypy.engine.start()
    cherrypy.engine.block()