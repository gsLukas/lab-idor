from flask import Flask, request, jsonify, render_template, redirect, make_response
import jwt
import datetime

app = Flask(__name__)
app.secret_key = 'segredo-muito-seguro'  # usado para JWT

USERS_DB = {
    1: {"id": 1, "username": "lukao", "password": "1234", "email": "lukao@ctf.local", "saldo": 90000},
    2: {"id": 2, "username": "admin", "password": "admin", "email": "admin@ctf.local", "saldo": 999999},
    3: {"id": 3, "username": "user", "password": "user", "email": "user@ctf.local", "saldo": 100},
    4: {"id": 4, "username": "guest", "password": "guest", "email": "guest@ctf.local", "saldo": 0} 
}

JWT_SECRET = 'lab-idor-chave'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    for user in USERS_DB.values():
        if user['username'] == data.get('username') and user['password'] == data.get('password'):
            token = jwt.encode({
                'user_id': user['id'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, JWT_SECRET, algorithm='HS256')

            return jsonify({
                "token": token,
                "user": {
                    "id": user['id'],
                    "username": user['username'],
                    "email": user['email'],
                    "saldo": user['saldo']
                }
            })
    return jsonify({"error": "Credenciais inválidas"}), 401



@app.route('/api/get_profile_data', methods=['GET'])
def get_profile_data():
    auth = request.headers.get('Authorization')
    if not auth or not auth.startswith("Bearer "):
        return jsonify({"error": "Token ausente"}), 401

    token = auth.split(" ")[1]
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user_id_from_token = decoded['user_id']
    except Exception as e:
        return jsonify({"error": "Token inválido"}), 403
    
    requested_id = request.args.get("user_id", type=int)
    if requested_id:
        user = USERS_DB.get(requested_id)
    else:
        user = USERS_DB.get(user_id_from_token)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    return jsonify({
        "username": user["username"],
        "email": user["email"],
        "saldo": user["saldo"]
    })

@app.route('/api/get_user_info', methods=['GET'])
def get_user_info():
#fake
    return jsonify({"info": "Endpoint de exemplo. Nenhum dado sensível aqui."})

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/seguranca')
def seguranca():
    return render_template('seguranca.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True)
