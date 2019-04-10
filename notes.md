# Introduction
1. What are meta-classes, how to create them, example at the end
2. Download the demo
3. Repo contains slides, demo and tests

# Everything is an object
1. Use `dir()` to get list of attributes and methods
2. Even scalar values are objects
3. True.__abs__()
4. Can't do `-1.__abs__()` but can do `a = -1; a.__abs__()`

# Every object has it's type
1. Type is the class it was created from
2. To get type use `type()`
3. Because everything is an object, it will work on everything
4. Classes are objects too, therefore they have their type - a metaclass

# Metaclass
1. Metaclass is a class used to create other classes

# Type
1. Type is actually a class that is used to create other classes
2. We can use other metaclasses but type is metaclass of most other classes
3. Calling `type()` calls constructor of class `type`
4. It always returns a class
5. Two ways to call it
   - With 1 argument
   - With 3 arguments

# Quiz
1. Result is type
2. Everything is an object, therefore `type` is also object
3. `type` is instance of itself

# Construction of class instance



# Demo
- @a: Remove attribute from class
- @s: Create new `set_*` attribute
- @d: Change `set_*` to an actual setter
- @f: Move setter to IntegerAttribute
- @g: Implement getter
- @h: Validate integer
- @j: Default value
- @k: Maximumum value

