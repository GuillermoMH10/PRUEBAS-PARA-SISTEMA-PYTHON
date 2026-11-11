from flask import Blueprint, render_template, request, jsonify
from app.models.contacto import ContactoModel

contactos_bp = Blueprint('contactos', __name__)


@contactos_bp.route('/', methods=['GET'])
def index():
    contactos = ContactoModel.listar_todos()
    return render_template('index.html', contactos=contactos)


@contactos_bp.route('/api/contactos', methods=['GET'])
def api_listar():
    contactos = ContactoModel.listar_todos()
    return jsonify({'ok': True, 'data': contactos})


@contactos_bp.route('/api/contactos', methods=['POST'])
def api_crear():
    data = request.get_json(silent=True) or request.form
    nombre = (data.get('nombre') or '').strip()
    apellido = (data.get('apellido') or '').strip()
    telefono = (data.get('telefono') or '').strip()
    correo = (data.get('correo') or '').strip()

    if not all([nombre, apellido, telefono, correo]):
        return jsonify({'ok': False, 'error': 'Todos los campos son obligatorios.'}), 400

    nuevo_id = ContactoModel.crear(nombre, apellido, telefono, correo)
    contacto = ContactoModel.obtener_por_id(nuevo_id)
    return jsonify({'ok': True, 'data': contacto}), 201


@contactos_bp.route('/api/contactos/<int:contacto_id>', methods=['PUT'])
def api_actualizar(contacto_id):
    data = request.get_json(silent=True) or request.form
    nombre = (data.get('nombre') or '').strip()
    apellido = (data.get('apellido') or '').strip()
    telefono = (data.get('telefono') or '').strip()
    correo = (data.get('correo') or '').strip()

    if not all([nombre, apellido, telefono, correo]):
        return jsonify({'ok': False, 'error': 'Todos los campos son obligatorios.'}), 400

    actualizado = ContactoModel.actualizar(contacto_id, nombre, apellido, telefono, correo)
    if not actualizado:
        return jsonify({'ok': False, 'error': 'Registro no encontrado.'}), 404

    contacto = ContactoModel.obtener_por_id(contacto_id)
    return jsonify({'ok': True, 'data': contacto})


@contactos_bp.route('/api/contactos/<int:contacto_id>', methods=['DELETE'])
def api_eliminar(contacto_id):
    eliminado = ContactoModel.eliminar(contacto_id)
    if not eliminado:
        return jsonify({'ok': False, 'error': 'Registro no encontrado.'}), 404
    return jsonify({'ok': True})
