# app.py
from flask import Flask, request, jsonify, render_template
from db_config import get_db_connection

app = Flask(__name__)

# Obtener todos los productos
@app.route('/api/productos', methods=['GET'])
def get_productos():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(productos)

# Obtener todos los usuarios
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(usuarios)

# Añadir un producto
@app.route('/api/producto', methods=['POST'])
def add_producto():
    nuevo_producto = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO productos (nombre, precio_venta, tipo, imagen_url) VALUES (%s, %s, %s, %s)',
                   (nuevo_producto['nombre'], nuevo_producto['precio_venta'], nuevo_producto['tipo'], nuevo_producto['imagen_url']))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Producto añadido'}), 201

# Añadir un usuario
@app.route('/api/usuario', methods=['POST'])
def add_usuario():
    nuevo_usuario = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)',
                   (nuevo_usuario['nombre'], nuevo_usuario['email'], nuevo_usuario['password']))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Usuario añadido'}), 201

# Modificar un producto
@app.route('/api/producto/<int:id>', methods=['PUT'])
def update_producto(id):
    datos_producto = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE productos SET nombre=%s, precio_venta=%s, tipo=%s, imagen_url=%s WHERE id=%s',
                   (datos_producto['nombre'], datos_producto['precio_venta'], datos_producto['tipo'], datos_producto['imagen_url'], id))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Producto actualizado'})

# Modificar un usuario
@app.route('/api/usuario/<int:id>', methods=['PUT'])
def update_usuario(id):
    datos_usuario = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE usuarios SET nombre=%s, email=%s, password=%s WHERE id=%s',
                   (datos_usuario['nombre'], datos_usuario['email'], datos_usuario['password'], id))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Usuario actualizado'})

# Borrar un producto
@app.route('/api/producto/<int:id>', methods=['DELETE'])
def delete_producto(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM productos WHERE id=%s', (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Producto borrado'})

# Borrar un usuario
@app.route('/api/usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id=%s', (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Usuario borrado'})

# Páginas HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

if __name__ == '__main__':
    app.run(debug=True)
