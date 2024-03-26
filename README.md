# SPAC7

## Assignment
The goal of this project was to simulate a warehouse, which uses a MySQL database.
It was suggested to use the classes Category, Product and Transaction as basis.

## Workflow

Being new to MySQL, the initial focus was getting a working prototype in OOP of the warehouse.
The goal was to work out the kinks on how stuff should interact, before venturing into unknown territory.
This initial phase included setting up the data classes and implementing tests to ensure things worked as expected.
A decent focus was put on not only exploring 'happy paths', but also expected user errors when handling inputs.

Once work on the MySQL database began, it was clear that I hadn't considered how versatile it was for searching data.
As such, the warehouse class quickly ended up becoming an annoying middle layer until its proper function was realized.

A large portion of the work was centered around implementing various search functions, and how best to do so using only the user terminal.
Several search functions are therefor questionable, either because they get the user too much freedom or because they are too combersome.

During the project time was set aside to showcase the program for others. A user friendly UI, in the user terminal, was therefor made a priority.

The final version of the project is capable of generating a database for the user and letting them search and edit items in the database. All data type values are guarded, ensuring that the user can't make any invalid changes.

Extra functionality, such as adding and deleting items to the database, was in the works, but no good solution, on how to handle the interconnected id values, was found in time.
The finanal solution does share tell tale signs of being rushed, as the WarehouseMySQL and SQLHandler classes both have far too many methods to be SOLID compliant.

## Design

- The program uses an SQLHandler to send and recieve data between python and the MySQL database. This class makes use of helper classes to build the queries.

- The WarehouseMySQL functions as an extra layer between the user and the database, with methods tailored to a more general user. A large part is therefor dedicated to exploring how best to handle the search functions.

- The FakeWarehouseFiller is a factory for all the faker modules, making it easy to fill the database with valid randomized data.

- The UserActionFactory loads all classes, which inherits from AbsUserAction, and builds a list of them whenever requested.

- The UserInteraction is a simple state machine, using UserInteractionData as a means to remember its state.

- The UserAction's each have a function which checks if they are usable or not, allowing for new functions to be added quickly. The drawback of this disconnected setup is that the flow can be difficult to visualize and debug.

- The UserChoiceSelector is a simble class dedicated to recieving an item list, handling the user input and returning the index of the requested item.

## Installation
1. Clone the repo
2. Install requirements in 'requirements.txt'
3. Run 'main.py'
