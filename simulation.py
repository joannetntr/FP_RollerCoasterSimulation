import math
import numpy as np


class RollerCoaster:
    def __init__(self, height, mass, radius, track_length):
        self.height = height
        self.mass = mass
        self.radius = radius
        self.track_length = track_length
        self.g = 9.8  # acceleration due to gravity

        self.times = None
        self.heights = None
        self.velocities = None
        self.positions_x = None
        self.positions_y = None
        self.positions_z = None

        self.g_forces = None
        self.net_forces = None

    def simulate(self):
        time_interval = 0.01  # time interval for simulation
        total_time = math.sqrt(2 * self.height / self.g) + math.sqrt(2 * (self.height - self.radius) / self.g)
        self.times = np.arange(0, total_time, time_interval)
        self.heights = []
        self.velocities = []
        self.positions_x = []
        self.positions_y = []
        self.positions_z = []

        self.g_forces = []
        self.net_forces = []

        for t in self.times:
            if t <= math.sqrt(2 * self.height / self.g):
                h = self.height - 0.5 * self.g * t ** 2
                v = -self.g * t
                g_force = abs(self.g)
                net_force = self.mass * self.g
            else:
                t1 = math.sqrt(2 * self.height / self.g)
                h = self.radius - self.radius * math.cos(math.sqrt(self.g / self.radius) * (t - t1))
                v = math.sqrt(self.g * self.radius) * math.sin(math.sqrt(self.g / self.radius) * (t - t1))
                g_force = abs(self.g + (v ** 2) / self.radius)
                net_force = self.mass * (self.g + (v ** 2) / self.radius)

            self.heights.append(h)
            self.velocities.append(v)
            self.positions_x.append(self.radius * math.sin(math.sqrt(self.g / self.radius) * t))
            self.positions_y.append(self.height - h)
            self.positions_z.append(self.radius * math.cos(math.sqrt(self.g / self.radius) * t))
            self.g_forces.append(g_force)
            self.net_forces.append(net_force)

    def get_result(self):
        result = f"Maximum Height: {max(self.heights):.2f} m\n"
        result += f"Minimum Height: {min(self.heights):.2f} m\n"
        result += f"Maximum Velocity: {max(self.velocities):.2f} m/s\n"
        result += f"Minimum Velocity: {min(self.velocities):.2f} m/s\n"
        result += f"Maximum G-Force: {max(self.g_forces):.2f} g\n"
        result += f"Minimum G-Force: {min(self.g_forces):.2f} g\n"
        result += f"Maximum Net Force: {max(self.net_forces):.2f} N\n"
        result += f"Minimum Net Force: {min(self.net_forces):.2f} N\n"
        return result
