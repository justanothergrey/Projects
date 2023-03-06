from vpython import *

# Define constants
k = 9e9  # Coulomb's constant
lambda_rod = 1e-6  # Linear charge density of rod

# Define the length of the rod and the number of discrete charges to represent it
L = 5
num_charges = 20

# Define the position of the rod
rod_pos = vector(0,0,0)

# Create the rod as a series of point charges
charges = []
for i in range(num_charges):
    charge_pos = vector(L/num_charges * (i+0.5) - L/2, 0, 0) + rod_pos
    charge = sphere(pos=charge_pos, radius=0.1, charge=lambda_rod * L/num_charges, color=color.red)
    charges.append(charge)

# Define a function to calculate the electric field at a given point
def E_field(pos):
    E = vector(0,0,0)
    for charge in charges:
        r = pos - charge.pos
        r_mag = mag(r)
        E += k * charge.charge / r_mag**2 * norm(r)
    return E

# Create a grid of arrows representing the electric field
num_arrows = 15
arrow_length = 0.5
arrow_scale = 1e-8
x_vals = [L * i / (num_arrows-1) - L/2 for i in range(num_arrows)]
y_vals = [L * i / (num_arrows-1) - L/2 for i in range(num_arrows)]
z_vals = [L * i / (num_arrows-1) - L/2 for i in range(num_arrows)]
arrows = []
for x in x_vals:
    for y in y_vals:
        for z in z_vals:
            pos = vector(x, y, z)
            E = E_field(pos)
            E_mag = mag(E)
            if E_mag > 0:
                arrow_obj = arrow(pos=pos, axis=E*arrow_scale*arrow_length/E_mag, shaftwidth=0.05, color=color.green)
                arrows.append(arrow_obj)

# Define the Gaussian surface
surface = box(pos=vector(0,0,0), size=vector(L,L,L), opacity=0.2, color=color.blue)

# Define a function to update the Gaussian surface based on the electric field
def update_surface():
    for i, x in enumerate(x_vals):
        for j, y in enumerate(y_vals):
            for k, z in enumerate(z_vals):
                pos = vector(x, y, z)
                E = E_field(pos)
                E_mag = mag(E)
                if E_mag > 0:
                    surface.opacity = min(0.2, E_mag / 1e10)
                else:
                    surface.opacity = 0

# Define a function to move the rod with the mouse
def move_rod(evt):
    rod_pos.x = evt.pos.x
    for charge in charges:
        charge.pos = charge.pos + vector(evt.pos.x - charge.pos.x, 0, 0)
    update_arrows()
    update_surface()

# Define a function to update the arrows based on the new rod position
def update_arrows():
    for arrow_obj in arrows:
        pos =arrow_obj.pos
    E = E_field(pos)
    E_mag = mag(E)
    if E_mag > 0:
      arrow_obj.axis = E*arrow_scale*arrow_length/E_mag
    else :
        arrow_obj.axis = vector(0,0,0)

#Bind the move_rod function to the scene's mousemove event

scene.bind('mousemove', move_rod)

#Update the arrows and surface initially

update_arrows()
update_surface()

#Run the simulation

while True:
  rate(30)