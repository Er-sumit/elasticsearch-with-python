import uuid

from werkzeug.wrappers import response
from es_connect import *
from uuid import *
es_index = 'es_app_01'

class User():
    def __init__(self) -> None:
        pass
    def create(self, **kwargs):
        if kwargs.get('name') is None or kwargs.get('email') is None:
            return({'status': 'Not Created', 'caused by': 'name or email not provided'})
        else:
            user_id = str(uuid.uuid4())
            es_document = {
                'name': kwargs.get('name'),
                'email': kwargs.get('email'),
                'user_type': 'general'
            }
            #below query to check if requested email id is already present in elasticsearch database/index
            es_query_email_check = {
                "query" : {
                    "match": {
                        "email.keyword": kwargs.get('email')
                    }
                }
            }
            es_email_check = my_instance.search(index=es_index,body=es_query_email_check)
            if es_email_check.get('hits',{}).get('total',{}).get('value') > 0:
                return({'status': 'User Not Created', 'caused by': 'user with email ' + kwargs.get('email') + ' already exists'})
            es_response = my_instance.index(index=es_index,id=user_id,body=es_document)
            if es_response.get('result') == 'created':
                return({'status': 'User Created', 'user_id': user_id})
            else:
                print(f"index operation to elasticsearch failed for body={es_document}, request failed by = {response}")
                return({'status': 'User Creation Failed', 'caused_by': 'System Error'})
        
    def get_users(self):
        es_query = {
            "query": {
                "match_all": {}
            }
        }
        es_response = my_instance.search(index=es_index, body=es_query)
        data=[]
        for item in es_response.get('hits',{}).get('hits',[]):
            data.append(item.get('_source',{}))
        return (data)
    
    def check_user(self,email):
        #below query to check if requested email id is already present in elasticsearch database/index
        es_query_email_check = {
            "query" : {
                "match": {
                    "email.keyword": email
                }
            }
        }
        es_email_check = my_instance.search(index=es_index,body=es_query_email_check)
        if es_email_check.get('hits',{}).get('total',{}).get('value') > 0:
            return True
        else:
            return False