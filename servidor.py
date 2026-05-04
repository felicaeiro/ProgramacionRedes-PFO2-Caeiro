from flask import Flask
from routes.auth_routes import auth_bp
from routes.tareas_routes import tareas_bp
from database import crear_tablas

app = Flask(__name__)

crear_tablas()

app.register_blueprint(auth_bp)
app.register_blueprint(tareas_bp)

if __name__ == "__main__":
    app.run(debug=True)