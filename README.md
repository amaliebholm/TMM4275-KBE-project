# Knowledge-Based Engineering Project 

This project is a part of the course TMM4275 Knowledge-Based Enineering, Project. The main task is making an automatic KBE system for manufacturing a coustom chair. From taking the client's order, checking if the order is within the constraints set by a product engineer, then making a model of the chair and ordering it from the factory.
The customar should be able to specify different sizes and shapes for the different parts of the chair, making their own custom chair. 

This project is made by: 
* Kasper Kallseter
* Magnus Myklegard
* Amalie Berge Holm


### The Chair

The image below show a NX modelling of the cair: 
![Chair_NX](https://github.com/amaliebholm/TMM4275-KBE-project/blob/main/Chair_NX.PNG)

the customer is able to define the following parameters for thir chair: 
* Length of legs
* Width of legs
* Hight og the back
* Depth of the seat
* Width of the seat
* Lenth og apron


### The KBE Application Architecture




### An Order Making Scenario


### Development Tools

This code was made using python in Visual Studio Code. Knowledge Fusion was used in NX to make models of the chair and Olingvi and Apache Jena Fuseki was used to communicate with the server containing the parameters, set by both the customer and the product engineer. 

To run the code you will need to hace a running Fuseki-Server and an correct Owl-file (in the Owl-folder) uploaded to the server. You also need tho change the paths in the code, to match the paths on yor own computer. 


### Code Description 

-- hhtpServer.py
-- manufChecker.py
-- ... 


### Examples of 3 product orders
