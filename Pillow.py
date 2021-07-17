from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

white = 255, 255, 255
black = 0, 0, 0

while True:
	userInput = input("\n\n\nEnter what you would like to write: ")
	if len(userInput) < 1:
		userInput = "Test"

	userFileNameInput = input("Enter the name of the file you would like to write on (include the extension): ")
	if len(userFileNameInput) < 1:
		userFileNameInput = "default.png"

	userColor = input("Enter what color you would like to use (black or white): ")
	if len(userColor) < 1:
		userColor = "black"
	else:
		pass

	if userColor == "black":
		userColor = "black"
	elif userColor == "white":
		userColor = "white"
	else:
		print('Error! Choose only black or white.')

	img = Image.open(f"{userFileNameInput}")
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("bahnschrift.ttf", 100)

	draw.text((100, 100), f"{userInput}", userColor, font=font)

	img.save("Pillow.png")
	print('Done!')