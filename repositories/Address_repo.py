from models import Address
from sqlalchemy.orm import Session

class AddressRepo:
    def __init__(self, db: Session):
        self.db = db

    def add_address(self, address: Address):
        self.db.add(address)
        self.db.commit()
        return address

    def get_all_addresses(self, skip: int = 0, limit: int = 100):
        return self.db.query(Address).offset(skip).limit(limit).all()

    def get_address_by_id(self, id: int):
        return self.db.query(Address).filter(Address.id == id).first()

    def get_addresses_by_user_id(self, user_id: int):
        return self.db.query(Address).filter(Address.user_id == user_id).all()

    def update_address(self, address: Address):
        self.db.add(address)
        self.db.commit()
        return address

    def delete_address(self, address: Address):
        self.db.delete(address)
        self.db.commit()
