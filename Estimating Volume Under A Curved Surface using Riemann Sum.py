def f(x, y):
    return x**2 + y**2

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

x_min = float(input("Enter the minimum value for x: "))
x_max = float(input("Enter the maximum value for x: "))
y_min = float(input("Enter the minimum value for y: "))
y_max = float(input("Enter the maximum value for y: "))
n = int(input("Enter the number of iterations (n): "))

volume = estimate_volume(x_min, x_max, y_min, y_max, n)

print(f"Estimated volume: {volume}")
