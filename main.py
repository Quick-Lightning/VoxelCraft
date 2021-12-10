from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
from perlin_noise import PerlinNoise
from game_utils import *
from ursina.shaders import lit_with_shadows_shader

worldseed = random.randint(1000, 9999)
noise = PerlinNoise(octaves=3, seed=worldseed)

grasstextures = ["assets/grass.png", "assets/Screenshot 2021-12-02 232322.png"]
leavestextures = ["assets/leaves1.png", "assets/leaves2.png", "assets/leaves3.png", "assets/leaves1.png", "assets/leaves1.png"]

app = Ursina()
pickedblock = "grass"



class Voxel(Button):
    def __init__(self, **kwargs):
        super().__init__()
        self.parent = scene
        self.position = (0, 0, 0)
        self.model = 'cube'
        self.origin_y = 0.5
        self.scale_y = 1
        self.scale_x = 1
        self.shader = lit_with_shadows_shader
        self.texture = 'assets/Screenshot 2021-12-02 232322.png'
        self.color = color.color(0, 0, random.uniform(0.9, 1))
        self.highlight_color = color.light_gray
        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                if self.texture == "assets/bedrock.png":
                    pass
                else:
                    destroy(self)
            if key == "right mouse down":
                if pickedblock == "grass":
                    voxel = Voxel(position=(self.position + mouse.normal),
                                  texture=grasstextures[random.randrange(-1, 1)])
                elif pickedblock == "assets/stone.png":
                    voxel = Voxel(position=(self.position + mouse.normal),
                                  texture=pickedblock)
                elif pickedblock == "assets/copper_block":
                    voxel = Voxel(position=(self.position + mouse.normal), texture=pickedblock)
                elif pickedblock == "assets/diamond_block":
                    voxel = Voxel(position=(self.position + mouse.normal), texture=pickedblock)
class Inventory(Entity):
    def __init__(self):
        super().__init__()
        self.parent=camera.ui
        self.model="quad"
        self.scale_x=0.7
        self.scale_y=0.2
        self.x=-0.37
        self.z=-3
        self.y=-0.4
        self.texture="assets/invgrass.png"
    def update(self):
        if pickedblock == "grass":
            self.texture="assets/invgrass.png"
        elif pickedblock == "assets/stone.png":
            self.texture="assets/invstone.png"
        elif pickedblock == "assets/copper_block":
            self.texture="assets/invcu.png"
        elif pickedblock == "assets/diamond_block":
            self.texture="assets/invdiamant.png"

def update():
    global worldx
    global SkyState
    global worldz
    global pickedblock
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    if held_keys["2"]:
        pickedblock = "assets/stone.png"
    elif held_keys["1"]:
        pickedblock = "grass"
    elif held_keys["3"]:
        pickedblock = "assets/copper_block"
    elif held_keys["4"]:
        pickedblock = "assets/diamond_block"
    if FPC.y < -11:
        FPC.y = 5
        FPC.x = int(worldx) / 2
        FPC.z = int(worldz) / 2


FPC = FirstPersonController()
print("VoxelCraft v1.1.3")
print("")
worldx = "16"
worldz = "16"
voxels = []
print(f"World seed:{worldseed}")
for z in range(int(worldz)):
    for x in range(int(worldx)):
        y = noise([x * .02, z * .03])
        y = math.floor(y * 7.1)
        if y < -1:
            voxel = Voxel(position=(x, y, z), texture="assets/sky.png", color=color.rgba(1, 94, 105, random.randrange(197, 241)),
                          collider=None)
            voxel1 = Voxel(position=(x, y - 1, z), texture="assets/bedrock.png",
                           color=color.color(0, 0, random.uniform(0.9, 1)), collider="cube")
        else:
            if random.randrange(1, 2 * (int(worldx) + int(worldz))) == (int(worldx) + int(worldz)) / 2:
                voxel = Voxel(position=(x, y, z), texture="assets/treetrunk.png",
                              color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel1 = Voxel(position=(x, y + 1, z), texture="assets/treetrunk.png",
                               color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel2 = Voxel(position=(x, y + 2, z), texture="assets/treetrunk.png",
                               color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel3 = Voxel(position=(x, y + 3, z), texture="assets/treetrunk.png",
                               color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel4 = Voxel(position=(x, y + 4, z), texture=leavestextures[random.randrange(0, 4)],
                               color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel5 = Voxel(position=(x + 1, y + 4, z), texture=leavestextures[random.randrange(0, 4)],
                               color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel6 = Voxel(position=(x, y + 4, z + 1), texture=leavestextures[random.randrange(0, 4)],
                               color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel7 = Voxel(position=(x - 1, y + 4, z), texture=leavestextures[random.randrange(0, 4)],
                               color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel8 = Voxel(position=(x, y + 4, z - 1), texture=leavestextures[random.randrange(0, 4)],
                               color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel9 = Voxel(position=(x, y + 5, z), texture=leavestextures[random.randrange(0, 4)],
                               color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel10 = Voxel(position=(x + 1, y + 4, z + 1), texture=leavestextures[random.randrange(0, 4)],
                                color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel11 = Voxel(position=(x + 1, y + 4, z - 1), texture=leavestextures[random.randrange(0, 4)],
                                color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel12 = Voxel(position=(x - 1, y + 4, z + 1), texture=leavestextures[random.randrange(0, 4)],
                                color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel13 = Voxel(position=(x - 1, y + 4, z - 1), texture=leavestextures[random.randrange(0, 4)],
                                color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel14 = Voxel(position=(x + 1, y + 5, z), texture=leavestextures[random.randrange(0, 4)],
                                color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel15 = Voxel(position=(x - 1, y + 5, z), texture=leavestextures[random.randrange(0, 4)],
                                color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel16 = Voxel(position=(x, y + 5, z + 1), texture=leavestextures[random.randrange(0, 4)],
                                color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel17 = Voxel(position=(x, y + 5, z - 1), texture=leavestextures[random.randrange(0, 4)],
                                color=color.color(0, 0, random.uniform(0.9, 1)))
                voxel18 = Voxel(position=(x, y + 6, z), texture=leavestextures[random.randrange(0, 4)],
                                color=color.color(0, 0, random.uniform(0.9, 1)))
            else:
                voxel = Voxel(position=(x, y, z), texture=grasstextures[random.randrange(-1, 1)],
                              color=color.color(0, 0, random.uniform(0.9, 1)))
            while y > -2:
                voxels.append(
                    Voxel(position=(x, y - 1, z), texture="assets/stone.png",
                          color=color.color(0, 0, random.uniform(0.9, 1))))
                y -= 1
hand = Hand()
inventory=Inventory()
sky = Sky()
app.run()
