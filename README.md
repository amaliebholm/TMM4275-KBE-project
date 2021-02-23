# Knowledge-Based Engineering Project 

This project is a part of the course TMM4275 Knowledge-Based Enineering, Project. The main task is making an automatic KBE system for manufacturing a coustom chair. From taking the client's order, checking if the order is within the constraints set by a product engineer, then making a model of the chair and ordering it from the factory.
The customar should be able to specify different sizes and shapes for the different parts of the chair, making their own custom chair. 

This project is made by: 
* Kasper Kallseter
* Magnus Myklegard
* Amalie Berge Holm


### The Chair

The image below show a NX modelling of the cair: 
![Chair_NX](https://github.com/amaliebholm/TMM4275-KBE-project/blob/main/Images/Chair_NX.PNG)

the customer is able to define the following parameters for thir chair: 
* Length of legs
* Width of legs
* Hight of the back
* Depth of the seat
* Width of the seat
* Lenth of apron


### The KBE Application Architecture

This is a diagram showing Client-Server architecture, and how the information travels through the different sercers and tools to make it possible for the customer to order the chair. 

![Client-Server](https://github.com/amaliebholm/TMM4275-KBE-project/blob/main/Images/Client-Server.png)


### An Order Making Scenario

This is an ULM sketch, showing how an order making scenario will play out. From the enineer defining constraits and the customer defining parameters for the chair, to the order being made. 

![ULM:PNG](https://github.com/amaliebholm/TMM4275-KBE-project/blob/main/Images/ULM.PNG)


### Development Tools

This code was made using python in Visual Studio Code. Knowledge Fusion was used in NX to make models of the chair and Olingvo and Apache Jena Fuseki was used to communicate with the server containing the parameters, set by both the customer and the product engineer. 

To run the code you will need to hace a running Fuseki-Server and an correct Owl-file (in the Owl-folder) uploaded to the server. You also need tho change the paths in the code, to match the paths on yor own computer. 


### Code Description 

- `DFAserver.py` - Setting ut the web-page that the customer uses to place an order
- `manufChecker.py` - Setting ut the web-page that the engineer uses to define the constraints. 

### OWLs
- `chair.owl` - File made in Olingvo and uploaded to Fuseki, making the model of the chair availavble, reachable from the web-pages, on the server

### DAFs
- `My_Chair_template.daf` - Containing the NX file of the chair template, this is used as the template which every oderer modify to the customers whishes
- `My_Chair_Order.daf` - Containing the NX file whith the parameters given by the customer


### Examples of 3 product orders 

### Product Engeneer Setting Constraints
![Ex1%20-%20setParams.PNG](https://github.com/amaliebholm/TMM4275-KBE-project/blob/main/Images/Ex1%20-%20setParams.PNG)

#### Example 1 
