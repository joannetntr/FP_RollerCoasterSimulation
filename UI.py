import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
from simulation import RollerCoaster


class RollerCoasterUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Roller Coaster Simulation')
        self.geometry('1000x600')

        self.input_frame = tk.Frame(self)
        self.input_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Input fields
        height_label = tk.Label(self.input_frame, text='Height (m):')
        height_label.grid(row=0, column=0, padx=10, pady=5)
        self.height_entry = tk.Entry(self.input_frame)
        self.height_entry.grid(row=0, column=1, padx=10, pady=5)

        mass_label = tk.Label(self.input_frame, text='Mass (kg):')
        mass_label.grid(row=1, column=0, padx=10, pady=5)
        self.mass_entry = tk.Entry(self.input_frame)
        self.mass_entry.grid(row=1, column=1, padx=10, pady=5)

        radius_label = tk.Label(self.input_frame, text='Radius (m):')
        radius_label.grid(row=2, column=0, padx=10, pady=5)
        self.radius_entry = tk.Entry(self.input_frame)
        self.radius_entry.grid(row=2, column=1, padx=10, pady=5)

        track_length_label = tk.Label(self.input_frame, text='Track Length (m):')
        track_length_label.grid(row=3, column=0, padx=10, pady=5)
        self.track_length_entry = tk.Entry(self.input_frame)
        self.track_length_entry.grid(row=3, column=1, padx=10, pady=5)

        # Simulate button
        self.simulate_button = tk.Button(self.input_frame, text='Simulate', command=self.start_simulation)
        self.simulate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.result_label = tk.Label(self.input_frame, text='', anchor='w', justify='left')
        self.result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky='ew')

        self.graph_frame = tk.Frame(self)
        self.graph_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.graph_count = 0
        self.graphs = []

    def start_simulation(self):
        height = float(self.height_entry.get())
        mass = float(self.mass_entry.get())
        radius = float(self.radius_entry.get())
        track_length = float(self.track_length_entry.get())

        coaster = RollerCoaster(height=height, mass=mass, radius=radius, track_length=track_length)
        coaster.simulate()
        result = coaster.get_result()
        self.result_label.config(text=result)

        self.display_results(coaster)

    def display_results(self, coaster):
        fig = Figure(figsize=(12, 4), dpi=100)
        ax1 = fig.add_subplot(131)  # First subplot for height vs. time
        ax1.plot(coaster.times, coaster.heights)
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Height (m)')
        ax1.set_title('Height vs. Time')

        ax2 = fig.add_subplot(132)  # Second subplot for velocity vs. time
        ax2.plot(coaster.times, coaster.velocities)
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Velocity (m/s)')
        ax2.set_title('Velocity vs. Time')

        ax3 = fig.add_subplot(133, projection='3d')  # Third subplot for roller coaster simulation
        ax3.plot(coaster.positions_x, coaster.positions_y, coaster.positions_z)
        ax3.set_xlabel('Position X (m)')
        ax3.set_ylabel('Position Y (m)')
        ax3.set_zlabel('Position Z (m)')
        ax3.set_title('Roller Coaster Simulation (3D)')

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT, padx=10, pady=10)

        self.graph_count += 1
        self.graphs.append(fig)

        if self.graph_count % 3 == 0:
            new_row_frame = tk.Frame(self.graph_frame)
            new_row_frame.pack()

        if self.graph_count % 2 == 0:
            tk.Label(self.graph_frame, width=20).pack(side=tk.LEFT)

    def clear_graphs(self):
        for graph in self.graphs:
            plt.close(graph)

        self.graph_count = 0
        self.graphs = []
        self.graph_frame.destroy()
        self.graph_frame = tk.Frame(self)
        self.graph_frame.pack(side=tk.LEFT, padx=10, pady=10)


if __name__ == '__main__':
    roller_coaster_ui = RollerCoasterUI()
    roller_coaster_ui.mainloop()

