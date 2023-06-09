###################################################
# THE ADVENTURES OF PAUL SOURCE CODE              #
# If used, give credit                            #
# ( Python 3.11.3 )                               #
#                                                 #
# I'm just not gonna fucking bother with docs     #
# Also, why do you event WANT to look here?       #
#                                                 #
# This code was tested on Python 3.11.1           #
# with an intel i3 10105F and a GTX 1050 TI       #
# Am i trying to flex my hardawre? No. it's shit. #
# If it don't work on your machine, go cry abt it #
###################################################

# Map size Max 1024x1024, else too much lag
# Do you like spaghetti? You'll get plenty here

import pygame
import os
import time
import json
from pynput.keyboard import Key
from math import *
import sys
import tracemalloc
import numpy
import pycparser
import keyboard
import numpy
import moderngl
import pymsgbox
import cython
import traceback
import datetime
import time
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import logging
import wmi
from array import array
from win32api import GetSystemMetrics
import shutil
import psutil
import win32com
import time
import log











##################
# Initialization #
##################

tracemalloc.start()

pycparser.CParser()


os.system('cls')

# If the program is compiled, change the directory to where the assets are located
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
else:
	os.chdir(os.path.split(__file__)[0])

appdir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', '.taop')
date_time = str(datetime.datetime.now()).replace(' ', '_')

logObject = log.LogObject(log.generate_filename(appdir))

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.font.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

pygame.mouse.set_visible(False)
pygame.mixer.set_num_channels(32)
#set variables
# for positions, tick n' stuff
mode = 'title'
nextargs = ''
emptymode = False
tick = True
frameCount = 0
logox = 0
scroll = 0
i = 5
startbi = 0
rpgbi = 0
coinbi = 0
logoy = 160
playerRun = False
hasYoshi = False
backX = 0
backY = 0
titlescreen = True
direction = '0'
mwframe = 0
mwframeupdate = 0
keydown = False
savefile = 0
enter = False
continuefade = True
joybuttonspressed = {}
frames = 0
dt = 0
shaderMemory = {}
playedfilemusic = False
buttonsPressed = []
fileselpos = [0, 1]
canpastefile = False

textdata = {}
scrollimgdata = {}
scrolly = 0
showtextdata = {}
pausetimer = 0
loadpaulfootup = False
loadpaulfootupconf = False
loadpaulfootupconf2 = False
loadpaulfootupconf3 = False

w = False
a = False
s = False
d = False

enablemouse = False
titlefadeout = False

buttonData = {}
currentcalledbutton = 0
introplayed = False
ldgamex = -801
savedata = {}
paused = False
screenUpdate = True
soundtracks = {}

disclaimer = ''
consoleText = ''
mapname = 'None'

mwi = 0

coinsi = 0

introcoini = 0

saveanimi = 0

sleepanimi = 0

#variables to do with moving / animation based on FPs
delta = 1
tick30 = 0
lastTick30 = 0

#debug stuff
debug = False
debugSettings = [True, True, True, True, True, True, True, True, True, True, True, 8]

#Map Stuff
mapSize = (0, 0)
mapData = [0, 0]
maxMap = [1, 1]
loadedMap = None

#shader stuff
shaderFrames = {'meth': 0}
shaderTime = 0
luma = 1.0

#item stuff
meth = False
methTimer = 0

# CPU Control Stuff
cpuMode = 1

# Setting stuff
enableSettings = False

#ending stuff
endingData = {}

# Get Info about System / Environment ( Most of the Start time is this shit )
sdlt = pygame.get_sdl_version()
sdlv = f'{sdlt[0]}.{sdlt[1]}.{sdlt[2]}'
ttft = pygame.font.get_sdl_ttf_version()
sdlttfv = f'{ttft[0]}.{ttft[1]}.{ttft[2]}'
pgv = pygame.version.ver
computer = wmi.WMI()
os_info = computer.Win32_OperatingSystem()[0]
gpu = computer.Win32_VideoController()[0].Name
cpu = computer.Win32_Processor()[0].Name
ram = float(os_info.TotalVisibleMemorySize) / 1048576
operatingsys = f'{os_info.Name.encode("utf-8").split(b"|")[0].decode("utf-8")}({" ".join([os_info.Version, os_info.BuildNumber])})'
pyv = f'{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}'
starttime = t1 = time.time()
introtheme = pygame.mixer.Sound(os.path.join('assets', 'title', '0.mp3'))
titletheme = pygame.mixer.Sound(os.path.join("assets", "title", "main.mp3"))
popsfx = pygame.mixer.Sound(os.path.join("assets", "ldsave", "pop.mp3"))
settingtheme = pygame.mixer.Sound(os.path.join('assets', 'title', 'settings.mp3'))
WIDTH = 800
HEIGHT = 600
FPS = 30
















##################
# Animation Data #
##################

introcoin = array('h', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 3, \
			 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 0, 0, 0, 0, 0])
startbounce = array('h', [-50, -30, -10, 10, 30, 50, 70, 90, 110, 130, 150, 160, 155, 150, 145, 140, 135, 130, 132, 134, 136, 138, 140, 142, 146\
			   , 150, 155, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 151, 151, 152, 152, 153, 154, 155, 156, 158, 160])
rpgbounce = array('h', [-180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, \
			 -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, 
-180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, -180, \
	-180, -180, -180, -180, -180, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, \
		220, 240, 260, 270, 265, 260, 255, 250, 245, 240, 242, 244, 246, 250, 255, 260, 265, 264, 263, 262, 261, 260, 259, 258, 257, \
			256, 255, 256, 256, 257, 257, 258, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270])
coinbounce = array('h', [-30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, \
			  -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, \
				-30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, \
					-30, -30, -30, -30, -30, 
-30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, \
	-30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -20, -10, -0, -10])

walkAnimation = array('h', [0, 0, 1, 1, 2, 2, 3, 3, 0, 0, 1, 1, 2, 2, 3, 3])

mousewiggl = [[0, 0], [1, -1], [2, -2], [3, -2], [4, -1], [5, 0], [5, 1], [4, 2], [3, 3], [2, 3], [1, 2], [0, 1], [0, 0], [-1, -1], \
			  [-2, -2], [-3, -2], [-4, -1], [-5, 0], [-5, 1], [-4, 2], [-3, -3], [-2, -3], [-1, -2], [-1, -1], [0, -1], [0, 0]]

sleepanim = array('h', [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, \
	     13, 13])

saveanim = array('h', [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, \
			12, 12, 13, 13])

coinbshine = array('h', [10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, \
			  20, 20, 21, 21, 22, 22, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, \
				10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])

with open(os.path.join(appdir, 'options.json'), 'r') as f:
	fullscreen = json.load(f)['fullscreen']
	debugSettings[1] = False



















######################
# Initialize Display #
######################

