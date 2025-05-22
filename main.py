
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


N = 50
grid = np.random.choice([0, 1], size=(N, N), p=[0.8, 0.2])

def update(frame_num, img, grid):
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((
                grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]
            ))
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1

    img.set_data(new_grid)
    grid[:] = new_grid[:]
    ax.set_title(f"Conway's Game of Life — Frame {frame_num}")
    return img,

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='binary_r')
ani = animation.FuncAnimation(fig,
    update,
    fargs=(img, grid),
    frames=1000,
    interval=10,
    repeat=False
)

plt.title("Conway's Game of Life")
plt.show()
