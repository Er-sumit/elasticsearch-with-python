import uuid
from User import *
from es_connect import *
es_index = 'es_app_01'

class Wallet():
    def __init__(self) -> None:
        pass
    def create(self,**kwargs):
        if kwargs.get("currency") == "INR" and kwargs.get("user_email") is not None:
            this_user = User()
            user_exists = this_user.check_user(kwargs.get("user_email"))
            if user_exists:
                es_document = {
                    "email": kwargs.get("user_email"),
                    "wallet_currency" : "INR",
                    "wallet_balance": 0,
                    "wallet_status": "active"
                }
                es_response = my_instance.index(index=es_index, id=str(uuid.uuid4()), body=es_document)
                if es_response.get('result') == 'created':
                    return({'request_status': 'success','status':'Wallet Created for user with email '+ kwargs.get("user_email")})
            else:
                return({'request_status': 'error','status':'Not Created','caused_by': 'Account with email ' + kwargs.get("user_email")+' not found'})
        else:
            return({'request_status': 'error','status':'Not Created','caused_by': 'user_email must be provided and currency must be INR'})