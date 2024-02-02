import pyvista as pv
import numpy as np

# Define the size of the grid
grid_size = 10
elevation_factor = 5

# Generate random data for biomes and elevation
biomes = np.random.randint(1, 5, size=(grid_size, grid_size))
elevation = np.random.rand(grid_size, grid_size) * elevation_factor

# Create a voxel grid
voxel_array = np.zeros((grid_size, grid_size, grid_size), dtype=bool)

# Fill the voxel grid with "blocks" up to the elevation height
for i in range(grid_size):
    for j in range(grid_size):
        height = int(elevation[i, j])
        voxel_array[i, j, :height] = True

# Convert the voxel grid to a PyVista mesh
voxels = pv.voxelize(pv.make_mesh(voxel_array))

# Assign colors to biomes (1: forest, 2: desert, 3: water, 4: mountain)
color_map = {
    1: 'green',
    2: 'yellow',
    3: 'blue',
    4: 'grey'
}

# Create a color array for the voxels
colors = np.empty((grid_size, grid_size, grid_size, 3), dtype=np.uint8)
for i in range(grid_size):
    for j in range(grid_size):
        biome = biomes[i, j]
        colors[i, j, :int(elevation[i, j]), :] = pv.plotting.hex_to_rgb(color_map[biome])

# Apply the colors to the voxels
voxels.cell_arrays['colors'] = colors.reshape(-1, 3, order='F')
voxels.plot(scalars='colors', rgb=True)
