from pydantic import BaseModel, RootModel


class Order(BaseModel):
    id: int
    courierId: None
    firstName: str
    lastName: str
    address: str
    metroStation: str
    phone: str
    rentTime: int
    deliveryDate: str
    track: int
    color: list
    comment: str
    createdAt: str
    updatedAt: str
    status: int


class Orders(RootModel):
    root: list[Order]
