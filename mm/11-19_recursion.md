# Chapter 16: Recursion

Recursion is a technique where a function calls itself to solve smaller instances of the same problem.

## 1. The Three Laws of Recursion
For a recursive function to work correctly, it must follow these rules:
1.  **Base Case:** A condition that stops the recursion. It does *not* make a recursive call. Without this, you get infinite recursion.
2.  **Change of State:** The arguments passed to the recursive call must move toward the base case (e.g., list gets smaller, number gets lower).
3.  **Self-Call:** The function must call itself.

## 2. Execution Flow (Stack Frames)
* When a function is called, a **stack frame** is created to handle its local variables.
* In recursion, frames are stacked on top of each other.
* When the base case is reached, the stack "unwinds" and values are returned back up the chain.
* **RecursionError:** Occurs if the stack grows too large (depth exceeded).

## 3. Recursive Logic Example (Sum)
* **Iterative:** "Add the first number to a running total, then move to the next."
* **Recursive:** "The sum of a list is the first number plus the sum of the rest of the list."

    def recursive_sum(numbers):
        if not numbers:         # Base Case
            return 0
        else:                   # Recursive Step
            return numbers[0] + recursive_sum(numbers[1:])

## 4. Visualizing Recursion
* **Fractals:** Shapes that are self-similar (contain copies of themselves) are easy to draw recursively.
    * Examples: Koch Snowflake, Sierpinski Triangle.
    * Logic: "Draw a triangle. Inside that triangle, draw three smaller triangles. Repeat."