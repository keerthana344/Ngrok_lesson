from models import Order
from sqlalchemy.orm import Session

class OrderRepo:
    def __init__(self, db: Session):
        self.db = db

    def add_order(self, order: Order):
        self.db.add(order)
        self.db.commit()
        return order

    def get_all_orders(self, skip: int = 0, limit: int = 100):
        return self.db.query(Order).offset(skip).limit(limit).all()

    def get_order_by_id(self, id: int):
        return self.db.query(Order).filter(Order.id == id).first()

    def get_orders_by_user_id(self, user_id: int):
        return self.db.query(Order).filter(Order.user_id == user_id).all()

    def update_order(self, order: Order):
        self.db.add(order)
        self.db.commit()
        return order

    def delete_order(self, order: Order):
        self.db.delete(order)
        self.db.commit()
