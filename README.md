# Monotonic Function Checker

This repository includes a Python program designed to evaluate Boolean functions across various scenarios to determine if they are monotonic. A monotonic function maintains a consistent order between its inputs and outputs, ensuring that if one input is less than or equal to another, the corresponding output must also be less than or equal to the other.

The repository also contains a PDF explanation in Hebrew.

## Code Description

### Defining Unique Scenarios
The code defines scenarios based on combinations of two activators and two inhibitors, each of which can be either on (1) or off (0). These scenarios represent the influence on a central gene, reducing the total number of scenarios from 16 to 9 by focusing on significant variations.

### Functions for Checking Monotonicity

- **`check_monotonicity(func)`**: This function checks whether a given Boolean function is monotonic. It uses helper functions to compare scenarios and determine if the function maintains monotonicity.

- **`scenarios_comparable(s1, s2)`**: This helper function determines whether one scenario is less than or equal to another by comparing the influence of activators and inhibitors on the central gene.

### Generating Functions
The code uses the `itertools` library to generate all possible Boolean functions for the defined scenarios. It then filters out non-monotonic functions, leaving only those that satisfy the monotonicity criteria.

### Outputting Results and Graphical Display

- **Console Output**: The code utilizes the `pandas` and `tabulate` libraries to display the monotonic functions in a clear, tabular format in the console. The `termcolor` library is used to color the text for better visibility.

- **Graphical Interface**: The `tkinter` library is used to create a graphical interface, presenting the monotonic functions in an interactive table.

## Features

- **Generate Functions**: Automatically generates all possible Boolean functions for the given scenarios.
- **Check Monotonicity**: Filters and identifies monotonic functions based on the defined constraints.
- **Visual Representation**: Displays the monotonic functions in a visually appealing table format in both the console and a Tkinter GUI.

## Dependencies

Before running this script, ensure that the following Python libraries are installed:

- `tkinter` for the graphical user interface (GUI).
- `itertools` for generating combinations of Boolean functions.
- `pandas` for managing and displaying data efficiently.
- `tabulate` and `termcolor` for enhanced console output.

You can install the necessary libraries using pip:

```bash
pip install pandas tabulate termcolor

## How to Run
bash
1. Ensure that all dependencies are installed as described above.
2. Download or clone the repository to your local machine.
3. Navigate to the directory containing the script in your terminal.
4. Execute the Python script using the following command:

   python BiologicalComputation_FinalProject.py