#Window stuff
if fullscreen:
	screensize = (GetSystemMetrics(0), GetSystemMetrics(1))
	screenheight = screensize[1]
	screenwidth = round((800 / 600) * screenheight)
	screenrest = screensize[0] - screenwidth
	screenresthalf = round(screenrest / 2)
	modernGLsurface = pygame.display.set_mode(screensize, pygame.SRCALPHA | pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.OPENGL, 32)
	WIN = pygame.Surface(screensize, pygame.SRCALPHA | pygame.DOUBLEBUF | pygame.HWSURFACE)
	noShaderSurface = pygame.Surface(screensize, pygame.SRCALPHA | pygame.DOUBLEBUF | pygame.HWSURFACE)
	# VERY IMPORTANT!!! RGB 0|0|0 is transparency (For black use 10|10|10)
	overCurtSurface = pygame.Surface((800, 600), pygame.SRCALPHA | pygame.DOUBLEBUF | pygame.HWSURFACE)
	ctx = moderngl.create_context()
	bitmap_tex = None
	ctx.enable(moderngl.BLEND)
	pausescreensurface = pygame.Surface((800, 600), pygame.SRCALPHA | pygame.DOUBLEBUF | pygame.HWSURFACE)

else:
	screensize = (800, 600)
	screenheight = 600
	screenwidth = 800
	screenrest = 0
	screenresthalf = 0

	modernGLsurface = pygame.display.set_mode(screensize, pygame.SRCALPHA | pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.OPENGL, 32)
	WIN = pygame.Surface(screensize, pygame.SRCALPHA | pygame.DOUBLEBUF | pygame.HWSURFACE)
	noShaderSurface = pygame.Surface(screensize, pygame.SRCALPHA | pygame.DOUBLEBUF | pygame.HWSURFACE)
	# VERY IMPORTANT!!! RGB 0|0|0 is transparency (For black use 10|10|10)
	overCurtSurface = pygame.Surface((800, 600), pygame.SRCALPHA | pygame.DOUBLEBUF | pygame.HWSURFACE)
	ctx = moderngl.create_context()
	bitmap_tex = None
	ctx.enable(moderngl.BLEND)
	pausescreensurface = pygame.Surface((800, 600), pygame.SRCALPHA | pygame.DOUBLEBUF | pygame.HWSURFACE)

screenx = screensize[0] / 800
screeny = screensize[1] / 600

clock = pygame.time.Clock()

quad_buffer = ctx.buffer(data=array('f', [
	-1.0, 1.0, 0.0, 0.0,
	1.0, 1.0, 1.0, 0.0,
	-1.0, -1.0, 0.0, 1.0,
	1.0, -1.0, 1.0, 1.0,
]))














###########
# Shaders #
###########

# GLSL Functions for Converting RGB to HSV and back
# vec3 rgb2hsv(vec3 c) {
#     vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
#     vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
#     vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));

#     float d = q.x - min(q.w, q.y);
#     float e = 1.0e-10;
#     return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
# }

# vec3 hsv2rgb(vec3 c) {
#     vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
#     vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
#     return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
# }

class shaderClass:
	def __init__(self):
		pts = os.path.join('assets', 'shaders')
		with open(os.path.join(pts, 'default_vertex.glsl'), 'r') as f:
			self.vert = f.read()
		with open(os.path.join(pts, 'meth.glsl'), 'r') as f:
			self.whirly = f.read()
		with open(os.path.join(pts, 'no_shader.glsl'), 'r') as f:
			self.no_shader = f.read()
		with open(os.path.join(pts, 'no_shader2.glsl'), 'r') as f:
			self.no_shader2 = f.read()
		with open(os.path.join(pts, 'watuh.glsl'), 'r') as f:
			self.watuh = f.read()
		
	def program(self, frag):
		program = ctx.program(vertex_shader=shaders.vert, fragment_shader=frag)
		render_object = ctx.vertex_array(program, [(quad_buffer, '2f 2f', 'vert', 'texcoord')])
		return [program, render_object]

shaders = shaderClass()

shader = shaders.program(shaders.no_shader2)
noshader = shaders.program(shaders.no_shader)











#####################
# Scaling Functions #
#####################

@cython.cfunc
def scale2x(image):
	x = image.get_width() * 2
	y = image.get_height() * 2
	image = pygame.transform.scale(image, (x, y))
	return image

@cython.cfunc
def scale4x(image):
	x = image.get_width() * 4
	y = image.get_height() * 4
	image = pygame.transform.scale(image, (x, y))
	return image














#################
# Load stuff in #
#################

bgscroll = [0, 0, 0, 0, 0, 0]
bg0 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'backgrounds', '0.png')).convert_alpha(), (1600, 600))
bg1 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'backgrounds', '1.png')).convert_alpha(), (1600, 600))
bg2 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'backgrounds', '2.png')).convert_alpha(), (1600, 600))
bg3 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'backgrounds', '3.png')).convert_alpha(), (1600, 600))
bg4 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'backgrounds', '4.png')).convert_alpha(), (1600, 600))
bg5 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'backgrounds', '5.png')).convert(), (1600, 600))
mousecursor = scale2x(pygame.image.load(os.path.join('assets', 'cursors', '0.png')).convert_alpha())
lpaula = scale2x(pygame.image.load(os.path.join('assets', 'other', '5.png')).convert_alpha())
lpaulb = scale2x(pygame.image.load(os.path.join('assets', 'other', '4.png')).convert_alpha())
ldbg = scale2x(pygame.image.load(os.path.join('assets', 'other', '6.png')).convert_alpha())
pausebg = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'pausescreen', '0.png')).convert_alpha(), (372, 600))
pausecont = scale4x(pygame.image.load(os.path.join('assets', 'pausescreen', '1.png')).convert_alpha())
pausesett = scale4x(pygame.image.load(os.path.join('assets', 'pausescreen', '2.png')).convert_alpha())
pauseload = scale4x(pygame.image.load(os.path.join('assets', 'pausescreen', '3.png')).convert_alpha())
pausequitg = scale4x(pygame.image.load(os.path.join('assets', 'pausescreen', '4.png')).convert_alpha())
settbg = scale2x(pygame.image.load(os.path.join('assets', 'settings', 'bg.png')))
ldsavbg = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ldsave', 'background.png')).convert_alpha(), (800, 600))
ldsavslots = scale2x(pygame.image.load(os.path.join('assets', 'ldsave', 'slots.png')).convert_alpha())
ldsavthinghy = scale2x(pygame.image.load(os.path.join('assets', 'ldsave', 'arrow.png')).convert_alpha())
ldpastebutton = scale2x(pygame.image.load(os.path.join('assets', 'ldsave', 'nopaste.png')).convert_alpha())
tlogo = pygame.image.load(os.path.join('assets', 'title', '1.png')).convert_alpha()
trpg = pygame.image.load(os.path.join('assets', 'title', '7.png')).convert_alpha()
tlogo = scale2x(tlogo)
trpg = scale2x(trpg)
tcts = pygame.image.load(os.path.join('assets', 'title', '9.png')).convert_alpha()
tcts = scale2x(tcts)
thevoid = pygame.image.load(os.path.join('assets', 'other', '7.png')).convert_alpha()
fpsfont = pygame.font.Font(os.path.join('assets', 'font', 'mc.otf'), 16)
curtain = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'title', '8.png')).convert_alpha(), (800, 600))















#############
# Map Stuff #
#############

