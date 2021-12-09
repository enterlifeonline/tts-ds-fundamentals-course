## Real World Examples

In early 2016, Python passed Java as the #1 beginners language in the world. Why? It's because it's simple enough for beginners yet advanced enough for the pros.

- **[SpaceX](https://github.com/r-spacex?language=python)** uses it to launch rockets.

- **[Pixar](https://graphics.pixar.com/)** uses Python to run their animation software.

- **[Instagram](https://instagram-engineering.com/tagged/python)** & **[Pinterest](https://pypi.org/project/pinterest-client/)** use it to run their web application (backend via **[Django](https://www.djangoproject.com/))**.
- - - 

### Data Structures

#### Lists, Sets, Dictionaries, Tuples

**Lists** are what they seem - a list of values. Each one of them is numbered, starting from zero - the first one is numbered zero, the second 1, the third 2, etc. 

You can remove values from the list, and add new values to the end. Example: ***Your many cats' names***.

```
# lists
# natural language processing

text = "It always takes longer than you expect, even when you take into account Hofstadter's Law."

tokens = text.split() 

for i in range(0,15):
   print(tokens[i])

```

<hr>

**Tuples** are just like lists, but you can't change their values. 

The values that you give it first up, are the values that you are stuck with for the rest of the program. Again, each value is numbered starting from ***zero***, for easy reference. 

Example: ***Store the latitude and longitude of your home, because a tuple always has a predefined number of elements (in this specific example, two). The same Tuple type can be used to store the coordinates of other locations.***


```
# tuples
# coordinates

self.coords[0] += self.velocity * dt * math.cos(self.rot) # sx = v * dt * cos()
self.coords[1] += self.velocity * dt * math.sin(self.rot) # sy = v * dt * sin()
```

<hr>

**Sets** are basically collection of certain items that are unordered. There is no specific order in which they are stored. In Python sets are same, but there are few differences with basic sets.

- The elements in python sets are unique, there can’t be duplicate items in python sets. If duplicate items entered, it will be ignored and final set will always contain unique elements.

- Python sets are mutable. But, its elements are immutable. Once entered items cannot be modified.

- Python set’s item cannot be accessed using indexes. There is no index attached to set items.

Example: ***Sets are more or less formal descriptions of what is included and what is not included. Thus, I think we do this daily when communicating with other people about various ideas, actions, objects. “Hey, I found this cool playlist on Spotify! Here are the songs: Heaven is a Place on Earth, What’s Up, What I Need, Same Love, Born This Way, Firework, We Can’t Stop.”***

```

{a character in the novel Noli Me Tangere} intersection {a character in the novel El Filibusterismo}

{a national hero of the Philippines} intersection {historical figures in the Philippines}

{a caffeinated drink} intersection {a carbonated drink}

{a country of Southeast Asia} intersection {a country of Asia}

{a Greek mythology goddess} intersection {an offspring of Zeus}

```

<hr>

**Dictionaries** are similar to what their name suggests - a dictionary. 

In a dictionary, you have an 'index' of words, and for each of them a definition. In python, the word is called a 'key', and the definition a 'value'. 

The values in a dictionary aren't numbered - tare similar to what their name suggests - a dictionary. 

In a dictionary, you have an 'index' of words, and for each of them a definition. In python, the word is called a 'key', and the definition a 'value'. 

The values in a dictionary aren't numbered - they aren't in any specific order, either - the key does the same thing. You can add, remove, and modify the values in dictionaries. Example: ***telephone book***.

```
# password example
# nested dictionaries
    
password_index = 

    {
    
    'Account 1' : {'Username': 'mrbooleanswag', 'Password': 'askjdkljfgsdfg'},

    'Account 2' : {'Username': 'Lexington', 'Password': 'kfsdjgfdg'},

    }
    
```


