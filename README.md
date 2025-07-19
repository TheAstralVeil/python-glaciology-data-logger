# Glaciology Data Logger (Python CLI)

A command-line application for logging and analyzing geological samples, demonstrating fundamental Python concepts. This project was developed as a hands-on exercise to solidify core programming principles through a practical, domain-specific tool.

## Features

* **Add New Samples:** Input details for various geological samples (e.g., ice cores, rock samples), including ID, location, type, depth, and the presence of volcanic ash.
* **View All Samples:** Displays all logged samples with their detailed attributes.
* **Search by ID:** Quickly finds and displays a specific sample using its unique ID.
* **Run Basic Analysis:** Generates a summary report including total samples, average sample depth, and a list of samples containing volcanic ash.

## Concepts Demonstrated

This application showcases the practical application of the following fundamental Python concepts:

* **Variables, Lists, and Dictionaries:** Used for structured data storage and manipulation.
* **Loops:** `for` and `while` loops for iteration and input validation.
* **Conditionals (`if/elif/else`):** For menu navigation, logic branching, and data integrity checks.
* **Functions:** Modularizing code into reusable blocks for better organization and readability.
* **User Input and Output:** Handling command-line interactions.

## How to Run

1.  **Prerequisites:**
    * Python 3.x (Ensure you have a recent version of Python installed on your system).

2.  **Clone the repository:**
    ```bash
    git clone [https://github.com/TheAstralVeil/python-glaciology-data-logger.git](https://github.com/TheAstralVeil/python-glaciology-data-logger.git)
    cd python-glaciology-data-logger
    ```

3.  **Execute the script:**
    ```bash
    python GlacioDataLogger.py
    ```

## Future Enhancements

* Implement data persistence (e.g., saving data to a CSV or JSON file).
* Add more advanced search and filtering options.
* Expand analysis capabilities (e.g., deepest sample, samples by type).
* Introduce error handling for file operations.