# Dialog class (Litarally the ENTIRE code that handles the dialogs, don't you fucking dare remove)
class dialog:
	def __init__(self, file: str):
		with open(file) as f:
			code =  json.load(f)
		self.file = file
		self.code = code
		self.name = code['name']
		self.images = code['images']
		self.options = code['options']
		self.texts = code['texts']
		self.order = code['order']
		self.current_step = 0
		self.misc = {}
		self.current_image = pygame.Surface((32, 32))
		self.current_options = []
		self.text = ''
		self.mode = 0
	
	def step(self, option):
		new_code = self.code[option]
		self.code = new_code

	def update(self):
		code = self.order
		self.curent_image = pygame.image.load(self.images[code[0]]).convert_alpha()
		self.text = self.texts[code[1]]
		self.current_options = self.options[code[2]]
	
	def handle(self):
		pass

class mapoptions:
	CANTALK = 0
	ANIMATED = 2
	HASCOLLIDER = 3
	HASCOLLISIONS = 4

# Map object class (very important. These are the objects that are present on the map)
class mapobject:
	def __init__(self, graphics: list, position: list or tuple, hitbox_position: list or tuple, hitbox_size: list or tuple, shown: bool=True) -> None:
		self.graphics = graphics
		self.pos = list(position)
		self.rectX, self.rectY = hitbox_position
		self.hitW, self.hitH = hitbox_size
		self.rect = pygame.Rect(hitbox_position[0], hitbox_position[1], hitbox_size[0], hitbox_size[1])
		self.shown = shown
	
	def regenerate_collision(self) -> None:
		self.rectX, self.rectY = self.pos
		self.rect = pygame.Rect(self.rectX, self.rectY, self.hitW, self.hitH)

	def set_graphics(self, graphics: list) -> None:
		self.graphics = graphics

	def set_pos(self, x: int, y: int) -> None:
		self.pos = [x, y]
		self.regenerate_collision()
	
	def set_pos_list(self, position: list or tuple) -> None:
		self.pos = list(position)
	
	def move_x(self, amount: int) -> None:
		self.pos[0] += amount
	
	def move_y(self, amount: int) -> None:
		self.pos[1] += amount

# Map call (very a lot important, it is litterally the ENTIRE code that handles the map, which is like 99% of the gameplay)
class map:
	def __init__(self, name: str, background: pygame.Surface, objects: list):
		self.name = name
		self.bg = background
		self.surface = pygame.Surface(background.get_size())
		self.blank = pygame.Surface(background.get_size())
		self.savepoint = None
		self.objects = objects
		self.animationframe = 0
	
	def add_object(self, object: mapobject):
		self.objects.append(object)
		return len(self.objects)
	
	def remove_object(self, i)-> mapobject:
		return self.objects.pop(i)

	def clear_objects(self):
		self.objects = []

	def stepanimation(self):
		self.animationframe += 1
		if self.animationframe == 4:
			self.aniamtionframe = 0
	
	def clear_surface(self):
		self.surface = self.blank
	
	def save(self):
		self.savepoint = self
	
	def load(self):
		if not self.savepoint == None:
			self = self.savepoint

	def render(self):
		self.surface.blit(self.bg)
		for object in self.objects:
			x, y = object.pos
			w, h = object.graphics[self.animationframe].get_size()
			if (x < -w and x > 800) and (y < -h and y > 600):
				self.surface.blit(object.graphics[self.animationframe], (x, y))
		return self.surface

#

def genMapfromJson(file, requiredVersion="1.0"):
	with open(file, 'r') as f:
		data = json.load(f)
		f.close()
	if not data['mapVersion'] == requiredVersion:
		e = ValueError()
		e.add_note('Wrong map Version')
		raise e
	objects = []
	for object in data['objects']:
		objects.append(
			mapobject(
				[
					pygame.image.load(object['graphics'][0]).convert_alpha(),
					pygame.image.load(object['graphics'][1]).convert_alpha(),
					pygame.image.load(object['graphics'][2]).convert_alpha()
				],
				object['pos'],
				[
					object['pos'][0] + object['hitboxOffset'][0],
    				object['pos'][1] + object['hitboxOffset'][1]
				],
				object['hitboxSize'],
				True
			)
		)
	outputMap = map(
		data['mapName'],
		pygame.image.load(data['background']).convert_alpha(),
		objects
	)
	return outputMap

# lasafba














#############
# Functions #
#############

@cython.cfunc
def getx(image):
	isize = image.get_width() / 2
	scrsize = WIDTH / 2
	x = scrsize - isize
	return x

@cython.cfunc
def gety(image):
	isize = image.get_height() / 2
	scrsize = HEIGHT / 2
	y = scrsize - isize
	return y

@cython.cfunc
def getmiddle(image):
	x = getx(image)
	y = gety(image)
	pos = (x, y)
	return pos

def appdata():
	try:
		emptyoptions = {'firststart': True, 'fullscreen': True, 'memory': 2048}
		returnDir = os.getcwd()
		os.chdir(os.getenv('LOCALAPPDATA'))
		os.mkdir('.taop')
		os.chdir('.taop')
		os.mkdir('saves')
		with open('options.json', 'x') as f:
			json.dump(emptyoptions, f)
			f.close()
		with open(os.path.join('saves', '0.json'), 'x') as f:
			f.write('{}')
		with open(os.path.join('saves', '1.json'), 'x') as f:
			f.write('{}')
		with open(os.path.join('saves', '2.json'), 'x') as f:
			f.write('{}')
		os.mkdir('mods')
		os.mkdir('logs')
	except:
		pass
	os.chdir(returnDir)

@cython.cfunc
def leave():
	sys.exit()

@cython.cfunc
def makeShortcut(file, target, shortcutname='shortcut'):
	shell = win32com.client.Dispatch("WScript.Shell")
	shortcut = shell.CreateShortCut(os.path.join(file, f'{shortcutname}.lnk'))
	shortcut.Targetpath = target
	shortcut.WindowStyle = 1 # 7 - Minimized, 3 - Maximized, 1 - Normal
	shortcut.save()

@cython.cfunc
def writetosave(data):
	with open(os.path.join(appdir, 'options.json'), 'r') as f:
		options = json.load(f)
		f.close()
	options |= data
	with open(os.path.join(appdir, 'options.json'), 'w') as f:
		json.dump(options, f)
		f.close()

@cython.cfunc
def readfromsave():
	with open(os.path.join(appdir, 'options.json'), 'r') as f:
		options = json.load(f)
		f.close()
	return options

@cython.cfunc
def savestate(slot):
	backupData = globals()
	with open(os.path.join(appdir, 'savestates', slot, '.json'), 'w') as f:
		json.dump(backupData, f)
		f.close()

@cython.cfunc
def loadstate(slot):
	with open(os.path.join(appdir, 'savestates', slot, '.json'), 'r') as f:
		data = json.load(f)
		f.close()
	globals().update(data)

@cython.cfunc
def savegame(slot):
	backupData = globals()
	with open(os.path.join(appdir, 'saves', slot, '.json'), 'w') as f:
		json.dump(backupData, f)
		f.close()

