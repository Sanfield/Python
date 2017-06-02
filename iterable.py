Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> a=list()
>>> a
[]
>>> b='i love fishc,com'
>>> b
'i love fishc,com'
>>> b=list(b)
>>> b
['i', ' ', 'l', 'o', 'v', 'e', ' ', 'f', 'i', 's', 'h', 'c', ',', 'c', 'o', 'm']
>>> c=(1,1,3,5,8,13,21)
>>> c=list(c)
>>> c
[1, 1, 3, 5, 8, 13, 21]
>>> max(c)
21
>>> max(b)
'v'
>>> min(c)
1
>>> min(b)
' '
>>> tuple1=(1,2,3,45,6,8,9)
>>> max(tuple1)
45
>>> xum(tuple1)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    xum(tuple1)
NameError: name 'xum' is not defined
>>> sum(tuple1)
74
>>> sorted(tuple1)
[1, 2, 3, 6, 8, 9, 45]
>>> list(enumberate(tuple1))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    list(enumberate(tuple1))
NameError: name 'enumberate' is not defined
>>> list(enumerate(tuple1))
[(0, 1), (1, 2), (2, 3), (3, 45), (4, 6), (5, 8), (6, 9)]
>>> list(zip(a,b))
[]
>>> list(zip(a,b))
[]
>>> reversed(tuple1)
<reversed object at 0x0000027F379E5FD0>
>>> a=[1,2,5,6,8,7,8]
>>> b=[5,8,1,9,7,8]
>>> list(zip(a,b))
[(1, 5), (2, 8), (5, 1), (6, 9), (8, 7), (7, 8)]
>>> zip(a,b)
<zip object at 0x0000027F37934648>
>>> 
