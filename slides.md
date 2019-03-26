%title: 00P - The Power of Metaclasses
%author: Jakub Tesárek
%date: 2019-03-23

# 00P - The Power of Metaclasses

---
# Everything is an object

```
>>> isinstance(True, bool)
True
```

```python
>>> dir(True)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__' ...]
```

```python
>>> True.__abs__()
1
```

```python
>>> bool() # Call constructor of bool without argument
False
```

---

# Every object has its type
use `type()` to get a class of an object

*Object:*            \<class>
*Scalars:*           int | str | bool ...
*Structures:*        list | dict | set ...
*None:*              NoneType
*Function:*          function
*Build-in function*: builtin\_function\_or\_method
*Module:*            module
*Classes:*           type

---

# Metaclass - Class of a class
**Any class whose instances are themselves classes, is a metaclass.**
**Class is an instance of its metaclass.**

---

# Type
`type` is a super-level metaclass. Everything is a type.

## With one arguments it returns class of that arguments
```python
>>> type(42)
<class 'int'>
```

## With 3 arguments it generates new class
```python
>>> type('Foo', (), {})
<class '__main__.Foo'>
```

---
Quiz. What's the output of this command?
`>>> type(type)`
^
`<class 'type'>`

---

# Construction of class instance
1. Python sees `class` definition
2. Determine metaclass - argument `metaclass` or `type`
3. Python calls `metaclass(name, bases, attributes)`

---

```python
class Greeter(Parent, metaclass=type):
    def greet(self):
        print 'hello'
```
^
is actually:
```python
Greeter = type('Greeter', (Parent,), {'greet': <function 0x108b20510>})
```
^
is actually:
```python
Klass = type.__new__(type, 'Klass', {'greet': <function 0x108b20510>})
type.__init__(Klass, 'Klass', (Parent,), {'greet': <function 0x108b20510>})
```
---

