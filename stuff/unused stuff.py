
####################################################
# IMPOTANT!!! OLD MAP INIT CODE! **DO NOT REMOVE** #
####################################################

# def __init__(file, pathtomod=None):
#         path, ext = os.path.split(file)
#         if not pathtomod == None:
#             if os.path.isdir(pathtomod):
#                 sys.path.insert(os.path.split(pathtomod)[0])
#                 import_module('taop_mode-main', 'main')
#         if not ext == '.pmap':
#             ctypes.windll.user32.MessageBoxW(0, "ERROR: Invalid map file", "FATAL ERROR", 0x0 | 0x10)
#             pygame.quit()
#         mapdatadir = f'{appdir}\\__map.cache__\\mapdata.json'
#         shutil.copyfile(file, mapdatadir)
#         try:
#             mapdatafile = open(mapdatadir, 'r')
#             mapdatastr = str(mapdatafile.read())
#             mapdatafile.close()
#             mapdata = json.loads(mapdatastr)
#         except:
#             ctypes.windll.user32.MessageBoxW(0, "ERROR: Invalid map file", "FATAL ERROR", 0x0 | 0x10)
#             pygame.quit()
#         layer1png = mapdata['layer1']
#         spritedata = mapdata['sprites']
#         texts = mapdata['texts']
#         name = mapdata['meta']['name']
#         assetzip = mapdata['assets']
#         with open(f'{appdir}\\__map.cache__\\mapassets.zip', 'w') as f:
#             f.write(assetzip)
#             f.close()
#         with zipfile.ZipFile(f'{appdir}\\__map.cache__\\mapassets.zip', 'r') as f:
#             f.extractall(f'{appdir}\\__map.cache__\\assets')
#             f.close()
#         with open(f'{appdir}\\__map.cache__\\layer1.png', 'w') as f:
#             f.write(layer1png)
#             f.close()
#         with open(f'{appdir}\\__map.cache__\\data.json', 'w') as f:
#             json.dump({"sprites": spritedata, "text": texts}, f)
#             f.close()
#         font = pygame.font.Font('assets\\font\\world.ttf', 32)
#         output = {
#             "assets": f'{appdir}\\__map.cache__\\assets',
#             "tileset": 'main',
#             "finalAssetPath": f'{appdir}\\__map.cache__\\assets\\main',
#             "layer1": pygame.image.load(f'{appdir}\\__map.cache__\\layer1.png'),
#             "data": open(f'{appdir}\\__map.cache__\\data.json', 'r'),
#             "name": font.render(name, True, (248, 248, 248)),
#             "size": pygame.image.load(f'{appdir}\\__map.cache__\\layer1.png').get_size(),
#             "3Anim": 0,
#             "5Anim": 0
#         }
#         return output

# class map:
# 	def __init__(path):
# 		global mapSize
# 		with open(os.path.join(path, 'mapdata.json'), 'r') as f:
# 			datas = json.load(f)
# 			f.close()
# 		name = datas['name']
# 		font = pygame.font.Font(os.path.join('assets', 'font', 'world.ttf'), 32)
# 		mapSize = pygame.image.load(os.path.join(path, 'map.png')).convert_alpha().get_size()
# 		output = {
# 			"assets": os.path.join(appdir, '__map.cache__', 'assets'),
# 			"tileset": 'main',
# 			"finalAssetPath": os.path.join(path, 'assets', 'main'),
# 			"layer1": pygame.image.load(os.path.join(path, 'map.png')).convert_alpha(),
# 			"data": {"sprites": datas['sprites'], "triggers": datas['triggers'], "texts": datas['texts']},
# 			"name": font.render(name, False, (248, 248, 248)),
# 			"size": mapSize,
# 			"3Anim": 0,
# 			"5Anim": 0,
# 			"source": path
# 		}
# 		return output

# 	MAPPINGS = {
# 		0: None
# 	}

# 	def update(map):
# 		global backX, backY, direction, mwframe
# 		if debugSettings[5]:
# 			WIN.blit(map['layer1'], backX, backY)
# 		m = pygame.image.load(os.path.join('assets', 'animations', 'mario', 'walk', direction, int(mwframe))).convert_alpha()
# 		m = scale2x(m)
# 		mpos = getmiddle(m)
# 		playerBox = pygame.Rect(mpos[0], mpos[1], m.get_width(), m.get_height())
# 		def calcPos(pos):
# 			ox, oy = pos
# 			x = backX + ox
# 			y = backY + oy
# 			return (x, y)
# 		if debugSettings[6]:
# 			WIN.blit(map['name'], [120, 100])
# 		assetpath = map['finalAssetPath']
# 		datas = map['data']
# 		sprites = datas['sprites']
# 		triggers = datas['triggers']
# 		texts = datas['texts']
# 		a3 = datas['3Anim']
# 		a5 = datas['5Anim']
# 		sID = 0
# 		cID = 0
# 		collidedRects = []
# 		if debugSettings[2]:
# 			for sprite in sprites:
# 				pos = sprite['pos']
# 				type = sprite['type']
# 				animType = sprite['aType']
# 				sID += 1
# 				realPos = calcPos(pos)
# 				rx, ry = realPos
# 				if rx <= -16:
# 					continue
# 				if rx > 800:
# 					continue
# 				if ry < -16:
# 					continue
# 				if ry > 600:
# 					continue
# 				if animType == 0:
# 					imgpath = os.path.join(assetpath, f'{type}.{a3}.png')
# 				else:
# 					imgpath = os.path.join(assetpath, f'{type}.{a5}.png')
# 				img = scale2x(pygame.image.load(imgpath).convert_alpha())
# 				WIN.blit(img, realPos)
# 		if debugSettings[3]:
# 			for trigger in triggers:
# 				x, y = trigger['pos']
# 				w, h = trigger['size']
# 				rx = x + backX
# 				ry = y + backY
# 				func = trigger['func']
# 				if (rx + w) < 0:
# 					continue
# 				if rx > 800:
# 					continue
# 				if (ry + h) < 0:
# 					continue
# 				if ry > 600:
# 					continue
# 				collide = pygame.Rect.contains(playerBox)
# 				if collide:
# 					collidedRects.append(cID)
# 				cID += 1
# 		if debugSettings[4]:
# 			WIN.blit(m, mpos)
# 		return collidedRects

# 	def updatePos(map, sID, newPos):
# 		sprite = map['data']['sprites'][sID]
# 		sprite['pos'] = newPos
# 		map['data']['sprites'][sID] = sprite
# 		return map
	
# 	def tileSet(map, tileset):
# 		mapData = map['data']
# 		defaultAssetPath = mapData['assets']
# 		newAssetPath = os.path.join(defaultAssetPath, tileset)
# 		mapData['tileset'] = tileset
# 		mapData['finalAssetPath'] = newAssetPath
# 		newMap = map
# 		newMap['data'] = mapData
# 		return newMap

# 	def stepAnimation(map):
# 		o3 = map['data']['3Anim']
# 		o5 = map['data']['5Anim']
# 		o3 += 1
# 		o5 += 1
# 		if o3 == 3:
# 			o3 = 0
# 		if o5 == 5:
# 			o5 = 0
# 		map['data']['3Anim'] = o3
# 		map['data']['5Anim'] = o5
# 		return map
