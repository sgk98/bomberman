# bomberman
SSAD Assignment1
Roll Number 20161221

File Structure:
    models.py->Has all the classes defined in it.
    inp.py -> Has functions for the asynchronous input defined 
    board.py -> Gameplay and utility functions defined there.

Usage:
python board.py
Enter 1/2/3 for level(Easy/Medium/Hard)
And the enjoy!!


Class definitions:
Person

Bomberman,Enemy inherit from it.

Cell
It is the basic building block of the board.

Bomb,Brick
classes for bomb and brick respectively.

The Board is visualized as a 19x19 cells.
Each cell is either empty or has an entity occupying it.
For printing the board as 76x38 board onto the terminal,you just apply a transformation on the 19x19 board.

Uses Of Inheritcance:
Person is the base class.
Bomberman and enemy inherit from it.

Modularity:
The project is split into 3 files with the possibility of splitting it further if needed
(models can be broken down into individual classes,and the board.py can also be broken down)

Polymorphism:
There is a function which checks the possible squares that a certain entity can go to.
Bomberman cannot go into a cell where there is an enemy or wall or brick.
Enemy has pretty much the same constrains, but it can go to a cell where the bomberman is.
The bomb can go anywhere except where the bomb is.
The function is the same, but it behaves differently for different entities.
This is an example of polymorphism.

Encapsulation:
The use of classes automatically implements encapsulation as it treats data and functions as a single unit.

Bonus Features Implemented:
1)3 Levels(Easy/Medium/Hard)
2)Ticking of the bomb

