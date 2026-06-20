#Importacao de frameworks
from flask import Flask, jsonify, request
from flask_cors import CORS

#Criar o nosso app
app = Flask(__name__)

#Habilitar o CORS - Conexões entre diferentes origens
CORS(app)

#Criando nosso banco de dado local
produtos = [
    {"id" : 1,
     "nome" : "Notebook Gamer",
     "preco" : 4000
     },
    {"id" : 2,
     "nome" : "Cadeira Gamer",
     "preco" : 300
     },
    {"id" : 3,
     "nome" : "Mouse Gamer",
     "preco" : 100
     },
    {"id" : 4,  
     "nome" : "Teclado",
     "preco" : 200
     }
]

#Criar rota para metodo GET (Visualizar produtos)
@app.route("/listar", methods=['GET'])
def exibirProdutos():
    return jsonify(produtos)


#Criar uma rota para o metodo POST (Criar um produto)
@app.route("/criar", methods=['POST'])
def criarProduto():
    produtoNovo = request.get_json()
    produtos.append(produtoNovo)
    return jsonify(produtoNovo), 201

#Criar uma rota para o metodo PUT (atualizar um produto)
@app.route("/atualizar/<int:id>", methods=['PUT'])
def atualizarProduto(id):
    produtoAtualizado = request.get_json()
    for produto in produtos:
        if produto["id"] == id:
            produto["preco"] = produtoAtualizado["preco"]
            produto["nome"] = produtoAtualizado["nome"];
            return jsonify(produto), 200           
    return jsonify({"message": "Produto não encontrado"}), 404

#Criar uma rota para o metodo DELETE (deletar um produto)
@app.route("/deletar/<int:id>", methods=['DELETE'])
def deletarProduto(id):
    for produto in produtos:
        if produto["id"] == id:
            produtos.remove(produto)
            return jsonify({"messagem": "Produto deletado com sucesso"}), 200
    return jsonify({"message": "Produto não encontrado"}), 404



#Rodar o programa
if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0")