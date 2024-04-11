# CMSC 355 Project - Warehouse Database

## Description
This is a warehouse storage program that lets a user search through a data base to find a specific item. We are currently working on the project and have plans on adding more user cases. So far we implemented the search and add use cases. In the subsections below we go into more detail about what we worked on and the requirements for each sprint. The Gui is still in development so some information will still show up in the terminal.

### Testing
- Test 1: This test will use the add use case to check the procedure of adding an item to the warehouse.
- Test 2: This test will use the search use case to check the procedure of looking for an item in the warehouse.

## Getting Started

### Dependencies
- Python Installed
- Tkinter Python Library

### Installing
- Check to make sure python is installed
- Download imported libraries if not already installed

### Executing Program
 - Run ```python gui.py``` to run the gui version of the program
 - Run ```python search.py``` to run the individual test cases for the search function without the gui.
 - Run ```python Add.py ``` to run the individual test cases for the add function without the gui.
 - Run ```python Test.py ``` to run the test case for the 2 functions without the gui.
 


# Workflow/Sprint Schedule (Requirements)
## Sprint 1 (due 4/2)

### Overview
The location class has an array that holds type items. The user than creates an item with a name, unique id, quantity and weight. When the user add the items it gets added to predefined location. The user can add multiple items into the location. The user then types in the name and the id to search by and it will search the warehosue data base. The information will be printed at the terminal and some at the gui.

### Summary
The first sprint had us meet as a team to create a program and think about the different use cases we needed to implement. We were required to create 2 use cases as well as test cases to show that they work. We were required to hold team meetings to discuss how we wanted to split up the work. We decided to use a Gui design to help the program be much easier to use for non technical users. The first goal was to assign everyone different tasks. Some of the scripts had to be slightly modified to be added to the gui. some scripts were directly included in the gui but originated as seperate scripts for testing.

### Problems Faced
We faced a few problems during our first sprint. One of the problems we were facing was learning new libraries to use with python. For example, when creating the gui we needed to do research to figure out a library to do so. This meant we had to find a library and reserach the documentation and try to learn from examples. Another problem was being able to solve bugs that may have came up in someone else's code. This meant we would have to communicate and see what the other person's code was meant to do and why they might have went with that specific method. Another issue was going from the code we created to test each function and implementing them into a gui. Some of the scripts and functions had to be rewritten to work with the gui. Creating and organizing the gui has been dificult. We plan on ironing out all the functionality before making a clean and organized gui. We might dedicate one person to work on getting a better understanding of the library.

## Sprint 1 (due 4/11)
### Overview
The second sprint is building off the first one. We now have to implement 2 new use cases and test cases for those use cases. We also have to create UML diagrams for our classes and major functions. This is a new requirement. We will also have to create use case specification forms for the two new use cases as well. The new use cases we decided as was **delete item** and **print location**. The **delete item** will delete any item based off of its name and unique id. The **print location** will print out all the items stored at a specific location.

### Summary
The second sprint had us meet again to break up some of the tasks and discuss how to move forward. We decided that we need to fix some the bugs and other issues that we had from the first sprint before moving forward. We did more research and found a better way to structure the gui that made it much more visible.

### Problems Faced
The first issue we faced was fixing some of the mistakes that we made in the previous sprint. We spent time making the gui more organized so the user can have an easier time working with it. We also needed to rework some of the data structures in our classes so they work with the next set of use cases we have to implement.

## Authors
[Evan Haaland](https://www.linkedin.com/in/evannhaaland/) </br>
Ishaan Thakur  </br>
[Nathan Germain](https://www.linkedin.com/in/nathan-germain/) </br>
Dylan Kekoa  </br>
Kelechukwu Onyedeke


