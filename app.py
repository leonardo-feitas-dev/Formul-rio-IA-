from flask import Flask, render_template, request, jsonify
import psycopg2
from db_config import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT nome FROM Categorias")
        categorias = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('index.html', categorias=categorias)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/add_categoria', methods=['POST'])
def add_categoria():
    data = request.json
    nome = data['nome']

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Verificar se a categoria já existe
        cur.execute("SELECT id FROM Categorias WHERE nome = %s", (nome,))
        existing_categoria = cur.fetchone()
        
        if existing_categoria:
            return jsonify({"status": "error", "message": "Categoria já registrada"}), 409

        cur.execute("INSERT INTO Categorias (nome) VALUES (%s)", (nome,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "success"}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/add_modelo', methods=['POST'])
def add_modelo():
    data = request.json
    nome = data['nome']
    descricao = data['descricao']
    plano = data['plano']
    categorias = data['categorias']

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Verificar se o nome já existe
        cur.execute("SELECT id FROM ModelosIA WHERE nome = %s", (nome,))
        existing_modelo = cur.fetchone()
        
        if existing_modelo:
            return jsonify({"status": "error", "message": "Nome do modelo já registrado"}), 409

        cur.execute("INSERT INTO ModelosIA (nome, descricao, plano, categorias) VALUES (%s, %s, %s, %s)",
                    (nome, descricao, plano, categorias))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "success"}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/categorias')
def categorias():
    return render_template('categorias.html')

@app.route('/modelos')
def modelos():
    plano = request.args.get('plano')
    categoria = request.args.get('categoria')

    query = "SELECT * FROM ModelosIA"
    conditions = []
    params = []

    if plano:
        conditions.append("plano = %s")
        params.append(plano)
    
    if categoria:
        conditions.append("%s = ANY(categorias)")
        params.append(categoria)
    
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query, params)
        modelos = cur.fetchall()
        cur.execute("SELECT nome FROM Categorias")
        categorias = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('modelos.html', modelos=modelos, categorias=categorias)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