@cython.cfunc
def loadgame(slot):
	with open(os.path.join(appdir, 'saves', slot, '.json'), 'r') as f:
		data = json.load(f)
		f.close()
	globals().update(data)

@cython.cfunc
def rstappdata():
	shutil.rmtree(appdir)
	appdata()

def loadEndings():
	global endingData, soundtracks
	endingData = {
		'button': scale2x(pygame.image.load(os.path.join('assets', 'endings', '0.png'))),
		'kahoot': {
			'img': pygame.transform.scale(pygame.image.load(os.path.join('assets', 'endings', 'kahoot.png')), (800, 600)),
			'start': pygame.mixer.Sound(os.path.join('assets', 'endings', 'kahoot_intro.mp3')),
			'loop': pygame.mixer.Sound(os.path.join('assets', 'endings', 'kahoot.mp3')),
			'intro': False
		}
	}
	soundtracks['sleep'] = [
		pygame.mixer.Sound(os.path.join('assets', 'music', 'sweep_intro.mp3')),
		pygame.mixer.Sound(os.path.join('assets', 'music', 'sweep.mp3')),
		False,
		False
	]

@cython.cfunc
def set_fullscreen():
	with open(os.path.join(appdir, 'options.json'), 'r') as f:
		data = json.load(f)
	with open(os.path.join(appdir, 'options.json'), 'w') as f:
		data['fullscreen'] = True
		json.dump(data, f)
	ctypes.windll.user32.MessageBoxW(0, f"Settings applied. Please restart the program now", "Restart", 0)

@cython.cfunc
def set_windowed():
	with open(os.path.join(appdir, 'options.json'), 'r') as f:
		data = json.load(f)
	with open(os.path.join(appdir, 'options.json'), 'w') as f:
		data['fullscreen'] = False
		json.dump(data, f)
	ctypes.windll.user32.MessageBoxW(0, f"Settings applied. Please restart the program now", "Restart", 0)

@cython.cfunc
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		absolute_path = os.path.join(sys._MEIPASS, relative)
	else:
		absolute_path = os.path.join(relative)
	return absolute_path

@cython.cfunc
def make_shaderprogram(vertex, fragment):
	program = ctx.program(vertex_shader=vertex, fragment_shader=fragment)
	render_object = ctx.vertex_array(program, [(quad_buffer, '2f 2f', 'vert', 'texcoord')])
	return [program, render_object]

@cython.cfunc
def surf_to_texture(surf):
	tex = ctx.texture(surf.get_size(), 4)
	tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
	tex.swizzle = 'BGRA'
	tex.write(surf.get_view('1'))
	return tex

@cython.cfunc
def grab(x, y, w, h, surf=WIN):
	rect = pygame.Rect(x, y, w, h)
	sub = surf.subsurface(rect)
	screenshot = pygame.Surface((w, h))
	screenshot.blit(sub, (0, 0))
	return screenshot

@cython.cfunc
def text(name: str, x: int, text: str, scrollspeed: int):
	global textdata
	font = pygame.font.Font(os.path.join('assets', 'texts', 'font.ttf'), 16)
	lines = text.split('\n')
	i = 0
	lineonscreen = False
	if not name in textdata.keys():
		textdata[name] = [0, 0, []]
	for line in lines:
		calpos = i * 16
		if calpos > -16 and calpos < 600:
			if 'ix'in line:
				img = line[2:]
				image = pygame.image.load(os.path.join('assets', 'texts', 'images', img)).convert_alpha()
				WIN.blit(image, [x, calpos + textdata[name][0] + 600])
				if not img in textdata[2]:
					textdata[name][1] += 0
					textdata[name][2].append(img)
				pass
			linerendered = font.render(line, True, (255, 255, 255))
			WIN.blit(linerendered, [x, calpos + textdata[name][0] + 600])
			lineonscreen = True
		textdata[name][0] += scrollspeed
		i += 1
		if not lineonscreen:
			textdata.pop(name)
			return True

@cython.cfunc
def scrollimage(image, name, yspeed, x=0, repeat=False):
	global scrollimgdata
	if not name in scrollimgdata:
		scrollimgdata[name] = 0
	WIN.blit(image, [x, scrollimgdata[name][1] + 600])
	scrollimgdata[name] += yspeed
	if repeat:
		if scrollimgdata[name] - yspeed > 0 - yspeed:
			scrollimgdata[name] -= image.get_height()
	else:
		if scrollimgdata[name] < 0 - image.get_height():
			scrollimgdata.pop(name)
			return True
	return False

class controls:
	def w():
		global playerRun, backY, direction, mwframe, mwframeupdate, mapData, mwi
		direction = '3'
		if mwframeupdate < 3:
			mwframeupdate += 1
		else:
			mwframeupdate = 0
		if mwframeupdate == 3:
			if mwi < 15:
				mwi += 1
			else:
				mwi = 0
		backY += debugSettings[11]
		if playerRun:
			backY += 4

	def s():
		global playerRun, backY, direction, mwframe, mwframeupdate, mapData, mwi
		direction = '0'
		if mwframeupdate < 3:
			mwframeupdate += 1
		else:
			mwframeupdate = 0
		if mwframeupdate == 3:
			if mwi < 15:
				mwi += 1
			else:
				mwi = 0
		backY -= debugSettings[11]
		if playerRun:
			backY -= 4

	def a():
		global playerRun, backX, direction, mwframe, mwframeupdate, mapData, mwi
		direction = '1'
		if mwframeupdate < 3:
			mwframeupdate += 1
		else:
			mwframeupdate = 0
		if mwframeupdate == 3:
			if mwi < 15:
				mwi += 1
			else:
				mwi = 0
		backX += debugSettings[11]
		if playerRun:
			backX += 4

	def d():
		global playerRun, backX, direction, mwframe, mwframeupdate, mapData, mwi
		direction = '2'
		if mwframeupdate < 3:
			mwframeupdate += 1
		else:
			mwframeupdate = 0
		if mwframeupdate == 3:
			if mwi < 15:
				mwi += 1
			else:
				mwi = 0
		backX -= debugSettings[11]
		if playerRun:
			backX -= 4

@cython.cfunc
def handleMouse():
	global mousetimer, mousewiggl
	if enablemouse:
		return mousecursor
	return pygame.Surface((1, 1))

@cython.cfunc
def caclMpos():
	screensize = (GetSystemMetrics(0), GetSystemMetrics(1))
	screenheight = screensize[1]
	screenwidth = round((800 / 600) * screenheight)
	screenrest = screensize[0] - screenwidth
	screenresthalf = round(screenrest / 2)
	globals().update(locals())

@cython.cfunc
def caclLpos():
	screensize = (GetSystemMetrics(0), GetSystemMetrics(1))
	screenheight = screensize[1]
	screenwidth = round((800 / 600) * screenheight)
	screenrest = 0
	screenresthalf = 0
	globals().update(locals())

@cython.cfunc
def caclRpos():
	screensize = (GetSystemMetrics(0), GetSystemMetrics(1))
	screenheight = screensize[1]
	screenwidth = round((800 / 600) * screenheight)
	screenrest = screensize[0] - screenwidth
	screenresthalf = screenrest
	globals().update(locals())




















