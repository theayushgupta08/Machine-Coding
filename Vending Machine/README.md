# State Design Pattern

## Intent
State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

---

## Problem
The State pattern is closely related to the concept of a **Finite-State Machine**.

### Finite-State Machine
At any given moment, there’s a finite number of states a program can be in. Within any unique state, the program behaves differently, and it can switch from one state to another instantaneously. However, depending on the current state, the program may or may not switch to certain other states. These switching rules, called **transitions**, are finite and predetermined.

### Example
Imagine a `Document` class with three states: **Draft**, **Moderation**, and **Published**. The `publish` method behaves differently in each state:

- **Draft**: Moves the document to moderation.
- **Moderation**: Makes the document public, but only if the current user is an administrator.
- **Published**: Does nothing.

#### Code Example
```java
class Document {
    private String state;

    public void publish() {
        switch (state) {
            case "draft":
                state = "moderation";
                break;
            case "moderation":
                if (currentUser.role.equals("admin")) {
                    state = "published";
                }
                break;
            case "published":
                // Do nothing.
                break;
        }
    }
}
```

The biggest weakness of a state machine based on conditionals reveals itself once we start adding more and more states and state-dependent behaviors to the Document class. Most methods will contain monstrous conditionals that pick the proper behavior of a method according to the current state. Code like this is very difficult to maintain because any change to the transition logic may require changing state conditionals in every method.

The problem tends to get bigger as a project evolves. It’s quite difficult to predict all possible states and transitions at the design stage. Hence, a lean state machine built with a limited set of conditionals can grow into a bloated mess over time.

## Solution
The State pattern suggests that you create new classes for all possible states of an object and extract all state-specific behaviors into these classes.

Instead of implementing all behaviors on its own, the original object, called context, stores a reference to one of the state objects that represents its current state, and delegates all the state-related work to that object.

Document delegates the work to a state object
Document delegates the work to a state object.

To transition the context into another state, replace the active state object with another object that represents that new state. This is possible only if all state classes follow the same interface and the context itself works with these objects through that interface.

This structure may look similar to the Strategy pattern, but there’s one key difference. In the State pattern, the particular states may be aware of each other and initiate transitions from one state to another, whereas strategies almost never know about each other.

## Real-World Analogy
The buttons and switches in your smartphone behave differently depending on the current state of the device:

- When the phone is unlocked, pressing buttons leads to executing various functions.
- When the phone is locked, pressing any button leads to the unlock screen.
- When the phone’s charge is low, pressing any button shows the charging screen.

## Structure
1. Context stores a reference to one of the concrete state objects and delegates to it all state-specific work. The context communicates with the state object via the state interface. The context exposes a setter for passing it a new state object.

2. The State interface declares the state-specific methods. These methods should make sense for all concrete states because you don’t want some of your states to have useless methods that will never be called.

3. Concrete States provide their own implementations for the state-specific methods. To avoid duplication of similar code across multiple states, you may provide intermediate abstract classes that encapsulate some common behavior.

State objects may store a backreference to the context object. Through this reference, the state can fetch any required info from the context object, as well as initiate state transitions.

4. Both context and concrete states can set the next state of the context and perform the actual state transition by replacing the state object linked to the context.


## Applicability
1. Use the State pattern when you have an object that behaves differently depending on its current state, the number of states is enormous, and the state-specific code changes frequently.

2. The pattern suggests that you extract all state-specific code into a set of distinct classes. As a result, you can add new states or change existing ones independently of each other, reducing the maintenance cost.

3. Use the pattern when you have a class polluted with massive conditionals that alter how the class behaves according to the current values of the class’s fields.

4. The State pattern lets you extract branches of these conditionals into methods of corresponding state classes. While doing so, you can also clean temporary fields and helper methods involved in state-specific code out of your main class.

5. Use State when you have a lot of duplicate code across similar states and transitions of a condition-based state machine.

6. The State pattern lets you compose hierarchies of state classes and reduce duplication by extracting common code into abstract base classes.


## Pros and Cons
### Pros
- Single Responsibility Principle. Organize the code related to particular states into separate classes.
- Open/Closed Principle. Introduce new states without changing existing state classes or the context.
- Simplify the code of the context by eliminating bulky state machine conditionals.
### Cons
- Applying the pattern can be overkill if a state machine has only a few states or rarely changes.
 