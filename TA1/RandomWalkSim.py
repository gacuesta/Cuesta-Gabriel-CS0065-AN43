import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -------- Get user input from console --------
num_agents = int(input("Enter number of agents: "))
grid_size = int(input("Enter grid size (e.g., 10 for 10x10): "))
num_steps = int(input("Enter number of steps: "))

# -------- Agent Definition --------
class RandomWalker(ap.Agent):

    def setup(self):
        # Store the path of the agent
        self.path = []

    def step(self):

        # Save current position before moving
        self.path.append(self.position)

        x, y = self.position

        # Possible movements
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # Shuffle directions so movement remains random
        random.shuffle(directions)

        # Try each possible direction
        for dx, dy in directions:

            new_x = x + dx
            new_y = y + dy

            # Make sure agent stays inside grid
            if not (0 <= new_x < self.model.p.grid_size[0] and
                    0 <= new_y < self.model.p.grid_size[1]):
                continue

            new_position = (new_x, new_y)

            # Check if another agent is already there
            occupied = False

            for other in self.model.agents:
                if other != self and other.position == new_position:
                    occupied = True
                    break

            # Move only if position is not occupied
            if not occupied:
                self.position = new_position
                break


# -------- Model Definition --------
class RandomWalkModel(ap.Model):

    def setup(self):

        # Create agents
        self.agents = ap.AgentList(
            self,
            self.p.agents,
            RandomWalker
        )

        # Initialize random positions
        for agent in self.agents:
            agent.position = (
                random.randint(0, self.p.grid_size[0] - 1),
                random.randint(0, self.p.grid_size[1] - 1)
            )

            # Start path with initial position
            agent.path.append(agent.position)

        # Create grid
        self.grid = ap.Grid(
            self,
            self.p.grid_size,
            torus=False
        )

        self.grid.add_agents(self.agents)

    def step(self):

        for agent in self.agents:
            agent.step()


# -------- Parameters from user input --------
parameters = {
    'agents': num_agents,
    'grid_size': (grid_size, grid_size),
    'steps': num_steps
}


# -------- Run Model --------
model = RandomWalkModel(parameters)
model.setup()


# -------- Animation --------
fig, ax = plt.subplots()

ax.set_xlim(-0.5, model.p.grid_size[0] - 0.5)
ax.set_ylim(-0.5, model.p.grid_size[1] - 0.5)

ax.set_xticks(range(model.p.grid_size[0]))
ax.set_yticks(range(model.p.grid_size[1]))

ax.grid(True)

# Create one line for each agent
lines = []

for agent in model.agents:
    line, = ax.plot([], [], linewidth=1)
    lines.append(line)

# Agent positions
scat = ax.scatter([], [], s=200)


def update(frame):

    # Move agents
    model.step()

    # Update paths
    for i, agent in enumerate(model.agents):

        x_path = [position[0] for position in agent.path]
        y_path = [position[1] for position in agent.path]

        lines[i].set_data(x_path, y_path)

    # Update agent positions
    x = [agent.position[0] for agent in model.agents]
    y = [agent.position[1] for agent in model.agents]

    scat.set_offsets(list(zip(x, y)))

    return lines + [scat]


ani = animation.FuncAnimation(
    fig,
    update,
    frames=model.p.steps,
    blit=True,
    repeat=False
)

plt.show()