############################
# Memory and Appdata Stuff #
############################

# make sure appdata folder is present, if not, make one
if not os.path.isdir(appdir):
	print('Generating appdata folder')
	appdata()

pcram = psutil.virtual_memory().total

ramlimit = 0

mousetimer = 0

















####################
# Visual Functions #
####################

@cython.cfunc
def titlebackground():
	global bgscroll
	WIN.blit(bg5, (bgscroll[5], 0))
	WIN.blit(bg5, (bgscroll[5] - 1600, 0))
	WIN.blit(bg5, (bgscroll[5] + 1600, 0))
	WIN.blit(bg4, (bgscroll[4], 0))
	WIN.blit(bg4, (bgscroll[4] - 1600, 0))
	WIN.blit(bg4, (bgscroll[4] + 1600, 0))
	WIN.blit(bg3, (bgscroll[3], 0))
	WIN.blit(bg3, (bgscroll[3] - 1600, 0))
	WIN.blit(bg3, (bgscroll[3] + 1600, 0))
	WIN.blit(bg2, (bgscroll[2], 0))
	WIN.blit(bg2, (bgscroll[2] - 1600, 0))
	WIN.blit(bg2, (bgscroll[2] + 1600, 0))
	WIN.blit(bg1, (bgscroll[1], 0))
	WIN.blit(bg1, (bgscroll[1] - 1600, 0))
	WIN.blit(bg1, (bgscroll[1] + 1600, 0))
	WIN.blit(bg0, (bgscroll[0], 0))
	WIN.blit(bg0, (bgscroll[0] - 1600, 0))
	WIN.blit(bg0, (bgscroll[0] + 1600, 0))
	bgscroll[0] += 6
	bgscroll[1] += 5
	bgscroll[2] += 4
	bgscroll[3] += 3
	bgscroll[4] += 2
	bgscroll[5] += 1
	if bgscroll[0] > 1600:
		bgscroll[0] = -1600
	if bgscroll[1] > 1600:
		bgscroll[1] = -1600
	if bgscroll[2] > 1600:
		bgscroll[2] = -1600
	if bgscroll[3] > 1600:
		bgscroll[3] = -1600
	if bgscroll[4] > 1600:
		bgscroll[4] = -1600
	if bgscroll[5] > 1600:
		bgscroll[5] = -1600
	if bgscroll == [0, 0, 0, 0, 0, 0]:
		pygame.quit()

@cython.cfunc
def button(pos: tuple, image_idle: pygame.Surface, image_hovering: pygame.Surface, surface=noShaderSurface):
	global event, currentcalledbutton
	xpos, ypos = pos
	output = 0
	idle_width, idle_height = image_idle.get_size()
	mousepos = pygame.mouse.get_pos()
	mx, my = mousepos
	#screenwidth = GetSystemMetrics(0) - screenrest
	if fullscreen:
		rect = pygame.Rect(((xpos * (screenwidth / 800)), ypos * (screenheight / 600)), ((idle_width * (screenwidth / 800)), (idle_height * (screenheight / 600))))
	else:
		rect = pygame.Rect(xpos, ypos, idle_width, idle_height)
	if not rect.collidepoint(mx, my):
		surface.blit(image_idle, [xpos, ypos])
		output = 0
	else:
		if pygame.mouse.get_pressed()[0]:
			output = 2
			time.sleep(0.1)
		else:
			surface.blit(pygame.transform.scale(image_hovering, (image_hovering.get_width() + 10, image_hovering.get_height() + 10)), [xpos - 5, ypos - 5])
			output = 1
	buttonData[currentcalledbutton] = output
	currentcalledbutton += 1
	return output

class oldmap:
	@cython.cfunc
	def __init__(self, map):
		global mapSize
		self.map = scale2x(pygame.image.load(map).convert())
		with open(os.path.splitext(map)[0] + '.json', 'r') as f:
			self.data = json.load(f)
			f.close()
		mapSize = self.map.get_size()
	
	@cython.cfunc
	def update(self):
		# 370, 100
		global direction, mwframe, backX, backY, mapname, mapSize
		m = pygame.image.load(os.path.join('assets', 'animations', 'mario', 'walk', direction + str(int(walkAnimation[mwi])) + '.png')).convert_alpha()
		m = scale2x(m)
		font = pygame.font.Font(os.path.join('assets', 'font', 'world.ttf'), 32)
		data = self.data
		mapname = data['name']
		text = font.render(mapname, False, (248, 248, 248))
		stop_rects = []
		for poss in data['collision']:
			collision_dect = pygame.rect.Rect(poss[0] + backX, poss[1] + backY, poss[2] - (poss[0] + backX), poss[3] - (poss[1] + backY))
			stop_rects.append(collision_dect)
		try:
			back = scale2x(pygame.image.load(data['background'])).convert_alpha()
			WIN.blit(back, [backX, backY])
		except:
			pass
		map = self.map
		WIN.blit(map, [backX, backY])
		if debugSettings[4]:
			WIN.blit(m, getmiddle(m))
		try:
			map2 = scale2x(pygame.image.load(data['2layer']).convert_alpha())
			WIN.blit(map2, (0, 0))
		except:
			pass
		WIN.blit(text, [120, 100])

@cython.cfunc
def loadscreen():
	global loadpaulfootup, loadpaulfootupconf, loadpaulfootupconf2, loadpaulfootupconf3
	WIN.fill((0, 0, 0))
	loadpaulfootup = not loadpaulfootup
	if loadpaulfootup:
		loadpaulfootupconf = not loadpaulfootupconf
	if loadpaulfootupconf:
		loadpaulfootupconf2 = not loadpaulfootupconf2
	if loadpaulfootupconf2:
		loadpaulfootupconf3 = not loadpaulfootupconf3
	if loadpaulfootup and loadpaulfootupconf and loadpaulfootupconf2 and not loadpaulfootupconf3:
		paul = lpaula
	else:
		paul = lpaulb
	WIN.blit(paul, getmiddle(paul))
	WIN.blit(ldbg, [getx(ldbg), 100])

@cython.cfunc
def scrollimg(image, x=0, speed=5):
	global scrolly
	width = (image.get_width() / image.get_height()) * 800
	if scrolly > width:
		scrolly = -width
	WIN.blit(image, [x, scrolly])
	scrolly += speed
	if scrolly < 0 - image.get_height():
		scrolly = -600
		return True
	return False

@cython.cfunc
def res(size):
	w, h = WIN.get_size()
	tempscreen = WIN
	tempscreen = pygame.transform.scale(pygame.transform.scale(tempscreen, (w / size, h / size)), (w, h))
	WIN.blit(tempscreen, [0, 0])

