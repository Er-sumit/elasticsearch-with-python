from connect import *
from wallet.Wallet import *
import uuid
document_1 = {
    "name": "asdas",
    "City": "UN",
    "asdf": 3,
    "date": "2021-12-15T13:12:00"
}

def write_my_data(document,es_index="app_wallet_01"):
    my_instance.index(index=es_index,body=document_1,id=str(uuid.uuid4()))

write_my_data(document_1)