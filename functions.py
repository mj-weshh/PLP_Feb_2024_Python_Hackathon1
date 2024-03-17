# Functions & Fibonacci Sequence
# Question
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
#We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.
def fibonacci(n):
  if n > 1:
    a, b,= 0, 1
    fibonacci_sequence = [a, b]
    for i in range(2, n):
      
      c = a + b
      a = b
      b = c

      # Generate the Fibonacci sequence
      fibonacci_sequence.append(c)
    return fibonacci_sequence
  else:
    print('Error! the number of terms must be greater than 1.')
    return None
    

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Calling the fibonacci function and parsing num_terms as the argument
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print(fibonacci_sequence)

