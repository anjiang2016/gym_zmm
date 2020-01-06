from gym.envs.classic_control import rendering
import pdb
import time


screen_width = 600
screen_height = 400


length=0.5
x_threshold=2.4
world_width = x_threshold*2
scale = screen_width/world_width
carty = 200 # TOP OF CART
polewidth = 10.0
polelen = scale * (2 * length)
cartwidth = 50.0
cartheight = 30.0

cartwidth=200
cartheight=100

viewer = rendering.Viewer(screen_width, screen_height)
l,r,t,b = -cartwidth/2, cartwidth/2, cartheight/2, -cartheight/2
l+=screen_width/2
r+=screen_width/2
t+=screen_height/2
b+=screen_height/2

axleoffset =cartheight/4.0
cart = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
carttrans = rendering.Transform()
cart.add_attr(carttrans)
#viewer.add_geom(cart)

#polewidth=30
#poleheight=50
#polelen=20
#carty=300


l,r,t,b = -polewidth/2,polewidth/2,polelen-polewidth/2,-polewidth/2
l+=screen_width/2
r+=screen_width/2
t+=screen_height/2
b+=screen_height/2
pole = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
pole.set_color(.8,.6,.4)
poletrans = rendering.Transform(translation=(0, axleoffset))
pole.add_attr(poletrans)
pole.add_attr(carttrans)
#viewer.add_geom(pole)

axle = rendering.make_circle(polewidth/2)
axle.add_attr(poletrans)
axle.add_attr(carttrans)
axle.set_color(.5,.5,.8)
#viewer.add_geom(axle)




track = rendering.Line((0,carty), (screen_width,carty))
track.set_color(0,0,0)
#viewer.add_geom(track)

def line(viewer,p1_x,p1_y,p2_x,p2_y):
    #track = rendering.Line((0,carty), (screen_width,carty))
    track = rendering.Line((p1_x,p1_y), (p2_x,p2_y))
    track.set_color(0,0,0)
    viewer.add_geom(track)
    return viewer

viewer = line(viewer,100,100,250,100)
viewer = line(viewer,100,150,250,150)
viewer = line(viewer,100,200,250,200)
viewer = line(viewer,100,250,250,250)

viewer = line(viewer,100,100,100,250)
viewer = line(viewer,150,100,150,250)
viewer = line(viewer,200,100,200,250)
viewer = line(viewer,250,100,250,250)


#pdb.set_trace()
mode='human'
viewer.render(return_rgb_array = mode=='rgb_array')


if __name__=="__main__":
   while 1:
     input()
     time.sleep(0.1)
   print("0")
