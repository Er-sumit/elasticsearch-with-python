from connect import *
#why this is 1000
max_documents_per_search = 1000
#search query for elasticsearch
es_query = {
  "query": {
    "match_all": {}
  }
}
es_query.update({"size": max_documents_per_search})
'''
this enable the code to be imported as module, 
so that code block written in main function below will be 
executed only when program is executed and not imported 
'''
if __name__ == "__main__":
    #get first 1000 documents using search query
    response = my_instance.search(index="kibana_sample_data_ecommerce",body=es_query,scroll="5m")
    '''
    In above line, three parameters are passed to search method
        1. index: The index on which search operation shall be performed
        2. query: This is changed from (body) [https://github.com/elastic/elasticsearch-py/issues/1698]
        3. scroll: Duration for which scroll should be alive (time out duration)

        The output of search query will be stored in response variable
        - number of documents found in search query can be found using
            len(response.get('hits',{}).get('hits'))
        - scroll_id can be found as
            response.get("_scroll_id")
    '''
    print(f"found {len(response.get('hits',{}).get('hits'))} number of documents")
    my_scroll_id = response.get('_scroll_id')
    
    #continue scrolling (searching) through es index until returned documents are not less than 1000
    while len(response.get('hits',{}).get('hits')) == max_documents_per_search:
        response = my_instance.scroll(scroll_id=my_scroll_id,scroll="1m")
        print(f"found {len(response.get('hits',{}).get('hits'))} number of documents")

