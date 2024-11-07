#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python program showing
# abstract base class work

from abc import ABC, abstractmethod


class Animal(ABC):
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


def main():
    # Driver code
    R = Human()
    R.move()

    K = Snake()
    K.move()

    R = Dog()
    R.move()

    K = Lion()
    K.move()


if __name__ == '__main__':
    main()