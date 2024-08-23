# api/src/services/cliente_service.py
from sqlalchemy.orm import Session
from ..models.cliente import Cliente

class ClienteService:
    @staticmethod
    def create(db: Session, cliente: Cliente):
        db_cliente = Cliente(**cliente.dict())
        db.add(db_cliente)
        db.commit()
        db.refresh(db_cliente)
        return db_cliente

    @staticmethod
    def get(db: Session, cliente_id: int):
        return db.query(Cliente).filter(Cliente.id == cliente_id).first()

    @staticmethod
    def get_by_identificacion(db: Session, numero_identificacion: str):
        return db.query(Cliente).filter(Cliente.numero_identificacion == numero_identificacion).first()

    @staticmethod
    def update(db: Session, cliente_id: int, cliente: Cliente):
        db_cliente = ClienteService.get(db, cliente_id)
        for key, value in cliente.dict().items():
            setattr(db_cliente, key, value)
        db.commit()
        db.refresh(db_cliente)
        return db_cliente

    @staticmethod
    def delete(db: Session, cliente_id: int):
        db_cliente = ClienteService.get(db, cliente_id)
        db.delete(db_cliente)
        db.commit()
        return db_cliente

# api/src/services/servicio_service.py
# (Implementar servicios similares para Servicio)
