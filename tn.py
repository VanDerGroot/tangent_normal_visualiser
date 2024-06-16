import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate the spiral
def generate_spiral(a, b, num_points):
    theta = np.linspace(0, 4 * np.pi, num_points)
    r = a + b * theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y, theta

# Function to calculate the tangent and normal at a point on the spiral
def calculate_tangent_normal(x, y, theta, i):
    dx_dt = np.gradient(x, theta)
    dy_dt = np.gradient(y, theta)
    
    tangent = np.array([dx_dt[i], dy_dt[i]])
    tangent /= np.linalg.norm(tangent)
    
    # Rotate the tangent vector by 90 degrees clockwise to get the normal vector
    normal = np.array([tangent[1], -tangent[0]])

    return tangent, normal

# Parameters for the spiral
a = 0
b = 0.2
num_points = 500

# Generate spiral data
x, y, theta = generate_spiral(a, b, num_points)

# Set up the plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
spiral_line, = ax.plot(x, y, 'b')
tangent_line, = ax.plot([], [], 'g', label='Tangent')  # Swapped colors and labels
normal_line, = ax.plot([], [], 'r', label='Normal')  # Swapped colors and labels
point, = ax.plot([], [], 'ko')

# Initialize animation
def init():
    tangent_line.set_data([], [])
    normal_line.set_data([], [])
    point.set_data([], [])
    return tangent_line, normal_line, point

# Animation function
def animate(i):
    if i >= num_points:
        return tangent_line, normal_line, point

    tangent, normal = calculate_tangent_normal(x, y, theta, i)
    point.set_data([x[i]], [y[i]])

    normal_start = [x[i], y[i]]  # Displaying tangent in red now
    normal_end = [x[i] + tangent[0], y[i] + tangent[1]]
    normal_line.set_data([normal_start[0], normal_end[0]], [normal_start[1], normal_end[1]])

    tangent_start = [x[i], y[i]]  # Displaying normal in green now
    tangent_end = [x[i] + normal[0], y[i] + normal[1]]
    tangent_line.set_data([tangent_start[0], tangent_end[0]], [tangent_start[1], tangent_end[1]])

    return tangent_line, normal_line, point

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_points, interval=50, blit=True)

# Show plot with animation
plt.legend()
plt.show()
