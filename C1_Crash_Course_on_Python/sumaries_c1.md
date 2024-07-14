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
>>...    (return base*height)/2   

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
You can do this by using square brackets and the location, or index, of the character you want to access. It's important to remember that Python starts indexes at 0. So to access the first character in a string, you would use the index [0]. If you try to access an index that’s larger than the length of your string, you’ll get an **IndexError**. This is because you’re trying to access something that doesn't exist! You can also access indexes from the end of the string going towards the start of the string by using negative values. The index [-1] would access the last character of the string, and the index [-2] would access the second-to-last character. It's also access a portion of a string, called a slice or a substring. This allows you to access multiple characters of a string. You can do this by creating a range, using a colon as a separator between the start and end of the range, like [2:5]. For instance:

This range is similar to the range() function we saw previously. It includes the first number, but goes to one less than the last number. For example:  
> fruit = "Mangosteen"   
> fruit[1:4]  
'ang'

The slice includes the character at index 1, and excludes the character at index 4. You can also easily reference a substring at the start or end of the string by only specifying one end of the range. For example, only giving the end of the range:
>fruit[:5]   
'Mango'

This gave us the characters from the start of the string through index 4, excluding index 5. On the other hand this example gives is the characters including index 5, through the end of the string:
> fruit[5:]   
'steen'

You might have noticed that if you put both of those results together, you get the original string back!
> fruit[:5] + fruit[5:]   
'Mangosteen'

- Methods

    If we aren't sure what the index of our typo is, we can use the string method *index* to locate it and return the index. Let's imagine we have the string **"lions tigers and bears"** in the variable animals. We can locate the index that contains the letter **g** using *animals.index("g")*, which will return the index; in this case 8. We can also use substrings to locate the index where the substring begins. animals.index("bears") would return 17, since that’s the start of the substring. If there’s more than one match for a substring, the index method will return the first match. If we try to locate a substring that doesn't exist in the string, we’ll receive a **ValueError** explaining that the substring was not found.

- Advance
    + The string method **lower** will return the string with all characters changed to lowercase. The inverse of this is the **upper** method, which will return the string all in uppercase. Just like with previous methods, we call these on a string using dot notation, like **"this is a string".upper()**. This would return the string **"THIS IS A STRING"**. This can be super handy when checking user input, since someone might type in all lowercase, all uppercase, or even a mixture of cases.
    + You can use the **strip** method to remove surrounding whitespace from a string. Whitespace includes spaces, tabs, and newline characters. You can also use the methods  **lstrip** and **rstrip** to remove whitespace only from the left or the right side of the string, respectively.
    + The method **count** can be used to return the number of times a substring appears in a string.
    + If you wanted to check if a string ends with a given substring, you can use the method **endswith**. This will return True if the substring is found at the end of the string, and False if not.
    + The **isnumeric** method can check if a string is composed of only numbers. If the string contains only numbers, this method will return True. We can use this to check if a string contains numbers before passing the string to the **int()** function to convert it to an integer, avoiding an error. Useful!
    + Use the **join** method to concatenate strings. This method is called on a string that will be used to join a list of strings. The inverse of the join method is the **split** method which allowing us to split a string into a list of strings.

- Formatting  
    Use the **format** method on strings to concatenate and format strings in all kinds of powerful ways. To do this, create a string containing curly brackets, **{}**, as a placeholder, to be replaced. Then call the format method on the string using .format() and pass variables as parameters.

- String reference guide
    + String operations
        + len(string) - Returns the length of the string
        + for character in string - Iterates over each character in the string
        + if substring in string - Checks whether the substring is part of the string 
        + string[i] - Accesses the character at index i of the string, starting at zero
        + string[i:j] - Accesses the substring starting at index i, ending at index j minus 1. If i is omitted, its value defaults to 0. If j is omitted, the value will default to len(string).

    + String methods
        + string.lower() - Returns a copy of the string with all lowercase characters
        + string.upper() - Returns a copy of the string with all uppercase characters
        + string.lstrip() - Returns a copy of the string with the left-side whitespace removed
        + string.rstrip() - Returns a copy of the string with the right-side whitespace removed
        + string.strip() - Returns a copy of the string with both the left and right-side whitespace removed
        + string.count(substring) - Returns the number of times substring is present in the string
        + string.isnumeric() - Returns True if there are only numeric characters in the string. If not, returns False.
        + string.isalpha() - Returns True if there are only alphabetic characters in the string. If not, returns False.
        + string.split() - Returns a list of substrings that were separated by whitespace (whitespace can be a space, tab, or new line)
        + string.split(delimiter) - Returns a list of substrings that were separated by whitespace or a delimiter
        + string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.
        + delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter 

- Formatting Strings Guide 
    + Formatting expression:

    | Expr | Meaning | Example |
    | -------- | -------- | -------- |
    |{:d}| integer value|'{:d}'.format(10.5) → '10'|
    |{:.2f}|floating point with that many decimals|'{:.2f}'.format(0.5) → '0.50'|
    |{:.2s}|string with that many characters|'{:.2s}'.format('Python') → 'Py'|
    |{:<6s}|string aligned to the left that many spaces|'{:<6s}'.format('Py') → 'Py'|
    |{:>6s}|string aligned to the right that many spaces|'{:>6s}'.format('Py') → 'Py'|
    |{:^6s}|string centered in that many spaces|'{:^6s}'.format('Py') → 'Py'|

- Formatted string literals (Optional)   
Example:
> name = "Micah"  
> print(f'Hello {name}')  
Hello Micah

- Knowledge  
    **String Operations and Methods**
    - .format() - String method that can be used to concatenate and format strings. 
        + {:.2f} - Within the .format() method, limits a floating point variable to 2 decimal places. The number of decimal places can be customized.

    - len(string) - String operation that returns the length of the string.

    - string[x] - String operation that accesses the character at index [x] of the string, where indexing starts at zero.

    - string[x:y] - String operation that accesses a substring starting at index [x] and ending at index [y-1]. If x is omitted, its value defaults to 0. If y is omitted, the value will default to len(string).

    - string.replace(old, new) - String method that returns a new string where all occurrences of an old substring have been replaced by a new substring.

    - string.lower() - String method that returns a copy of the string with all lowercase characters.


### Lists








