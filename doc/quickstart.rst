Quickstart
==========

Literals provides a mechanism for declaring sets of literal values, that can be bound to multiple possible versions/value sets. Each such set is called a *binding*.

The Literals Superset
---------------------

Let's say we build an API to a car factory robot. We need to communicate to it the type, color and model of cars it should build. The API for this robot is likely to be versioned, so future versions of the same robot would use different values meaning the same thing.

We start by declaring our **root** literal set, which declares the superset of all available values. Also, this forces us to refer to these constants by name, rather than value. 

.. code-block:: python
       
       >>> from literals import Literals
       >>> robot_literals = Literals({
       ...     'car.color.red': 'RED',
       ...     'car.color.blue': 'BLUE',
       ...     'car.type.sedan': 'CARTYPE_SEDAN',
       ...     'car.type.station': 'CARTYPE_STATION',
       ...     'car.model.v1': 1,
       ...     'car.model.v2': 2,
       ...     })

You'll notice that besides for the names of the various constants, we also provide default values. This is not obligatory, as we might just use `NOTHING` in case we don't want to provide a default::

       
       from literals import NOTHING
       ...
            'car.type.sedan': NOTHING,

Adding Bindings
---------------

After declaring the superset of all possible values (or to be exact - the value names), we create *bindings*, which is our way of saying "the literal set which is bound to a specific use case or version of our subject. Let's say we ship a new version of the robot, and we would like to update its API values to reflect the current ones:

.. code-block:: python
       
       >>> with robot_literals.new_binding(lambda robot: robot.is_v2()) as binding:
       ...     binding.set('car.model.v1', 'VERSION1')
       ...     binding.set('car.model.v2', 'VERSION2')

In the code above we actually performed an *override* of the previous literal value, implying that all the other values remained the same across versions.

Binding Enforcement
-------------------

One of the advantages we get is that we cannot accidentally add values to new versions which were not in previous versions:

.. code-block:: python
       
       >>> with robot_literals.new_binding(lambda robot: robot.is_v2()) as binding:
       ...     binding.set('car.model.v3', 3) # +doctest: IGNORE_EXCEPTION_DETAIL
       Traceback (innermost call last)
          ...
       UnknownLiteralDefinition: Attempted to define a new literal 'car.model.v3' which does not exist in the literal superset


Using Bindings
--------------

After we create bindings we can use them by actually performing a bind. This looks up the appropriate binding needed and returns it:

.. code-block:: python
       
       >>> robot = Robot(version=2)
       >>> robot.literals = robot_literals.bind(robot)
       >>> print(robot.literals.values.car.model.v2)
       VERSION2
       >>> print(robot.literals.values.car.color.red)
       RED

Using Values
------------

Another useful feature is that we can compare literals, even if their resolved values are not equal in our particular case, for instance:

.. code-block:: python
       
       >>> robot.literals.values.car.model.v2 == robot_literals.values.car.model.v2
       True

You can also compare to the specific value in question, but not to another:

.. code-block:: python
       
       >>> robot.literals.values.car.model.v2 == 'VERSION2'
       True
       >>> robot.literals.values.car.model.v2 == 2
       False

