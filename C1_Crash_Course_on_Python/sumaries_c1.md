# Summaries C1

## Module 1
### Syntax and code blocks
- Common syntax error
    + Misspellings
    + Incorrect indentations
    + Missing or incorrect key characters:
        + Bracket types - ( curved ), [ square ], { curly }
        + Quote types - "straight-double" or 'straight-single', “curly-double” or ‘curly-single’
        + Block introduction characters, like colons - :
    + Data type mismatches
    + Missing, incorrectly used, or misplaced Python reserved words
    + Using the wrong case (uppercase/lowercase) - Python is a case-sensitive language 


### First concept
- Arithmetic operators   

Python can calculate numbers using common mathematical operators, along with some special operators, too:  
| Expression | Explain |
| -------- | -------- |
|x + y|           Addition + operator returns the sum of x plus y   
|x - y|           Subtraction - operator returns the difference of x minus y   
|x * y|           Multiplication * operator returns the product of x times y   
|x / y|           Division / operator returns the quotient of x divided by y   
|X**e|            Exponent ** operator returns the result of raising x to the power of e    
|x**2|            Square expression returns x squared   
|x**3|            Cube expression returns x cubed   
|x**(1/2)|        Square root (½) or (0.5) fractional exponent operator returns the square root of x   
|x // y|          Floor division operator returns the integer part of the integer division of x by y   
|x % y|           Modulo operator returns the remainder part of the integer division of x by y   

- Order of operations
The order of operations are to be calculated from left to right in the following order: 

    1. Parentheses ( ), { }, [ ]
    2. Exponents xe   (x**e)
    3. Multiplication * and Division /  
    4. Addition + and Subtraction -    

 You might find the **PEMDAS** mnemonic device to be helpful in remembering the order.   




## Module 2

### Expressions and Variables
- When the error **"TypeError"** that, try to check the data type of something using the type() function.   
- Implicit vs Explicit Conversion: some data types can be mixed and matched due to implicit conversion. Implicit conversion is where the interpreter helps us out and automatically converts one data type into another, without having to explicitly tell it to do so. For instance:   
>total = 2048 + 4357 + 97658 + 125 + 8 #the result of total is 104196  
>files = 5   
>average = total / files    
>print("The average size is: " + str(average))# the output is The average size is: 20839.2
- Terms:
    + expression - a combination of numbers, symbols, or other values that produce a result when evaluated
    + data types - classes of data (e.g., string, int, float, Boolean, etc.), which include the properties and behaviors of instances of the data type (variables)
    + variable - an instance of a data type class, represented by a unique name within the code, that stores changeable values of the specific data type
    + implicit conversion - when the Python interpreter automatically converts one data type to another
    + explicit conversion - when code is written to manually convert one data type to another using a data type conversion function:
        + str() - converts a value (often numeric) to a string data type
        + int() - converts a value (usually a float) to an integer data type
        + float() - converts a value (usually an integer) to a float data type


### Function
Example:
>def area_triangle(base, height):   
...    (return base*height)/2   
>area_a=area_triangle(5,4)   
>area_b=area_triangle(7,3)   
>sum=area_a+area_b   
>print("The sum of both areas is: ", str(sum)) #The sum of both areas is 20.5

Terms:

    - return value - the value or variable returned as the end result of a function
    - parameter (argument) -  a value passed into a function for use within the function
    - refactoring code - a process to restructure code without changing functionality

Knowledge:  

    - The purpose of the def() keyword is to define a new function. 
    - Best practices for writing code that is readable and reusable:
    - Create a reusable function - Replace duplicate code with one reusable function to make the code easier to read and repurpose.
    - Refactor code - Update code so that it is self-documenting and the intent of the code is clear.
    - Add comments - Adding comments is part of creating self-documenting code. Using comments allows you to leave notes to yourself and/or other programmers to make the purpose of the code clear.


### Conditional
1. Comparison Operators with Equations and Strings   

    The following examples demonstrate how to use comparison operators with the data types **int** (integers, whole numbers) and **float** (number with a decimal point or fractional value). Comparison operators return **Boolean** results. As you learned previously, Boolean is a data type that can hold only one of two values: True or False.     

    The comparison operators include: 
    | Symbol | Explain |
    | -------- | -------- |
    |==|    (equality) 
    |!=|     (not equal to) 
    |>|       (greater than)
    |<|      (less than)
    |>=|    (greater than or equal to)
    |<=|    (less than or equal to)


2. Logical Operators   

    Logical operators are used to construct more complex expressions. You can make complex comparisons by joining comparison statements together using the ***logical operators: and, or, not***. Complex comparisons return a **Boolean (True or False)** result. 

        - and   
            + Both sides of the statement being evaluated must be True for the whole statement to be True. 
            + Example: (5 > 1 and 5 < 10) = True

        - or 
            + If either side of the comparison is True, then the whole statement is True. 
            + Example: (color = "blue" or color = "green") = True

        - not 
            + Inverts the Boolean result of the statement immediately following it. So, if a statement evaluates to True, and we put the not operator in front of it, it would become False.
            + Example: (not "A" == "A") = False




## Module 3

### While loops
If you try to use a variable without first initializing it, you'll run into a **"NameError"**. This is the Python interpreter catching the mistake and telling you that you’re using an undefined variable. The fix is pretty simple: initialize the variable by assigning the variable a value before you use it.

1. Common Errors in while Loops   
    If you get an error message on a loop or it appears to hang, your debugging checklist should include the following checks:

    - **Failure to initialize variables**. Make sure all the variables used in the loop’s condition are initialized before the loop.

    - **Unintended infinite loops**. Make sure that the body of the loop modifies the variables used in the condition, so that the loop will eventually end for all possible values of the variables. You can often prevent an infinite loop by using the break keyword or by adding end criteria to the condition part of the while loop.

2. while Loop Terms
    - while loop - Tells the computer to execute a set of instructions while a specified condition is True. In other words, while loops keep executing the same group of instructions until the condition becomes False.
    - infinite loop - Missing a method for exiting the loop, causing the loop to run forever.
    - break - A keyword that can be used to end a loop at a specific point. 


### For loops
1. *for* loops begin with the keyword **for** with a colon at the end of the line. 
2. The **range()** function can take up to three parameters:  **range(start, stop, step)**:
    - **start**: The first item in the range() function parameters is the starting position of the range.
    - **stop**: The ending position of the range.
    - **step**: The incremental step value.

3. **for** Loops vs. **while** Loops

    **for** loops and **while** loops share several characteristics. Both loops can be used with a variety of data types, both can be nested, and both can be used with the keywords **break** and **continue**. However, there are important differences between the two types of loops:  
    - **while** loops are used when a segment of code needs to execute repeatedly **while** a condition is true
    - **for** loops iterate over a sequence of elements, executing the body of the loop **for** each element in the sequence


4. Recursion
Example:
>def recursive_function(parameters):  
>>   if base_case_condition(parameters):  
    >>>    return base_case_value  

>>  recursive_function(modified_parameters)

docs: 



## Module 4
### Strings

