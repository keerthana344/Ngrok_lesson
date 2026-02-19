from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderSchema(BaseModel):
    user_id: int
    address_id: int
    order_date: datetime
    total_price: int
    status: str

class OrderUpdateStatus(BaseModel):
    status: str
