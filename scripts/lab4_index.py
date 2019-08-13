import requests, json                                                                                            
HEADERS = {'Content-type': 'application/json'}                                                                   
with open("datasets/sample.txt", "r") as data:                                                                   
    for index, row in enumerate(data):                                                                           
        document = json.dumps({"original":row})                                                                  
        response = requests.put('http://localhost:9200/lab4_index/_doc/{0}?pipeline=lab4_ingest_pipeline'.format(index), data=document, headers=HEADERS)
        if response.status_code == 200:                                                                          
            print(".", end='', flush=True)                                                                       
    print("")                                                                                                    
