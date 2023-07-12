questions = [
    # 1
    {
        "question": "What is the correct syntax for replacing the string apple in the list with the string orange?\nmy_list = [2, 'apple', 3.5]",
        "options": ["a. my_list['orange'] = 1", "b. my_list[1] = 'orange'", "c. 'orange' = my_list[1] ", "d. my_list[1] == 'orange'"],
        "correct_answer": "my_list[1] = 'orange'"
    },
    # 2
    {
        "question": "How do you add a comment to existing Python script?",
        "options": ["a. -- This is a comment", "b. /* This is a comment *\\", "c. // This is a comment", "d. # This is a comment"],
        "correct_answer": "d"
    },
    # 3
    {
        "question": "Given a list defined as numbers = [1,2,3,4], what is the value of numbers[-2]?",
        "options": ["a. 3", "b. An IndexError exception is thrown", "c. 1", "d. 2"],
        "correct_answer": "a"
    },
    # 4
    {
        "question": "What operator do you use to assess equality between two elements?",
        "options": ["a. ||", "b. &&", "c. =", "d. =="],
        "correct_answer": "d"
    },
    # 5
    {
        "question": "Suppose you want to double-check if two matrices can be multiplied using NumPy for debugging purposes. How would you complete this code fragment by filling in the blanks with the appropriate variables?\nimport numpy as np\ndef can_matrices_be_multiplied (matrix1, matrix2):\n\trowsMat1, columnsMat1 = matrix1.shape\n\trowsMat2, columnsMat2 = matrix2.shape\n\n\tif ____ == ____ :\n\t\tprint('The matrices can be multiplied!')\n\t\treturn True\n\telse:\n\t\treturn False",
        "options": ["a. columnsMat1; rowsMat1;", "b. columnsMat1; rowsMat2", "c. columnsMat1; columnsMat2", "d. columnsMat2; rowsMat1"],
        "correct_answer": "b"
    },
    # 6
    {
        "question": "What will be the value of x after running this code?\nx = {1,2,3,4,5}\nx.add(5)\nx.add(6)",
        "options": ["a. {1,2,3,4,5,5,6}", "b. {1,2,3,4,5,6}", "c. {5,6,1,2,3,4,5}", "d. {6,1,2,3,4,5}"],
        "correct_answer": "b"
    },
    # 7
    {
        "question": "What is the output of this code? (NumPy has been imported as np.)\na = np.array([1,2,3,4])\nprint(a[[False, True, False, False]])",
        "options": ["a. {2}", "b. [2]", "c. {0,2}", "d. [0,2,0,0]"],
        "correct_answer": "b"
    },
    # 8
    {
        "question": "Which fragment of code will print exactly the same output as this fragment?\nimport math\nprint(math.pow(2,10)) # prints 2 elevated to the 10th power",
        "options": ["a. \ny = [x*2 for x in range(1,10)]\nprint(y)", "b. print(2^10)", "c.\ny = 1\nfor i in range(1,10):\n\ty = y*2\nprint(y)", "d. print(2**10)"],
        "correct_answer": "d"
    },
    # 9
    {
        "question": "What will this line of code return? (Assume n is already defined as any positive integer value.)\n[x*2 for x in range(1,n)]",
        "options": ["a. a list with all the odd numbers less than 2*n", "b. a dictionary with all the even numbers less than 2*n", "c. a list with all the even numbers less than 2*n", "d. a list with all the even numbers less than or equal to 2*n"],
        "correct_answer": "c"
    },
    # 10
    {
        "question": "What will this code print?\nnumber = 3\nprint(f'The number is {number}')",
        "options": ["a. the number is 3", "b. It throws a TypeError because the integer must be cast to a string.", "c. The number is 3", "d. THE NUMBER IS 3"],
        "correct_answer": "c"
    },
    # 11
    {
        "question": "What is 17 % 15 equal to?",
        "options": ["a. 15", "b. 2", "c. 16", "d. 17"],
        "correct_answer": "b"
    },
    # 12
    {
        "question": "What is the output of this code?\nnum_list = [1,2,3,4,5]\nnum_list.remove(2)\nprint(num_list)",
        "options": ["a. [1,2,4,5]", "b. [1,3,4,5]", "c. [1,2,3]", "d. [3,4,5]"],
        "correct_answer": "b"
    },
    # 13
    {
        "question": "Which collection type is used to associate values with unique keys?",
        "options": ["a. dictionary", "b. queue", "c. shorted list", "d. slot"],
        "correct_answer": "a"
    },
    # 14
    {
        "question": "Suppose you need to use the sin function from the math library. What is the correct syntax for importing only that funcion?",
        "options": ["a. import math.sin", "b. from math import sin", "c. import sin from math", "d. using math.sin"],
        "correct_answer": "b"
    },
    # 15
    {
        "question": "In Python, how can the compiler identify the innner block of a for loop?",
        "options": ["a. because of the level of identation after the for loop", "b. because of the end keyword at the end of the for loop", "c. because of a blank space at the end of the body of the for loop", "d. because the block is surrounded by brackets ({})"],
        "correct_answer": "a"
    }
]