@cython.cfunc
def pausescreen():
	global paused, mode, nextargs, playedfilemusic, titlefadeout, soundtracks, enablemouse, enableSettings
	if paused and enablemouse:
		pausescreensurface.blit(pausebg, (0, 0))
		contb = button((100, 100), pausecont, pausecont, pausescreensurface)
		settb = button((100, 164), pausesett, pausesett, pausescreensurface)
		loadb = button((100, 228), pauseload, pauseload, pausescreensurface)
		quitb = button((100, 292), pausequitg, pausequitg, pausescreensurface)
		if quitb == 2:
			leave()
		if contb == 2:
			paused = False
			enablemouse = False
		if settb == 2:
			enableSettings = True
			paused = False
		if loadb == 2:
			mode = 'ldsave'
			nextargs = ''
			paused = False
			playedfilemusic = False
			titlefadeout = False
			soundtracks['sweden'][2] = False

@cython.cfunc
def settings():
	WIN.blit(settbg, getmiddle(settbg))

@cython.cfunc
def game(data):
	global enableChat, enablemouse, loadedMap
	loadedMap.update()
	if paused:
		enablemouse = True
		pausescreen()
	else:
		enablemouse = False
	if enableSettings:
		settings()

@cython.cfunc
def grayscale(surface: pygame.Surface):
	arr = pygame.surfarray.array3d(surface)
	mean_arr = numpy.mean(arr, axis=2)
	mean_arr3d = mean_arr[..., numpy.newaxis]
	new_arr = numpy.repeat(mean_arr3d[:, :, :], 3, axis=2)
	return pygame.surfarray.make_surface(new_arr)

@cython.cfunc
def runCommand(command):
	pass

@cython.cfunc
def console():
	pass

@cython.cfunc
def trigger_ending(name):
	global endingData, enablemouse, mode, nextargs
	enablemouse = True
	if not endingData[name]['intro']:
		pygame.mixer.Channel(0).set_volume(0.5)
		pygame.mixer.Channel(0).play(endingData[name]['start'])
		endingData[name]['intro'] = True
	else:
		if not pygame.mixer.Channel(0).get_busy():
			pygame.mixer.Channel(0).play(endingData[name]['loop'], -1)
	WIN.blit(endingData[name]['img'], (0, 0))
	t = button((getx(endingData['button']), 400), endingData['button'], endingData['button'])
	if t == 2:
		mode = 'title'
		nextargs = ''
		pygame.mixer.Channel(0).stop()
		pygame.mixer.Channel(0).play(introtheme)

@cython.cfunc
def ldsave():
	global logox, nextargs, mode, backX, backY, titlescreen, direction, mwframe, w, s, savefile, enter, ldgamex, mode, savedata, continuefade, \
		playedfilemusic, buttonsPressed, fileselpos, canpastefile, loadedMap
	if not playedfilemusic:
		pygame.mixer.Channel(1).play(soundtracks['loadsave'][0], -1)
		playedfilemusic = True
	WIN.blit(ldsavbg, [0, 0])
	WIN.blit(ldsavslots, getmiddle(ldsavslots))
	if s:
		pygame.mixer.Channel(2).play(popsfx)
		fileselpos[1] += 1
		if fileselpos[1] == 5:
			fileselpos[1] = 1
		time.sleep(0.1)
	if w:
		pygame.mixer.Channel(2).play(popsfx)
		fileselpos[1] -= 1
		if fileselpos[1] == 0:
			fileselpos[1] = 4
		time.sleep(0.1)
	if a:
		pygame.mixer.Channel(2).play(popsfx)
		fileselpos[0] -= 1
		if fileselpos[0] == -1:
			fileselpos[0] = 2
		time.sleep(0.1)
	if d:
		pygame.mixer.Channel(2).play(popsfx)
		fileselpos[0] += 1
		if fileselpos[0] == 3:
			fileselpos[0] = 0
		time.sleep(0.1)
	if fileselpos[1] == 2 and enter:
		canpastefile = True
	sx, sy = getmiddle(ldsavslots)
	if not canpastefile:
		WIN.blit(ldpastebutton, [sx + 38, sy + 120])
		WIN.blit(ldpastebutton, [sx + 218, sy + 120])
		WIN.blit(ldpastebutton, [sx + 398, sy + 120])
	WIN.blit(ldsavthinghy, [(fileselpos[0] * 178) + 19 + sx, (fileselpos[1] * 33) + 26 + sy])
	if enter and fileselpos[1] == 1:
		ldgamex = 0
		try:
			with open(os.path.join('C:', 'Users', os.getlogin(), 'AppData', 'Local', 'smwrpg', 'saves', savefile, '.json')) as f:
				savedata = json.load(f)
		except:
			savedata = {}
		mode = 'game'
		nextargs = 'savedata'
		titlescreen = False
		playedfilemusic = True
		loadedMap = oldmap(os.path.join('assets', 'maps', '4.png'))
		print('Start the game Now!')

@cython.cfunc
def disappearlogo():
	global logox, nextargs, mode, backX, backY, titlescreen, direction, mwframe, w, s, savefile, enter, ldgamex, mode, savedata, continuefade, \
		playedfilemusic, buttonsPressed, fileselpos, canpastefile
	if logox < 801:
		logox += 8
		ldgamex -= 1
		title()
	else:
		ldsave()

@cython.cfunc
def autosave():
	global saveanimi
	img = pygame.image.load(os.path.join('assets', 'save', saveanim[saveanimi], '.png'))
	img = scale2x(img)
	overCurtSurface.blit(img, (2, 530))
	saveanimi += 1
	if saveanimi == 28:
		saveanimi = 0

@cython.cfunc
def playsleep():
	global sleepanimi, soundtracks
	if not soundtracks['sleep'][2]:
		soundtracks['sleep'][2] = True
		pygame.mixer.Channel(0).set_volume(0.7)
		pygame.mixer.Channel(0).play(soundtracks['sleep'][0], fade_ms=256)
	elif (not soundtracks['sleep'][3]) and (not pygame.mixer.Channel(0).get_busy()):
		pygame.mixer.Channel(0).play(soundtracks['sleep'][1], -1)
		soundtracks['sleep'][3] = True
	imgid = sleepanim[floor(sleepanimi)]
	imgpath = os.path.join('assets', 'animations', 'mario', 'sleep', imgid, '.png')
	img = pygame.image.load(imgpath).convert()
	img = pygame.transform.scale(img, (800, 600))
	WIN.blit(img, (0, 0))
	sleepanimi += 0.5
	if sleepanimi == 28.0:
		sleepanimi = 0

@cython.cfunc
def playwatuh():
	song = os.path.join('assets', 'music', 'watuh', f'{random.randint(0, 14)}_intro.mp3')

