from PIL import Image, ImageTk
import tkinter as tk
import random

# divide source image into 16 tiles
def split_image(image_path):
	image = Image.open(image_path)
	width, height = image.size
	tile_width = width // 4
	tile_height = height // 4

	tiles = []
	for i in range(4):
		for j in range(4):
			left = j * tile_width
			upper = i * tile_height
			right = left + tile_width
			lower = upper + tile_height
			tile = image.crop((left, upper, right, lower))
			tiles.append(tile)

	return tiles


# display the tiles in a 4x4 grid
def display_tiles(tiles):
	for i, tile_image in enumerate(tiles):
		tk_image = ImageTk.PhotoImage(tile_image)  # Convert to Tkinter image
		label = tk.Label(root, image=tk_image)
		label.image = tk_image  # Keep a reference!
		row, col = divmod(i, 4)
		label.grid(row=row, column=col)
		# Bind mouse events for drag and drop
		#label.bind("<Button-1>", lambda event, idx=i: start_drag(event, idx))
		#label.bind("<ButtonRelease-1>", lambda event, idx=i: end_drag(event,idx))

# Start dragging
def start_drag(event, index):
	# print to terminal drag starting
	global root

	global drag_start_index
	drag_start_index = index
	# Print the mouse down within the widget, the window and the host system
	print("Drag starting (x,y)       : " + str(event.x) + ", " + str(event.y) + ".")
	print("Drag starting (_root     ): " + str(event.x_root) + ", " + str(event.y_root) + ".")
	print("Drag starting (winfo_root): " + str(root.winfo_rootx()) + ", " + str(root.winfo_rooty()) + ".")

	# Print the index of the tile being dragged
	calculated_index = get_tile_index_from_position(event.x_root, event.y_root, tiles, root)
	print("Drag starting tile index: " + str(index) + "," + str(calculated_index) + ".")
	print(f"Event widget: {event.widget}")

# End dragging (drop)
def end_drag(event, index):
	global root
	# Print the mouse down within the widget, the window and the host system
	print("Drag ending (x,y)       : " + str(event.x) + ", " + str(event.y) + ".")
	print("Drag ending (_root     ): " + str(event.x_root) + ", " + str(event.y_root) + ".")
	print("Drag ending (winfo_root): " + str(root.winfo_rootx()) + ", " + str(root.winfo_rooty()) + ".")
	print(f"Event widget: {event.widget}")
	new_x = root.winfo_rootx() + event.x_root
	new_y = root.winfo_rooty() + event.y_root
	# Print the index of the tile being dragged
	calculated_index = get_tile_index_from_position(new_x, new_y, tiles, root)
	print("Drag ending tile index: " + str(index) + "," + str(calculated_index) + ".")


def pick(event, index):
	# show location of event in all x,y refercence systems
	# Print the mouse down within the widget, the window and the host system
	print("Pick starting (x,y)       : " + str(event.x) + ", " + str(event.y) + ".")
	print("Pick starting (_root     ): " + str(event.x_root) + ", " + str(event.y_root) + ".")
	print("Pick starting (winfo_root): " + str(root.winfo_rootx()) + ", " + str(root.winfo_rooty()) + ".")
	# Print the index of the tile being dragged
	calculated_index = get_tile_index_from_position(event.x_root, event.y_root, tiles, root)
	print("Pick starting tile index: " + str(index) + "," + str(calculated_index) + ".")
	print(f"Event widget: {event.widget}")
	global drag_start_index
	drag_start_index = calculated_index

	


def place(event, index):
	# Print the mouse down within the widget, the window and the host system
	print("Place ending (x,y)       : " + str(event.x) + ", " + str(event.y) + ".")
	print("Place ending (_root     ): " + str(event.x_root) + ", " + str(event.y_root) + ".")
	print("Place ending (winfo_root): " + str(root.winfo_rootx()) + ", " + str(root.winfo_rooty()) + ".")
	# Print the index of the tile being dragged
	calculated_index = get_tile_index_from_position(event.x_root, event.y_root, tiles, root)
	print("Place ending tile index: " + str(index) + "," + str(calculated_index) + ".")
	print(f"Event widget: {event.widget}")
	# Swap the source and destination cells in the tiles list
	swap_tiles(drag_start_index, calculated_index, tiles)

def swap_tiles(source_index, destination_index, tiles):
	# Swap the source and destination cells in the tiles list
	tiles[source_index], tiles[destination_index] = tiles[destination_index], tiles[source_index]
	# Display the updated tiles in a 4x4 grid
	display_tiles(tiles)


def get_tile_index_from_position(x, y, tiles, root):
    # Adjust for the window's absolute position
	grid_mouse_x = x
	grid_mouse_y = y - 60	# Adjust for the window title bar

	tile_width = tiles[0].width
	tile_height = tiles[0].height

	# Calculate the column and row based on the adjusted mouse positions
	col = grid_mouse_x // tile_width
	row = grid_mouse_y // tile_height

	if col >= 4 or row >= 4:  # Outside the grid
		return None
	return row * 4 + col




# Function to rearrange the tiles
def randomize_tiles(tiles):
	# Add your logic here to rearrange the tiles

	# Example: Randomly shuffle the tiles
	random.shuffle(tiles)

	# Display the tiles in a 4x4 grid
	display_tiles(tiles)

# Create the main window
root = tk.Tk()
root.title("Connections Splitter")
# Global variable to track dragging
global drag_start_index
drag_start_index = None


# Prompt the user for the image file in a TK dialog
from tkinter import filedialog
image_path = filedialog.askopenfilename()
print(image_path)


# Split the image into tiles
tiles = split_image(image_path)

# Display the tiles in a 4x4 grid
display_tiles(tiles)

# Button to rearrange the tiles.
# The rearrange_tiles function is called with the tiles list as an argument

button = tk.Button(root, text="Shuffle", command=lambda: randomize_tiles(tiles))	
button.grid(row=4, columnspan=4)

# Bind mouse events for drag and drop relative to parent window
root.bind("<Button-1>", lambda event: pick(event, 0))
root.bind("<ButtonRelease-1>", lambda event: place(event, 0))




# on mouse down event, select a source tile for a move, highlight it and create a draggable image to move with the mouse
# on mouse up event, select a destination tile for the move, swap the tiles and update the display
# on mouse move event, move the draggable image with the mouse
# on mouse out event, remove the draggable image
# on mouse over event, highlight the destination tile
# on mouse click event, swap the source and destination tiles and update the display

def drag_and_drop(event, source_index):
	# Get the destination index based on the mouse position
	destination_index = event.widget.grid_info()['row'] * 4 + event.widget.grid_info()['column']
	
	# Swap the source and destination cells in the tiles list
	tiles[source_index], tiles[destination_index] = tiles[destination_index], tiles[source_index]
	
	# Display the updated tiles in a 4x4 grid
	display_tiles(tiles)

# Function to display the tiles in a 4x4 grid
	
# Start the main event loop
root.mainloop()