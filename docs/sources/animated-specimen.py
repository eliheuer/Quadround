# Render this specimen GIF with DrawBot3: http://www.drawbot.com/
import math
import os

# Basic variables  (width, height, ):
W, H, M, F = 1024, 1024, 128, 32

# Load font and print font info:
# print(installedFonts(supportsCharacters=None))
os.chdir("..")
os.chdir("..")
font("fonts/Quadround-VF.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))  # Get axis info from font


# Grid drawn from a given increment:
def grid(inc):
    stroke(0.6, 0, 0)  # Set grid line color
    stpX, stpY = 0, 0  # Step in sequence on x axis
    incX, incY = inc, inc  # Grid increment
    for x in range(int(((W-(M*2))/inc)+1)):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX  # Set position for next gridline
    for y in range(int(((H-(M*2))/inc)+1)):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY  # Set position for next gridline


# Page loop
varOpsz = 500
stepUp = 0
stepDown = 0
for frame in range(16):
    newPage(W, H)
    fill(0)           # Background color
    rect(0, 0, W, H)  # Draw the background

    # Draw the grid (uncomment next line)
    grid(32)

    # Basic Style
    stroke(None)
    fill(1)
    
    varOpsz = varOpsz - 25

    # Calculate the weight
    # if frame <= 35:
    #     pass
    #     if frame > 5:
    #         stepUp = stepUp + 12
    #         varOpsz = 100 + stepUp
    # if frame > 40:
    #     stepDown = stepDown + 12
    #     varOpsz = 500 - stepDown
    # if varOpsz >= 500:
    #     varOpsz = 500
    # if varOpsz <= 100:
    #     varOpsz = 100

    # Set weight
    fontVariations(opsz=varOpsz)
    print("varOPSZ=", varOpsz)
    fill(1)
    stroke(None)
    font("fonts/Quadround-VF.ttf")
    fontSize(1010)

    # Draw specimen
    text("A", (M+128+32+16, (896+32)-(8*96)))

# Save GIF
os.chdir("docs")
os.chdir("images")
saveImage("animated-specimen.gif")
os.chdir("..")
os.chdir("sources")