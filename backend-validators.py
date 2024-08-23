# api/src/utils/validators.py
from ..models.cliente import Cliente
from ..models.servicio import Servicio

def validate_cliente(cliente: Cliente):
    if not all([cliente.tipo_identificacion, cliente.numero_identificacion, cliente.nombres, 
                cliente.apellidos, cliente.fecha_nacimiento, cliente.direccion, 
                cliente.ciudad, cliente.departamento, cliente.pais, 
                cliente.telefono, cliente.email]):
        raise ValueError("Todos los campos son obligatorios")
    
    valid_tipos = ["CC", "TI", "CE", "RC"]
    if cliente.tipo_identificacion not in valid_tipos:
        raise ValueError(f"Tipo de identificación inválido. Debe ser uno de: {', '.join(valid_tipos)}")

def validate_servicio(servicio: Servicio):
    if not all([servicio.tipo_servicio, servicio.cliente_id]):
        raise ValueError("Todos los campos son obligatorios")
    
    valid_servicios = ["Internet 200 MB", "Internet 400 MB", "Internet 600 MB", "Directv Go", "Paramount+", "Win+"]
    if servicio.tipo_servicio not in valid_servicios:
        raise ValueError(f"Tipo de servicio inválido. Debe ser uno de: {', '.join(valid_servicios)}")
