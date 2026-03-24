# Bit String Generator

## A program generating pseudorandom bit strings by simulating a customisable logic register

This project enables you to run a simulation on a fully customisable register comprised of D-type flip-flops and logic gates (NOT, AND, OR, XOR, NAND, NOR, XNOR). Values of next flip-flops in the current step of the simulation, create a string of bits (for example flip-flop1 - 1, flip-flop2 - 1, flip-flop3 - 0 creates 110), and at the end of the simulation all unique generated strings are shown. Additionally, the strings are ranked by space utilisation percentage (number generated/2^(bits in strings)*100%), and average number of changed bits between steps.

* Fully customise the register
* Set custom starting values
* Simulate stepping
* Create bit strings
* Compare different layouts
* Save results

## How does the simulation work?

The example below shows the next steps of the simulation of register from test.json file:

<img width="2000" height="1414" alt="ExampleSimulation1" src="https://github.com/user-attachments/assets/9944443f-7205-4158-8303-13503ad3e83b" />
Each step a bit string is created by reading every flip-flop's stored value in order, and appended to the string

<img width="2000" height="1414" alt="ExampleSimulation2" src="https://github.com/user-attachments/assets/a8227030-cc59-45ad-b3fa-89885a3af917" />
In this diagram, white squares represent flip-flops storing true, and black squares represent flip-flops storing false

<img width="2000" height="1414" alt="ExampleSimulation3" src="https://github.com/user-attachments/assets/77d89618-dd63-4d00-b77b-2976ad3d257c" />
Every flip-flop's value is updated to store the value on it's input

<img width="2000" height="1414" alt="ExampleSimulation4" src="https://github.com/user-attachments/assets/e0b1cbd4-53e9-497a-8d9b-3d0f43cdab91" />
Logic gates change how the new values are calculated by doing logic operations

<img width="2000" height="1414" alt="ExampleSimulation5" src="https://github.com/user-attachments/assets/aba38c2a-7eeb-4997-8115-0e50083c92ec" />

<img width="2000" height="1414" alt="ExampleSimulation6" src="https://github.com/user-attachments/assets/d4297e0c-1e99-42c9-9ba8-163a7af0d1c0" />

## How to run the program

1. Download all required files:
* components.py
* errors.py
* file_reader.py
* generator.py
* test.json (or other .json file containing correct connections (not any of the test files))

2. Run generator.py

3. Input a path to your .json file

4. Input ids of flip-flops which you want to set values manually (defaults to false) separated by a comma and space (for example: 1, 3, 4)

5. Input values for chosen flip-flops one by one as shown in the text

6. (optional) Should you input an id not present in the .json file, you will get the option to replace the mistake, and write the id again or skip it entirely

7. Choose a stepping mode - a fixed number of steps (fixed) or until the strings repeat (loop)

8. (optional) If you picked a fixed number of steps specify the number by inputting an integer number

9. The program will output all unique generated strings, the space utilisation percentage, and the average changing bits between strings. You can choose to save the results by inputting "yes" or end the program by inputting "no". The results will be saved in the same folder as the program under "result.txt".

## How to create your own register

The register file has to be a .json file which contains a list of dictionaries. Every dictionary inside corresponds to one flip-flop, and contains 2 or 3 keys:
* id - gate's unique identifier (any string) used for connecting components correctly
* input - id of the gate that connects to this one's input or a list of gate ids if there is a AND, OR, XOR, NAND, NOR, XNOR gate specified
* (optional) gate - type of gate connecting to the input (NOT, AND, OR, XOR, NAND, NOR, XNOR). WARNING! AND, OR, XOR, NAND, NOR, XNOR gates require the input to be a list of 2+ gate ids

Visual example of test.json file creating register on the right:

<img width="2000" height="1414" alt="FileExample" src="https://github.com/user-attachments/assets/e63d5f67-dc3d-4010-a335-a1ee8eb7891e" />
