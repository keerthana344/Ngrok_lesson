from pydantic import BaseModel

class AddressSchema(BaseModel):
    user_id: int
    address: str
    city: str
    state: str
    zip_code: str
    country: str

class AddressUpdateSchema(BaseModel):
    address: str
    city: str
    state: str
    zip_code: str
    country: str
