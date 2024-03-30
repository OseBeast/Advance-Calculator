# Advanced Python Calculator
## Project Overview

This project necessitated creating a sophisticated calculator application using Python. The goal was to emphasize the significance of adhering to professional software development standards. The application incorporates several key elements including well-organized and sustainable code, utilization of design patterns, thorough logging, adaptability through environment variables, advanced data management using Pandas, and a command-line interface (REPL) for seamless interaction with users in real-time.

## Project Analysis

### Set up Instructions
1. Open up User Terminal
2. Run "python main.py"
3. Choose Operation or Command from Menu (add, subtract, multiply, divide, load, save, delete, clear, exit)
4. When ready to terminate app type "exit"
5. Run play pytest --pylint to varify proper operation.

### Usage example

Type the command to select the following:
                add: Adds two numbers
                subtract: Subtracts two numbers
                multiply: Multiplies two numbers
                divide: Divides two numbers
                load: Load history from a csv file which will add to the current history
                save: Save the current history
                delete: Deletes the history
                clear: Clears the history from display 
                exit: Exits out of the program   
        
Empty DataFrame
Columns: [value1, symbol, value2, result]
Index: []
>>> add
2024-03-29 23:22:57,555 - root - INFO - User Selected Add.
Enter value one:3
2024-03-29 23:23:02,849 - root - INFO - User entered the number: 3
Enter value two:5
2024-03-29 23:23:03,833 - root - INFO - User entered the number: 5
2024-03-29 23:23:03,834 - root - INFO - User Answer: 8
Type the command to select the following:
                add: Adds two numbers
                subtract: Subtracts two numbers
                multiply: Multiplies two numbers
                divide: Divides two numbers
                load: Load history from a csv file which will add to the current history
                save: Save the current history
                delete: Deletes the history
                clear: Clears the history from display 
                exit: Exits out of the program   
        
   value1 symbol  value2  result
0       3      +       5       8
>>> 

### Analysis of Architectural Decisions

A **Read-Eval-Print Loop (REPL)** was introduced to enable direct interaction with the calculator. This interface allowed users to manage calculation history and perform basic arithmetic operations including addition, subtraction, multiplication, and division. Furthermore, it granted access to additional features via dynamically loaded plugins.

The versatile **plugin framework** was developed to facilitate effortless integration of new commands or functionalities. This framework dynamically loads and incorporates plugins into the application without requiring alterations to the core code. Moreover, it incorporates a persistent "Menu" feature to display all available plugin commands regardless of application state to ensuring users can easily discover and interact with them.

The calculator utilizes **Pandas** to manage a robust calculation history, enabling users to load, save, clear, and delete history records through the REPL interface. As well as for efficient handling of data, particularly in reading and writing to *CSV files*, along with managing calculation history.

A thorough **Logging Infrastructure** was set up to meticulously document various aspects of the application, including detailed operations, data manipulations, errors, and informational messages. Log messages are categorized by severity, distinguishing between *INFO* and *ERROR* levels for efficient monitoring. Additionally, the logging configuration can be dynamically adjusted through **Environment Variables** to specify logging levels and output destinations as per requirements.

The calculator integrates various design patterns to tackle software design challenges effectively. It employs the **Facade Pattern** to provide a simplified interface for intricate Pandas data manipulations. Additionally, it structures commands within the REPL using the **Command Pattern** to facilitate efficient calculation and history management. Furthermore, the application's code structure, flexibility, and scalability are enhanced through the utilization of **Factory Method, Singleton, and Strategy Patterns**.

### Link to description and Demonstration.
**Link:**  https://youtu.be/An1s6Mxd6yk 
