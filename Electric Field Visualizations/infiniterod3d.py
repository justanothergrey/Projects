from vpython import *
from math import sqrt, pi, cos, sin

# Constants
k = 9e9   # Coulomb's constant
half_width=5

# Function to calculate the electric field at a given point
def E_field(pos):
    E = vector(0,0,0)
    for i in range(N_charges):
        dpos = pos - q_pos[i]
        r = mag(dpos)
        E += k*q_vals[i] * dpos / r**3
    return E

# Function to update the positions of the charges based on rod position
def update_charges():
    for i in range(N_charges):
        q_pos[i] = rod.pos + ((i - (N_charges-1)/2) * charge_spacing) * rod.axis.norm()

# Function to update the arrows based on the current electric field
def update_arrows():
    for arrow in arrows:
        pos = arrow.pos
        E = E_field(pos)
        E_mag = mag(E)
        if E_mag > 0:
            arrow.axis = E*arrow_scale*arrow_length/E_mag
        else:
            arrow.axis = vector(0,0,0)

# Function to update the Gaussian surface based on the current electric field
def update_surface():
    for i in range(N_voxels):
        for j in range(N_voxels):
            for k in range(N_voxels):
                pos = vec(i,j,k) * voxel_spacing - half_width
                E = E_field(pos)
                E_mag = mag(E)
                opacity = min(0.2, E_mag / 1e10)
                voxel_grid[i][j][k].opacity = opacity

# Function to move the rod in response to mouse movement
def move_rod(evt):
    # Calculate the new position of the rod based on mouse movement
    dtheta = (evt.pos.x - evt.last_event.pos.x) * pi / 180
    dphi = (evt.pos.y - evt.last_event.pos.y) * pi / 180
    rod.axis = rotate(rod.axis, angle=-dtheta, axis=vec(0,1,0))
    rod.axis = rotate(rod.axis, angle=dphi, axis=vec(1,0,0))
    rod.pos = rod_pos_init + rod.axis * rod_length/2
    update_charges()
    update_arrows()
    update_surface()

# Set up the scene
scene.width = 800
scene.height = 600
scene.background = color.white
scene.range = 2*half_width
scene.title = "Electric Field of an Infinite Charged Rod"

# Create the rod object
rod_pos_init = vec(0,0,0)
rod_length = 2*half_width
rod_radius = half_width/20
rod = cylinder(pos=rod_pos_init, axis=vec(0,rod_length,0), radius=rod_radius, color=color.blue)

# Create the charges on the rod
N_charges = 11
q_vals = [1e-9] * N_charges
charge_spacing = rod_length / (N_charges - 1)
q_pos = [vec(0,0,0)] * N_charges
update_charges()

# Create the arrows to represent the electric field
arrow_scale = 1e-9
arrow_length = half_width / charge_spacing

arrows = []
for i in range(N_charges):
    pos = q_pos[i]
    arrow = arrow(pos=pos, axis=vec(0,0,0), half_width =rod_radius/3, color=color.red)
    arrows.append(arrow)

#Create the Gaussian surface to visualize the electric field

N_voxels = 30
voxel_spacing = 2*half_width / (N_voxels - 1)
voxel_grid = [[[box(pos=vec(i,j,k)*voxel_spacing - half_width, length=voxel_spacing, height=voxel_spacing, depth=voxel_spacing, color=color.cyan, opacity=0.2) for k in range(N_voxels)] for j in range(N_voxels)] for i in range(N_voxels)]

#Bind the mouse move event to the function that moves the rod

scene.bind("mousemove", move_rod)
#Run the simulation

while True:
    rate(30)
