"""
In this Python program, we will find all the monotonic regulation conditions
from the given table (part d). We will do this steps:
1) Define a function to check monotonicity.
2) Read the table data (in this case, we'll hardcode it in a matrix as it's provided visually).
3) Iterate through the regulation conditions and check each one for monotonicity.
4) Print the regulation conditions that satisfy the monotonic requirement.
"""

########################################################################################
#                            Hadas Hanasab 213486764                                   #
#                            Shoham Galili 208010785                                   #
########################################################################################


import tkinter as tk
from tkinter import ttk
from itertools import product
import pandas as pd
from tabulate import tabulate
from termcolor import colored


#This function checks monotonicity:
def check_monotonicity(func,inputs):
    if func[2] != 1 or func[6] != 0:
        return False

    for i, sc1 in enumerate(inputs):
        for j, sc2 in enumerate(inputs):
            if scenarios_comparable(sc1, sc2) and func[i] > func[j]:
                return False
    return True


#This function compare scenarios based on activation and inhibition
def scenarios_comparable(s1, s2):
    if (s1[2] == s2[2] and s1[3] == s2[3] and s1[0] <= s2[0] and s1[1] <= s2[1]) or \
            (s1[0] == s2[0] and s1[1] == s2[1] and s1[2] >= s2[2] and s1[3] >= s2[3]):
        return True
    return False

#This function create a DataFrame to store the data
def prepare_dataframe(inputs,monotonic_funcs):
    formatted_data = []
    for func in monotonic_funcs:
        formatted_row = [colored('1', 'red') if bit == 1 else colored('0', 'white') for bit in func]
        formatted_data.append(formatted_row)

    return pd.DataFrame(formatted_data, columns=[str(inp) for inp in inputs])

#This function display the table using tkinter
def display_table(df):
    window = tk.Tk()
    window.title("Monotonic Functions Overview")

    tree = ttk.Treeview(window, columns=list(df.columns), show='headings')

    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.pack(expand=True, fill='both')
    window.mainloop()


#This function print outputs to console
def console_output(df,monotonic_funcs):
    print(tabulate(df, headers='keys', tablefmt='pretty'))
    print(f"Total monotonic functions: {len(monotonic_funcs)}")
    print("Monotonic functions listing:")
    for func in monotonic_funcs:
        print(func)


def main():
    #input scenarios
    inputs = [
        (0, 0, 0, 0),
        (1, 0, 0, 0),
        (1, 1, 0, 0),
        (0, 0, 1, 0),
        (1, 0, 1, 0),
        (1, 1, 1, 0),
        (0, 0, 1, 1),
        (1, 0, 1, 1),
        (1, 1, 1, 1),
    ]

    #Generate all Boolean functions and filter for monotonicity
    possible_functions = list(product([0, 1], repeat=len(inputs)))
    monotonic_funcs = [func for func in possible_functions if check_monotonicity(func,inputs)]
    df = prepare_dataframe(inputs,monotonic_funcs)
    console_output(df,monotonic_funcs)
    display_table(df)

#calling the main
main()
