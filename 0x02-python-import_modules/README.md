# Python - import & modules

This project, taughtme about importing and using Functions and creating
Python modules. I continued to practice using the builtin function
`dir()` and using the command line arguments within Python programs.

## Tasks :page_with_curl:

* **0. Import simple function from simple file**
  * [0-add.py](./0-add.py): Python program will import the function
  `def add(a, b):` from the file [add_0.py](./add_0.py) and print the
  result of the addition `1 + 2 = 3`.
  * Output: `<a value> + <b value> = <add(a, b) value>` followed by a new line.

* **1. My First toolbox!**
  * [1-calculation.py](./1-calculation.py): Python program import functions
  from the file [calculator_1.py](./1-calculator.py) and print the result
  of the addition, subtraction, multiplication and division of `10` and `5`.
  * Output: `<a value> <operator> <b value> = <operation(a, b) value>` followed by a new line.

* **2. How to make script dynamic!**
  * [2-args.py](./2-args.py): Python program Will print number of
  list of its arguments.
  * Output: `[Number of arguments] argument` (if number is one) or `arguments` (otherwise), followed by:
    * `:` (or `.` if no argumets were passed), followed by
    * A new line, followed by
    * One argument per line - position the argument (starting at `1`) followed by `:` followed by the argument value and another new line.

* **3. Infinite addition**
  * [3-infinite_add.py](./3-infinite_add.py): Python program will prints the result of the
  addition of all arguments.
  * Output: Sum of the arguments followed by a new line.

* **4. Who are you?**
  * [4-hidden_discovery.py](./4-hidden_discovery.py): Python program will prints all the
  names defined by the compiled module `hidden_4.pyc`.
  * Output: One name per line in alphabetical order.
  * Names starting with `__` are not printed.

* **5. Everything can be imported**
  * [5-variable_load.py](./5-variable_load.py): Python program that imorts the
  variable `a` from the file [variable_load_5.py](./variable_load_5.py) and prints its value.

* **6. Build my own calculator!**
  * [100-my_calculator.py](./100-my_calculator.py): Python program that imports all functions
  from the file [calculator_1.py](./calculator_1.py) and handles basic operations.
  * Usage: `./100-my_calculator.py <a> <operator> <b>` followed by a new line.
  * Output: `<a> <operator> <b> = <result>` followed by a new line.
  * The parameter `operator` can be:
    * `+` for addition
    * `-` for subtraction
    * `*` for multiplication
    * `/` for division
  * If the operator is none of the above, the function prints `Unknown operator.
  Available operators: +, -, *, and /` followed by a new line and exits
  with a status value of `1`.
  * If the number of arguments is not three, the program prints `Usage: ./1s -my_calculator.py <a> <operator> <b>` followed by a new line and exits with a status value of `1`.

* **7. Easy print**
  * [101-easy_print.py](./101-easy_print.py): Python program that pwith
  `#pythoniscool` followed by a new line in the standard output.
  * Without using `print`, `eval`, `open`, or `sys`.

* **8. ByteCode -> Python #3**
  * [102-magic_calculation.py](./102-magic_calculation.py): Python functions matching exactly a
  bytecode provided by Holberton School.

* **9. Fast alphabet**
  * [103-fast_alphabet.py](./103-fast_alphabet.py): Python program will print the alphabet in
  uppercase, followed by a new line.
  * Without using loops, conditoinals, `str.join()`, string literals, or system calls.

