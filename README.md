# Advanced Python Calculator
## Project Overview

This project necessitated creating a sophisticated calculator application using Python. The goal was to emphasize the significance of adhering to professional software development standards. The application incorporates several key elements including well-organized and sustainable code, utilization of design patterns, thorough logging, adaptability through environment variables, advanced data management using Pandas, and a command-line interface (REPL) for seamless interaction with users in real-time.

## Core Functionalities

### Command-Line Interface (REPL)

A Read-Eval-Print Loop (REPL) was introduced to enable direct interaction with the calculator. This interface allowed users to manage calculation history and perform basic arithmetic operations including addition, subtraction, multiplication, and division. Furthermore, it granted access to additional features via dynamically loaded plugins.

### Plugin System

A versatile plugin framework was developed to facilitate effortless integration of new commands or functionalities. This framework dynamically loads and incorporates plugins into the application without requiring alterations to the core code. Moreover, it incorporates a persistent "Menu" feature to display all available plugin commands, ensuring users can easily discover and interact with them.

### Calculation History Management with Pandas

The Calculator sUtilize Pandas to manage a robust calculation history, enabling users to Load, save, clear, and delete history records through the REPL interface.

### Professional Logging Practices

A thorough logging infrastructure was set up to meticulously document various aspects of the application, including detailed operations, data manipulations, errors, and informational messages. Log messages are categorized by severity, distinguishing between INFO and ERROR levels for efficient monitoring. Additionally, the logging configuration can be dynamically adjusted through environment variables to specify logging levels and output destinations as per requirements.

### Advanced Data Handling with Pandas

It utilizes Pandas for efficient handling of data, particularly in reading and writing to CSV files, along with managing calculation history.

### Design Patterns for Scalable Architecture

The calculator integrates various design patterns to tackle software design challenges effectively. For instance, it employs the **Facade Pattern** to provide a simplified interface for intricate Pandas data manipulations. Additionally, it structures commands within the REPL using the **Command Pattern** to facilitate efficient calculation and history management. Furthermore, the application's code structure, flexibility, and scalability are enhanced through the utilization of **Factory Method, Singleton, and Strategy Patterns**.

### Link to description and Demonstration.
Link: 
