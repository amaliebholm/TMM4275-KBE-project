# Reading from OWL on FUSEKI and updating DFA file.
import requests 

constraints = ["legLengthMax","legLengthMin", "legWidthMax", "legWidthMin",
    "backMax", "backMin", "seatDepthMax", "seatDepthMin",
    "seatWidthMax", "seatWidthMin", "apronMax", "apronMin"]
URL = "http://127.0.0.1:3030/kbe/query"

for c in constraints:
    PARAMS = {'query':'PREFIX kbe:<http://www.kbe_chair.com/.owl#> SELECT ?data WHERE {?inst kbe:' + c + ' ?data.}'} 

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()
    print(c, data['results']['bindings'][0]['data']['value'])
    
#Checking the result
#data = r.json()
#print("Data:", data['results']['bindings'][0]['data']['value'])