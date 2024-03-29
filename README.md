# Advanced Python Calculator for Software Engineering Graduate Course
## Project Overview

This project required the development of an advanced Python-based calculator application. Designed to underscore the importance of professional software development practices, the application integrates clean, maintainable code, the application of design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.

## Core Functionalities

### Command-Line Interface (REPL)

Implement a Read-Eval-Print Loop (REPL) to facilitate direct interaction with the calculator. This interface should support:
- Execution of arithmetic operations (Add, Subtract, Multiply, and Divide)
- Management of calculation history.
- Access to extended functionalities through dynamically loaded plugins.

### Plugin System

Create a flexible plugin system to allow seamless integration of new commands or features. This system should:
- Dynamically load and integrate plugins without modifying the core application code.
- Include a REPL  "Menu" command to list all available plugin commands, ensuring user discoverability and interaction.

### Calculation History Management with Pandas

Utilize Pandas to manage a robust calculation history, enabling users to:
- Load, save, clear, and delete history records through the REPL interface.


### Professional Logging Practices

Establish a comprehensive logging system to record:
- Detailed application operations, data manipulations, errors, and informational messages.
- Differentiate log messages by severity (INFO, WARNING, ERROR) for effective monitoring.
- Dynamic logging configuration through environment variables for levels and output destinations.

### Advanced Data Handling with Pandas

Employ Pandas for:
- Efficient data reading and writing to CSV files.
- Managing calculation history.

### Design Patterns for Scalable Architecture

Incorporate key design patterns to address software design challenges, including:
- **Facade Pattern:** Offer a simplified interface for complex Pandas data manipulations.
- **Command Pattern:** Structure commands within the REPL for effective calculation and history management.
- **Factory Method, Singleton, and Strategy Patterns:** Further enhance the application's code structure, flexibility, and scalability.

## Development, Testing, and Documentation Requirements

### Testing and Code Quality

- Achieve a minimum of 90% test coverage with Pytest.
- Ensure code quality and adherence to PEP 8 standards, verified by Pylint.

### Version Control Best Practices

- Utilize logical commits that clearly group feature development and corresponding tests, evidencing clear development progression.

### Comprehensive Documentation

- Compile detailed documentation in `README.md`, covering setup instructions, usage examples, and an in-depth analysis of architectural decisions, particularly emphasizing the implementation and impact of chosen design patterns and the logging strategy.
