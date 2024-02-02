import pyvista as pv
import numpy as np
import matplotlib.colors

# Define the size of the grid and the elevation factor
grid_size = 10
elevation_factor = 5

# Generate random data for biomes and elevation
biomes = np.random.randint(1, 5, size=(grid_size, grid_size))
elevation = np.random.rand(grid_size, grid_size, grid_size) * elevation_factor

# Assign colors to biomes (1: forest, 2: desert, 3: water, 4: mountain)
color_map = {
 1: '#008000', # green
 2: '#FFFF00', # yellow
 3: '#0000FF', # blue
 4: '#808080' # grey
}

# Create an ImageData
grid = pv.ImageData()

# Set the grid dimensions
grid.dimensions = np.array([grid_size, grid_size, grid_size])

# Edit the spatial reference
grid.origin = (0, 0, 0) # The bottom left corner of the data set
grid.spacing = (1, 1, 1) # These are the cell sizes along each axis

# Create a color array for the voxels
colors = np.empty((grid_size, grid_size, grid_size, 3), dtype=np.uint8)
for i in range(grid_size):
    for j in range(grid_size):
        for k in range(grid_size):
            biome = biomes[i, j]
            colors[i, j, k, :] = matplotlib.colors.hex2color(color_map[biome])

# Add the data values to the point data
grid.point_data["colors"] = colors.reshape(-1, 3, order='F')

# Now plot the grid!
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(grid, scalars="colors", rgba=True)
plotter.show(screenshot='3d_heatmap.png')
