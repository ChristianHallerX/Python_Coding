"""
Quiz Questions

1. What should the <FUNCTION> below be called to set up a new object?

class Student
    def (self, name):
        self.name = name


- __init__
- __init
- __construct__
- __main__

Answer: __init__


2. What is the 'abc' module used for?

- It provides functionalities for abstract classes.
- It provided common word parsing functions.
- It provides functionalities for alphabet and string manipulation.

Answer: "It provides functionalities for abstract classes."


3. What does the expression 'range(5, 15, 3)' in Python generate?

- A sequence of numbers starting from 3 to 15, incremented by 5 each time (3, 8, 13, 18).
- A sequence of numbers starting from 5 to 15, incremented by 3 each time (5, 8, 11, 14, 17).
- A sequence of numbers starting from 5 to 14, incremented by 3 each time (5, 8, 11, 14).
- A sequence of numbers starting from 3 to 14, incremented by 5 each time (3, 8, 13).

Answer: A sequence of numbers starting from 5 to 14, incremented by 3 each time (5, 8, 11, 14).


4. What is the purpose of 'torch.nn.Module' in PyTorch?

- It is a class for storing dataset information
- It is a class for handling all sorts of matrix operations
- It is a base class for all neural network modules
- It is a class for handling t ensor operations

Answer: "It is a base class for all neural network modules."


5.  Describe the memory management mechanism used by Python, including its primary features and how it differs from
traditional memory management in languages like C or C++.

- Python relies on a stack-based memory management system, similar to how memory is managed in languages like C or C++.
This system allocates memory in a linear fashion and releases it in a last-in, first-out (LIFO) order.

- Python uses a private heap to manage memory, which is a data structure that keeps track of all the objects and data
in a Python program. Unlike languages like C or C++, Python's memory management is automatic and handles tasks such as
allocation and deallocation of memory dynamically. It employs a technique called "garbage collection" to automatically
reclaim memory occupied by objects that are no longer in use. Additionally, Python employs reference counting to keep
track of the number of references to an object, and objects with zero references are automatically deallocated.
This approach simplifies memory management for developers but may lead to overhead and occasional performance
implications compared to manual memory management in languages like C or C++.

- In Python, memory management is handled by the operating system, which allocates memory blocks as needed and
releases them when they are no longer in use. This approach is more efficient than manual memory management but lacks
the flexibility and control provided by languages like C or C++.

- Python uses manual memory management, where developers must explicitly allocate and deallocate memory for objects.
This approach provides more control and efficiency compared to automatic memory management used in languages like
Java or C#.

Answer: 2


6. In PyTorch, how can you move all parameters and buffers of a model to a GPU?

- By using the .gpu() method of a model
- By using the torch.cuda.move() function
- By using the .cuda() or .to(device) method of the model
- By passing the model to the torch.cuda.Tensor() function

Answer: "By using the .cuda() or .to(device) method of the model."


7. Which metric is used to evaluate the performance of a regression model in scikit-learn?

- F1-Score
- Accuracy
- Mean Squared Error (MSE)
- Area Under Curve (AUC)

Answer: "Mean Squared Error (MSE)."


8. What is the effect of calling .zero_grad() on an optimizer in PyTorch?

- It resets the internal state of the optimizer
- It initializes the gradients of all optimized parameters
- It resets the learning rate of the optimizer to zero
- It sets the gradients of all optimized parameters to zero

Answer: "It sets the gradients of all optimized parameters to zero."


9. Explain the concept of inheritance in Python, including its purpose, how it is implemented, and how it differs
from composition.

- Inheritance in Python allows a class to inherit attributes and methods from another class, but it is
implemented differently from other languages like Java or C++. In Python, inheritance is more dynamic and allows for
multiple inheritance, where a subclass can inherit from multiple base classes. This differs from composition, where
objects are composed of other objects and relationships between classes are more flexible.

- Inheritance in Python allows a class to define its own attributes and methods independently of other classes,
providing encapsulation and modularity. It is implemented by creating a new class and specifying the base class using
the "extends" keyword. Inheritance differs from composition, where objects are composed of other objects, allowing for
more flexibility and reusability.

- Inheritance in Python allows a class to inherit attributes and methods from another class, enabling code reuse and
the creation of hierarchies. It is implemented by defining a new class that extends an existing class using the syntax
class NewClass(BaseClass). Subclasses inherit all attributes and methods from the base class and can override or
extend them as needed. Inheritance differs from composition, where objects are composed of other objects rather than
inheriting behavior. In composition, the relationship between classes is typically looser, and objects can be composed
of multiple components, whereas inheritance implies an "is-a" relationship between classes.

- Inheritance in Python is the process of creating multiple classes from a single base class, enabling code reuse and
polymorphism. It is implemented by creating a new class and using the inherits keyword to specify the base class.
Inheritance differs from composition, which involves creating complex objects by combining simpler objects.

Answer: 3


10. What is Docker primarily used for?

- Creating, deploying, and running applications in containers
- Cloud storage
- Managing virtual machines
- Automating the deployment of applications

Answer: "Creating, deploying, and running applications in containers."


11. What line is missing from this Dockerfile that allows us to install Python modules?
----------------------------
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
***
COPY . /code/
-----------------------------

- RUN pip install -r requirements.txt
- INSTALL pip install -r requirements.txt
- Python RUN pip install -r -requirements.txt
- DOCKER-RUN pip install -r requirements.txt

Answer: "RUN pip install -r requirements.txt"


12. What command is used to create a Docker image?

- docker make
- docker build
- docker create
- docker compile

Answer: "docker build"


13. In Docker, what command is used to list all running containers?

- docker containers
- docker running
- docker ps
- docker list

Answer: "docker ps"


14. What is the Docker command to stop a running container?

- docker kill [container_id]
- docker halt [container_id]
- docker pause [container_id]
- docker stop [container_id]

Answer: "docker stop [container_id]"


15. What is the command to view logs of a Docker container?

- docker trace [container_id]
- docker logs [container_id]
- docker view [container_id]
- docker monitor [container_id]

Answer: "docker logs [container_id]"




"""
