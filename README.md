# One-to-many Object Relationships Lab

## Learning Goals

- Create one-to-many relationships.

***

## Key Vocab

- **Class**: a bundle of data and functionality. Can be copied and modified to
accomplish a wide variety of programming tasks.
- **Object**: the more common name for an instance. The two can usually be used
interchangeably.
- **Object-Oriented Programming**: programming that is oriented around data
(made mobile and changeable in **objects**) rather than functionality. Python
is an object-oriented programming language.
- **Function**: a series of steps that create, transform, and move data.
- **Method**: a function that is defined inside of a class.

***

## Introduction

In this lab we will implement a one-to-many relationship between a `Owner` and `Pet`.

***

## Instructions

This is a **test-driven lab**. Run `pipenv install` to create your virtual
environment and `pipenv shell` to enter the virtual environment. Then run
`pytest -x` to run your tests. Use these instructions and `pytest`'s error
messages to complete your work in the `lib/` folder.

Instructions:

- Define a `Pet` and pass into the constructor a `name` and a `pet_type`.
- Define an `Owner` class and pass into the constructor a `name`.
- In the `Owner` class write a method called `add_pet(self, pet)` that adds pets to a `pets` list for the owner.
- In the `Owner` class write a method called `remove_pet(self, pet_name)`
that takes a pets name and removes the pet from the `Owners` `pets` list.
- In the `Owner` class write a method called `sort_pets_by_name(self)` returns a sorted list of pet names.

***

## Resources

- [Python classes](https://docs.python.org/3/tutorial/classes.html)