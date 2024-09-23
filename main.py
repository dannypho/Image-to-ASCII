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
        # print(f"Pixel at {y},{x} Tuple : {rgbTuple}")
        average = sum(rgbTuple) / 3
        # print(f"Average = {average}")
        brightnessMatrix[x][y] = int(average)


# Printing to terminal. Not viable as VScode terminal does cannot handle all the text
# for x in range(imageHeight):
#     for y in range(imageWidth):
#         characterMatrix[x][y] = brightness_to_character(brightnessMatrix[x][y], characters)
#         print(characterMatrix[x][y], end='')
#     print()

file = open("output.txt", "w")

for x in range(imageHeight):
    for y in range(imageWidth):
        characterMatrix[x][y] = brightness_to_character(brightnessMatrix[x][y], characters)
        file.write(characterMatrix[x][y])
        file.write(characterMatrix[x][y])
        file.write(characterMatrix[x][y])
    file.write("\n")