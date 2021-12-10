from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
from perlin_noise import PerlinNoise
import time
from ursina.shaders import lit_with_shadows_shader
class Sky(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.parent = scene
        self.position = (16, 0, 16)
        self.model = 'sphere'
        self.scale = 221
        self.shader = lit_with_shadows_shader
        self.texture = 'assets/sky.png'
        self.double_sided = True
        for key, value in kwargs.items():
            setattr(self, key, value)

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            shader=lit_with_shadows_shader,
            texture=load_texture('assets/arm_texture.png'),
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6))

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)
class Inventory(Entity):
    def __init__(self):
        super().__init__()
        self.parent=camera.ui
        self.model="quad"
        self.scale_x=0.7
        self.scale_y=0.1
        self.x=-0.37
        self.z=-3
        self.y=-0.4
        self.texture="assets/inventorytest.png"

