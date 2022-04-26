from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

from textures import *


block_pick = 1

def update():
  global block_pick
  if held_keys['1']: block_pick=1
  if held_keys['2']: block_pick=2
  if held_keys['3']: block_pick=3
  if held_keys['4']: block_pick=4
  
  #hand
  if held_keys['left mouse'] or held_keys['right mouse']:
    hand.active()
  else:
    hand.passive()



class Voxell(Button):
  def __init__(self, position = (0,0,0), texture=grass_texture):
    super().__init__(
      parent=scene,
      position=position,
      model='assets/block',
      origin_y=0.5,
      texture=texture,
      color=color.color(0,0,random.uniform(0.9,1)),
      
      scale=0.5)


  def input(self, key):
    print(key)
    if self.hovered:
      if key == 'left mouse down':
        if block_pick == 1: voxel = Voxell(position= self.position + mouse.normal, texture=grass_texture)
        if block_pick == 2: voxel = Voxell(position= self.position + mouse.normal, texture=dirt_texture)
        if block_pick == 3: voxel = Voxell(position= self.position + mouse.normal, texture=stone_texture)
        if block_pick == 4: voxel = Voxell(position= self.position + mouse.normal, texture=brick_texture)
        
      if key == 'right mouse down':
        destroy(self)

      if key == 'escape':
        sys.exit()

class Sky(Entity):
  def __init__(self):
    super().__init__(
      parent=scene,
      model='sphere',
      texture=sky_texture,
      scale=150,
      double_sided=True
    )

class Hand(Entity):
  def __init__(self):
    super().__init__(
      parent=camera.ui,
      model='assets/arm',
      texture=arm_texture,
      scale=0.2,
      rotation=Vec3(150,-10,0),
      position=Vec2(0.4,-0.6)
    )
  def active(self):
    self.position = Vec2(0.3,-0.5)
  
  def passive(self):
    self.position=Vec2(0.4,-0.6)

for z in range(20):
  for x in range(20):
    Voxell(position=Vec3(x,0,z))


player = FirstPersonController()
hand = Hand()
sky = Sky()
app.run()