#!/usr/bin/env python3

from person import Person

class TestPerson:
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person"'''
        guido = Person("Guido")
        assert type(guido) == Person

class TestInit:
    '''Person.__init__ in person.py'''

    def test_saves_self_name(self):
        '''takes a name as an argument and saves it to self.name'''
        guido = Person("Guido")
        assert guido.name == "Guido"

    def test_person_name_attribute(self):
        '''Person instance has a name attribute set correctly'''
        alice = Person("Alice")
        assert hasattr(alice, "name")
        assert alice.name == "Alice"

    def test_person_name_is_unique(self):
        '''Each Person instance has its own name'''
        bob = Person("Bob")
        carol = Person("Carol")
        assert bob.name == "Bob"
        assert carol.name == "Carol"
        assert bob.name != carol.name

    def test_person_name_type(self):
        '''Person name attribute is a string'''
        dave = Person("Dave")
        assert isinstance(dave.name, str)