@cython.cfunc
def title():
	global tick, i, scroll, logoy, mode, nextargs, logox, introplayed, startbounce, startbi, rpgbounce, rpgbi, introcoin, introcoini,\
	coinbi, coinbounce, coinbshine, coinsi, keydown, titlescreen
	titlescreen = True
	logo = tlogo
	rpg = trpg
	cts = tcts
	WIN.blit(cts, [getx(cts) + logox, 500])
	if not pygame.mixer.Channel(0).get_busy():
		pass
		if keydown:
			mode = 'disappearlogo'
			nextargs = ''
			soundtracks['loadsave'] = [pygame.mixer.Sound(os.path.join('assets', 'ldsave', 'main.mp3')), pygame.mixer.Sound(os.path.join('assets', 'ldsave', 'pop.mp3'))]
			titlescreen = True
	logooffset = 60
	try:
		coin = pygame.image.load(os.path.join('assets', 'intro', f'{introcoin[introcoini]}.png')).convert_alpha()
		coin = scale2x(coin)
		WIN.fill((0, 0, 0))
		WIN.blit(coin, getmiddle(coin))
		introcoini += 1
	except:
		try:
			WIN.blit(logo, [getx(logo) + logox, (startbounce[startbi] * (900 / 800)) - logooffset])
		except:
			WIN.blit(logo, [getx(logo) + logox, (logoy * (900 / 800)) - logooffset])
		try:
			WIN.blit(rpg, (getx(rpg) + logox, (rpgbounce[rpgbi] * (900 / 800)) - logooffset - 10))
		except:
			WIN.blit(rpg, (getx(rpg) + logox, (270 * (900 / 800)) - logooffset - 10))
		startbi += 1
		rpgbi += 1
		coinbi += 1
	if not introplayed:
		if not pygame.mixer.Channel(0).get_busy():
			pygame.mixer.Channel(1).play(titletheme, -1)
			introplayed = True

@cython.cfunc
def empty():
	global scroll, i, mode, emptymode, nextargs
	#bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "title", "Background.png")).convert_alpha(), (2043, 600))
	if not emptymode:
		if i <= 32:
			i += 1
	else:
		if not i < 6:
			i -= 1
		if i == 6:
			pass
	scroll += i

@cython.cfunc
def main():
	global tick, frameCount, mode, event, buttonData, nextargs, scroll, playerRun, backX, backY, titlescreen, mwframe, keydown, w, a, s, d, \
		enter, backX, backY, frames, dt, screenUpdate, titlefadeout, soundtracks, buttonsPressed, paused, currentcalledbutton, delta, \
		tick30, lastTick30, debug, debugSettings, shaderTime, luma, mwi, hueShift
	run = True
	void = thevoid
	caclMpos()
	infosurf = pygame.Surface((800, 600), pygame.SRCALPHA | pygame.HWSURFACE)
	while run:
		shaderTime += 2
		frames += 30
		dt += 0.01
		t = pygame.time.get_ticks()
		tick30 = t / 30
		delta = tick30 - lastTick30
		lastTick30 = tick30
		time.sleep(delta / 1000)
		frameCount += clock.tick(FPS)
		if not titlefadeout:
			if not titlescreen:
				titlefadeout = True
				soundtracks['sweden'] = [pygame.mixer.Sound(os.path.join('assets', 'music', 'germany_remastered_intro.mp3')), pygame.mixer.Sound(os.path.join('assets', 'music', 'germany_remastered.mp3')), \
										 False]
				pygame.mixer.Channel(1).play(soundtracks['sweden'][0])
				pygame.mixer.Channel(1).set_volume(0.1)
		if titlefadeout:
			if not soundtracks['sweden'][2]:
				if not pygame.mixer.Channel(1).get_busy():
					pygame.mixer.Channel(1).play(soundtracks['sweden'][1], -1)
					soundtracks['sweden'][2] = True
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				return
			if event.type == pygame.KEYDOWN:
				buttonsPressed.append(event.key)
				keydown = True
				if event.key == pygame.K_LSHIFT:
					playerRun = True
				if event.key == pygame.K_w:
					w = True
				if event.key == pygame.K_a:
					a = True
				if event.key == pygame.K_s:
					s = True
				if event.key == pygame.K_d:
					d = True
				if event.key == pygame.K_ESCAPE:
					if not titlescreen and not enableChat:
						paused = not paused
				if event.key == pygame.K_RETURN:
					enter = True
				if event.key == pygame.K_j:
					set_windowed()
				if event.key == pygame.K_k:
					set_fullscreen()
				if debug:
					if event.key == pygame.K_F2:
						debugSettings[0] = not debugSettings[0]
					elif event.key == pygame.K_F3:
						debugSettings[1] = not debugSettings[1]
					elif event.key == pygame.K_F4:
						debugSettings[2] = not debugSettings[2]
					elif event.key == pygame.K_F5:
						debugSettings[3] = not debugSettings[3]
					elif event.key == pygame.K_F6:
						debugSettings[4] = not debugSettings[4]
					elif event.key == pygame.K_F8:
						debugSettings[5] = not debugSettings[5]
					elif event.key == pygame.K_F9:
						debugSettings[6] = not debugSettings[6]
					elif event.key == pygame.K_F10:
						debugSettings[7] = not debugSettings[7]
					elif event.key == pygame.K_F11:
						debugSettings[8] = not debugSettings[8]
					elif event.key == pygame.K_F12:
						debugSettings[9] = not debugSettings[9]
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					w = False
				if event.key == pygame.K_a:
					a = False
				if event.key == pygame.K_s:
					s = False
				if event.key == pygame.K_d:
					d = False
			if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYAXISMOTION:
				keydown = True
			try:
				if round(pygame.joystick.Joystick(0).get_axis(4)) == -1:
					keyboard.press('w')
			except:
				pass
			try:
				if round(pygame.joystick.Joystick(0).get_axis(0)) == -1:
					keyboard.press('a')
			except:
				pass
			try:
				if round(pygame.joystick.Joystick(0).get_axis(4)) == 1:
					keyboard.press('s')
			except:
				pass
			try:
				if round(pygame.joystick.Joystick(0).get_axis(0)) == 1:
					keyboard.press('d')
			except:
				pass
			try:
				if pygame.joystick.Joystick(0).get_button(1) == 1:
					keyboard.press(Key.enter)
			except:
				pass
			if event.type == pygame.JOYBUTTONDOWN:
				pass
				#print(pygame.joystick.Joystick(0).get_button(0))
			if event.type == pygame.JOYAXISMOTION:
				pass
				########################
				# WICHTIG!!!!!!!!!!
				# Axis 0 = Horizontal!!!!!! (-1 = Links) (1 = Rechts)
				# Axis 2 = Vertikal!!!!!!! (-1 = Oben, 1 = Unten)
		if w:
			if not paused:
				controls.w()
			if not titlescreen:
				keyboard.release('w')
		if a:
			if not paused:
				controls.a()
			if not titlescreen:
				keyboard.release('a')
		if s:
			if not paused:
				controls.s()
			if not titlescreen:
				keyboard.release('s')
		if d:
			if not paused:
				controls.d()
			if not titlescreen:
				keyboard.release('d')
		if titlescreen:
			try:
				titlebackground()
			except:
				print('Oh well')
		keys = pygame.key.get_pressed()
		if debug:
			if keys[pygame.K_F7]:
				if keys[pygame.K_PLUS]:
					debugSettings[11] += 1
					time.sleep(0.1)
				if keys[pygame.K_MINUS]:
					debugSettings[11] -= 1
					time.sleep(0.1)
		else:
			if fullscreen:
				if keys[pygame.K_F11]:
					pygame.display.toggle_fullscreen()
					time.sleep(0.1)
		if keys[pygame.K_LSHIFT]:
			playerRun = True
		# if keys[pygame.K_w]:
		# 	if not paused:
		# 		controls.w()
		# 	if not titlescreen:
		# 		keyboard.release('w')
		# 	w = True
		# if keys[pygame.K_a]:
		# 	if not paused:
		# 		controls.a()
		# 	if not titlescreen:
		# 		keyboard.release('a')
		# 	a = True
		# if keys[pygame.K_s]:
		# 	if not paused:
		# 		controls.s()
		# 	if not titlescreen:
		# 		keyboard.release('s')
		# 	s = True
		# if keys[pygame.K_d]:
		# 	if not paused:
		# 		controls.d()
		# 	if not titlescreen:
		# 		keyboard.release('d')
		# 	d = True
		if keys[pygame.K_RETURN]:
			enter = True
		if keys[pygame.K_F1]:
			debug = not debug
			time.sleep(0.1)
		if not True in [w, a, s, d]:
			mwi = 0
		exec(f'{mode}({nextargs})')
		if frameCount % 8 == 0:
			tick = not tick
			frameCount = 0
		if True in buttonData.values():
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
		else:
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
		if debugSettings[0]:
			noShaderSurface.blit(curtain, [0, 0])
		noShaderSurface.blit(overCurtSurface, (0, 0))
		#Show Debug Menu
		if debug:
			tmem = tracemalloc.get_traced_memory()
			fpsimg = fpsfont.render(
f'''   --DEBUG INFO (for debugging)--
The Adventures of Paul Alpha 1.4 (build 1st May 2023)
FPs:                            {round(clock.get_fps())} / 30
Delta:                          {delta}
Lag:                            {delta - 1}
tick30:                         {tick30}
Player Pos:                  x: {0 - backX}, y: {0 - backY}
SDL Version:                 {sdlv}
SDL TTF version:           {sdlttfv}
Pygame Version:            {pgv}
Python Version:             {pyv}
System Memory:             {ram}
Operating System:          {operatingsys}
CPU Model:                    {cpu}
GPU Model:                    {gpu}
Detected Monitor Size:    {screensize[0]}x{screensize[1]}
Current Map:                 {mapname}
Current Used Memory:     {tmem[0] / 1000000}MB
Peak Used Memory:         {tmem[1] / 1000000}MB
Enable Barrior:              {debugSettings[0]}   (Press F2 to toggle)
Enable scaling:               {debugSettings[1]}   (Press F3 to toggle)
Enable Sprites:               {debugSettings[2]}   (Press F4 to toggle)
Enable Triggers:             {debugSettings[3]}   (Press F5 to toggle)
Show Player:                  {debugSettings[4]}   (Press F6 to toggle)
Player Speed:                 {debugSettings[11]}  (Press F7 and +/- to increase/decrease)
Show map:                      {debugSettings[5]}   (Press F8 to toggle)
Show map Name:              {debugSettings[6]}   (Press F9 to toggle)
Enable debug text (top left) (Press F10 to toggle)
To toggle debug/cheat console press CRTL + P + C (Only works when in debug mode)''',
			False, (255, 255, 255))
			infosurf.fill((0, 0, 0))
			infosurf.set_alpha(128)
		noShaderSurface.convert_alpha()
		if debugSettings[1] or fullscreen:
			scr = grab(0, 0, 800, 600)
			scr = pygame.transform.scale(scr, (screenwidth, screenheight))
			WIN.fill((222, 0, 0))
			WIN.blit(scr, [screenresthalf, 0])
		#res(32)
		playerRun = False
		frame_tex = surf_to_texture(WIN)
		frame_tex.use(0)
		if paused:
			noShaderSurface.blit(pausescreensurface, [0, 0])
		if debug:
			noShaderSurface.blit(infosurf, (0, 0))
			noShaderSurface.blit(fpsimg, [0, 0])
		if fullscreen:
			nscr = pygame.transform.scale(grab(0, 0, 800, 600, noShaderSurface), [screenwidth, screenheight])
			noShaderSurface.fill((222, 0, 0))
			nscr.blit(handleMouse(), pygame.mouse.get_pos())
			noShaderSurface.blit(nscr, [screenresthalf, 0])
			noshadertex = surf_to_texture(noShaderSurface)
		else:
			noShaderSurface.blit(handleMouse(), pygame.mouse.get_pos())
			noshadertex = surf_to_texture(noShaderSurface)
		noshadertex.use(1)
		#noShaderSurface.fill((222, 0, 0))
		shader[0]['tex'] = 0
		#shader[0]['tx'] = shaderTime
		#shader[0]['ty'] = shaderTime
		#shader[0]['luma'] = luma
		shader[1].render(moderngl.TRIANGLE_STRIP)
		noshader[0]['tex'] = 1
		noshader[1].render(moderngl.TRIANGLE_STRIP)
		pygame.display.flip()
		frame_tex.release()
		#noShaderSurface.fill((0, 0, 0)) # VERY IMPORTANT!!! RGB 0|0|0 is transparency (For black use 10|10|10)
		WIN.fill((0, 0, 0))
		keydown = False
		w = False
		a = False
		s = False
		d = False
		enter = False
		buttonData = {}
		currentcalledbutton = 0
		if backX > 0:
			WIN.blit(void, (0, 0))

