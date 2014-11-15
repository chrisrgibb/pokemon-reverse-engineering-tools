import extract_maps as ex
# import extract_tileblocks

ex.load_rom()

ex.load_map_pointers()




# header attributes
###################
# connections
# address
# referenced_texts
# object_data
# bank
# id
# number_of_referenced_texts
# texts_pointer
# script_pointer
# tileset
# name
# num_connections
# object_data_pointer
# y
# x
# connection_byte
# map_pointer
################
# warp_tos
# warps
# things
# number_of_warps
# number_of_signs
# signs
# number_of_things
# maps_border_tile

map_pointers = {
    #0x00: {
    #       "name": "Pallet Town",
    #       "address": 0x182a1
    #      },
               }

# map_headers = {
    #0x00: {
    #       "name": "Pallet Town",
    #       "address": 0x182a1,
    #       "tileset"
    #       "y"
    #       "x"
    #       "map_pointer"
    #       "texts_pointer"
    #       "script_pointer"
    #       "connection_byte"
    #       "num_connections"
    #       "connections":
    #        { "0":
    #          { map_id, connected_map_tile_pointer, current_map_tile_pointer, bigness, width, y, x, window_pointer }
    #        },
    #       "object_data_pointer" : {
	#            warp_tos
	#            warps
	#            things
	#            number_of_warps
	#            number_of_signs
	#            signs
	#            number_of_things
	#            maps_border_tile
    #        }
    #      },
    #   }

tileblocks = {
"Tset00_Block": [0x645E0, 0x64DE0, ""],
"Tset01_Block": [0x65270, 0x653A0, ""],
"Tset02_Block": [0x693BF, 0x6960F, ""],
"Tset03_Block": [0x6A9FF, 0x6B1FF, ""],
"Tset05_Block": [0x6867F, 0x68DBF, ""],
"Tset08_Block": [0x65980, 0x65BB0, ""],
"Tset09_Block": [0x69BFF, 0x6A3FF, ""],
"Tset0B_Block": [0x6FEF0, 0x70000, ""],
"Tset0D_Block": [0x6E930, 0x6ED10, ""],
"Tset0E_Block": [0x66BF0, 0x66D60, ""],
"Tset0F_Block": [0x6C5C0, 0x6CCA0, ""],
"Tset10_Block": [0x67350, 0x676F0, ""],
"Tset13_Block": [0x66190, 0x66610, ""],
"Tset11_Block": [0x6D0C0, 0x6D8C0, ""],
"Tset12_Block": [0x6DEA0, 0x6E390, ""],
"Tset14_Block": [0x6F2D0, 0x6F670, ""],
"Tset15_Block": [0x6FB20, 0x6FD60, ""],
"Tset16_Block": [0x6B7FF, 0x6C000, ""],
"Tset17_Block": [0x67B50, 0x68000, ""],
}



def do_tileblocks():
	for tileblock_id in tileblocks.keys():
		print tileblock_id

	
def read_blockdata(map_header):
	map_pointer = int(map_header["map_pointer"], 16)
	## width of whole map in blocks
	width = int(map_header["x"], 16)
	height = int(map_header["y"], 16)
	size = width * height
	
	blockdata = ex.rom[map_pointer:map_pointer+size]
	
	return [ord(x) for x in blockdata]

def print_properties(map):
	for prop in map_properties:
		print ' {0} : {1}'.format(prop, map[prop])


def read_blocks(tileset_id):
	blocks = []

	block_width = 4
	block_height = 4
	block_length = block_width * block_height



def create_array(width, height):
	l = []
	for x in xrange(height):
		l.append([0] * width)
	return l

def print_map(map_array):
	width = len(map_array[0])
	height = len(map_array)
	for y in xrange(height):
		line = []
		for x in xrange(width):
			c = str(map_array[y][x])
			line.append(c.ljust(4))
		l2 = ''.join(line)
		print l2


def draw_map(mapp):
	map = headers[mapp]
	# print "drawing map : {0}".format(map["name"])

	print_properties(map)
	width = int(map["x"], 16)
	height = int(map["y"], 16)
	
	tileset_id = int(map["tileset"], 16)
	blockdata = read_blockdata(map)

	# print blockdata
	blocks2d = create_array(width, height)
	block_x = 0
	print ' tileset_id = {0}'.format(tileset_id)

	for blocknum in xrange(len(blockdata)):
		line = ""
		
		block_x = blocknum % width 
		block_y = blocknum / width
		
		index = block_y * width + block_x
			
		block = blockdata[index]
		blocks2d[block_y][block_x] = block
		
		# lines.append(line)
	# print myblocks
	print_map(blocks2d)

## MAIN ## 

headers = ex.read_all_map_headers()

map_properties = [
"name",
"tileset",
"map_pointer",
"x",
"y"
]

do_tileblocks();

draw_map(58)


