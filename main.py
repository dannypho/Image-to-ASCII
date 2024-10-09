from PIL import Image

def brightness_to_character(number, characterString):
    index = int((number / 255) * (len(characterString) - 1))
    return characterString[index]


im = Image.open("album.jpg")
pixel = im.load()
imageWidth = im.width
imageHeight = im.height

print("\nSuccessfully loaded image!\n")
print(f"Image size: {imageWidth} x {imageHeight}")

brightnessMatrix = [[0 for j in range(imageWidth)] for x in range(imageHeight)]
characterMatrix = [[0 for j in range(imageWidth)] for x in range(imageHeight)]

characters = "^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


for x in range(imageHeight):
    for y in range(imageWidth):
        rgbTuple = pixel[y, x]
        average = sum(rgbTuple) / 3
        brightnessMatrix[x][y] = int(average)
        
file = open("output.txt", "w")

for x in range(imageHeight):
    for y in range(imageWidth):
        characterMatrix[x][y] = brightness_to_character(brightnessMatrix[x][y], characters)
        file.write(characterMatrix[x][y])
        file.write(characterMatrix[x][y])
        file.write(characterMatrix[x][y])
    file.write("\n")