#@numba.jit(nopython=False)
@cython.cfunc
def start():
	jsondata = {}
	# Set window data
	pygame.display.set_caption('The Adventures of Paul version Alpha 1.4')
	pygame.display.set_icon(pygame.image.load(os.path.join('assets', 'other', 'icon.ico')))
	# Get info about System (also RIP readability)
	#os.chdir(os.path.split(__file__)[0])
	pygame.mixer.Channel(0).play(introtheme)
	globals().update(jsondata)
	# main loop
	main()
	# Print info about what happened
	print(f'Amount of Variables used: {len(globals().keys())}')
	print(f'Amount of Memory (RAM) Used: {tracemalloc.get_traced_memory()[1]} bytes')
	print(f'Game ran for {time.time() - starttime} seconds')
	print('--END OF SESSION--')
	tracemalloc.stop() # Stop the tracemalloc library

@cython.cfunc
def launch(check_main=True):
	def exceptionHandler(e):
		pygame.mouse.set_visible(True)
		errlist = traceback.format_exception_only(e)
		errstr = ''
		for line in errlist:
			errstr += line + '\n'
		pygame.mixer.stop()
		pymsgbox.alert(f'A Fatal Error Accured and the Adventures of Paul will close.\n\n{errstr}', 'Fatal Error', icon=16)
		print(e, end='\n\n')
		pygame.quit()
		e.add_note('           <(^.^)>           ')
		e.add_note('Stop coding you fucking idiot')
		logging.error('Program Crashed')
		logObject.critical(f'Program crashed. {errstr}')
		logObject.update()
		raise e
	if check_main:
		try:
			if __name__ == '__main__':
				start()
			else:
				e = RuntimeError()
				e.add_note('This is a game, not a library, do not use it as one.\nPlease.')
				raise e
		except Exception as e:
			exceptionHandler(e)
	else:
		try:
			start()
		except Exception as e:
			exceptionHandler(e)

launch(False) # i wonder what this does
logObject.flush()
