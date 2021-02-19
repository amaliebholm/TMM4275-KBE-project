# Reading from OWL on FUSEKI and updating DFA file.
import requests 

URL = "http://127.0.0.1:3030/kbe/query"
  
# defining a query params 
PARAMS = {'query':'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>SELECT ?side WHERE {?cube a kbe:Cube.?cube kbe:hasSide ?side.}'} 
        # ?subject = ? what we would like to retrieve (cube a kbe:)
            #kbe: = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>'
        # ?predicate (cuve kbe:hasSide)
        # ?object (side)

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 

#Checking the result
print("Result:", r.text)
data = r.json()
print("JSON:", data)
