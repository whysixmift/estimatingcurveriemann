# Estimating Volume Under a Curved Surface using Riemann Sum

This Python project estimates the volume under a curved surface using the **Riemann Sum** method. The program allows the user to input the boundaries of the region in 2D space (x_min, x_max, y_min, y_max) and the number of iterations \(n\) to calculate the volume under a function, which is by default \( f(x, y) = x^2 + y^2 \).

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Customization](#customization)
- [License](#license)

## Requirements

- Python 3.x or higher
- **NumPy** (Optional, only if you modify the code to use NumPy for advanced features)

To install **NumPy**:

```bash
pip install numpy
```

## Installation

1. Clone or download this repository.
2. Navigate to the project directory:

   ```bash
   cd path/to/project
   ```

3. Install required dependencies (if any):

   ```bash
   pip install -r requirements.txt  # If there are dependencies listed
   ```

## Usage

1. Open a terminal or command prompt.
2. Run the Python script:

   ```bash
   python Estimating_Volume.py
   ```

3. You will be prompted to enter the following inputs:
   - **x_min**: The minimum value for \(x\).
   - **x_max**: The maximum value for \(x\).
   - **y_min**: The minimum value for \(y\).
   - **y_max**: The maximum value for \(y\).
   - **n**: The number of iterations for the Riemann Sum (higher values yield more accurate results but take longer).

Example input:

```bash
Enter the minimum value for x: -1
Enter the maximum value for x: 1
Enter the minimum value for y: -1
Enter the maximum value for y: 1
Enter the number of iterations (n): 1000
```

The program will then calculate and print the estimated volume.

## Code Explanation

### Function `f(x, y)`

This is the surface function we are working with. By default, it is:

```python
def f(x, y):
    return x**2 + y**2
```

You can modify this function to represent any surface.

### Function `estimate_volume(x_min, x_max, y_min, y_max, n)`

This function estimates the volume under the surface defined by `f(x, y)` using the **Riemann Sum** method. It works by discretizing the 2D space into a grid and summing the volume of small cuboids beneath the surface.

```python
def estimate_volume(x_min, x_max, y_min, y_max, n):
    dx = (x_max - x_min) / n
    dy = (y_max - y_min) / n
    
    volume = 0.0

    for i in range(n):
        for j in range(n):
            x = x_min + i * dx
            y = y_min + j * dy

            volume += f(x, y) * dx * dy

    return volume
```

### User Input

The program prompts the user for the following inputs:
- `x_min`, `x_max`: The boundaries for the x-axis.
- `y_min`, `y_max`: The boundaries for the y-axis.
- `n`: The number of iterations for calculating the Riemann Sum.

The values are obtained using the `input()` function:

```python
x_min = float(input("Enter the minimum value for x: "))
x_max = float(input("Enter the maximum value for x: "))
y_min = float(input("Enter the minimum value for y: "))
y_max = float(input("Enter the maximum value for y: "))
n = int(input("Enter the number of iterations (n): "))
```

### Output

After computing the volume, the program outputs the result:

```python
print(f"Estimated volume: {volume}")
```

## Customization

### Modify Surface Function

By default, the surface function is:

```python
def f(x, y):
    return x**2 + y**2
```

To change the surface function to something else, simply modify the `f(x, y)` definition. For example, to use a cubic function:

```python
def f(x, y):
    return x**3 + y**3
```

### Adjusting Precision

The parameter `n` (number of iterations) determines the precision of the Riemann Sum approximation. Increasing `n` will give a more accurate result, but it will also increase the computation time.

### Example Custom Function:

```python
def f(x, y):
    return x**2 + y**3  # Change the surface to a combination of x^2 and y^3
```

## License

This project is licensed under the MIT License
