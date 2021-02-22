import requests 

URL = "http://127.0.0.1:3030/kbe/update"

"""
Use of POST with requests module:
https://www.w3schools.com/python/ref_requests_post.asp
"""
query = 'PREFIX kbe:<http://www.kbe-solutions.com/shapes.owl#> ' + \
'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> ' + \
'DELETE ' + \
'{ ' + \
'kbe:cube_1 a kbe:Cube. ' + \
'kbe:cube_1 ?pred ?obj. ' + \
'}  ' + \
'WHERE ' + \
'{ ' + \
'kbe:cube_1 ?pred ?obj. ' + \
'}'



# defining a query params 
PARAMS = {'update': query} 
 
# sending get request and saving the response as response object 
r = requests.post(url = URL, data = PARAMS) 

#Checking the result
print("Result:", r.text)
