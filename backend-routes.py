# api/src/routes/cliente_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.database import get_db
from ..models.cliente import Cliente
from ..services.cliente_service import ClienteService
from ..utils.validators import validate_cliente

router = APIRouter()

@router.post("/clientes/")
def create_cliente(cliente: Cliente, db: Session = Depends(get_db)):
    validate_cliente(cliente)
    existing_cliente = ClienteService.get_by_identificacion(db, cliente.numero_identificacion)
    if existing_cliente:
        raise HTTPException(status_code=400, detail="El registro ya existe")
    return ClienteService.create(db, cliente)

@router.get("/clientes/{cliente_id}")
def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = ClienteService.get(db, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.put("/clientes/{cliente_id}")
def update_cliente(cliente_id: int, cliente: Cliente, db: Session = Depends(get_db)):
    validate_cliente(cliente)
    existing_cliente = ClienteService.get(db, cliente_id)
    if existing_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return ClienteService.update(db, cliente_id, cliente)

@router.delete("/clientes/{cliente_id}")
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    existing_cliente = ClienteService.get(db, cliente_id)
    if existing_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return ClienteService.delete(db, cliente_id)

# api/src/routes/servicio_routes.py
# (Implementar rutas similares para Servicio)
