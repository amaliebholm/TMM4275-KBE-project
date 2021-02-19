# Reading from OWL on FUSEKI and updating DFA file.
import requests 

URL = "http://127.0.0.1:3030/kbe/query"
  
# defining a query params 
PARAMS = {'query':'PREFIX kbe:<http://www.kbe_chair.com/.owl#>SELECT ?var WHERE {?apron a kbe:Apron.?Apron kbe:apronMax ?var.}'} 
        # ?subject = ? what we would like to retrieve (cube a kbe:)
            #kbe: = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>'
        # ?predicate (cube kbe:hasSide)
        # ?object (side)

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 

#Checking the result
print("Result:", r.text)
data = r.json()
print("JSON:", data)


  
                            #SELECT ?var WHERE {?apron a kbe:Apron.?Apron kbe:apronMax ?var.}

URL = "http://127.0.0.1:3030/kbe/update"

# Defining a query in oder to delete previous value
PARAMS = {'update':'PREFIX kbe:<http://www.kbe_chair.com/.owl#> DELETE {?apron kbe:apronMax ?var.} WHERE { ?apron kbe:apronMax ?var.}'}
	
# Sending get request and saving the returning parameters
r = requests.post(url = URL, data = PARAMS) 

#Checking the result
print("Result for DELETE query:", r.text)
		

PARAMS = {'update':'PREFIX kbe:<http://www.kbe_chair.com/.owl#> INSERT { ?apron kbe:apronMax "' + str(25) + '" ^^<http://www.w3.org/2001/XMLSchema#int>.} WHERE { ?apron a kbe:Apron.}'} 

# sending get request and saving the response as response object 
r = requests.post(url = URL, params = PARAMS) 

#Checking the result
print("Result of INSERT query:", r.text)
