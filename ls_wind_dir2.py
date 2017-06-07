import wind_direction as wind_vane
import turtle

# Create a turtle object
ben = turtle.Turtle()
turtle.mode("logo") # Logo mode (0 is North)
ben.degrees()

def draw_line(angle, length):
    ben.setheading(angle)
    ben.forward(length)
    ben.backward(length)
    
# Draw a compass
compass = 0
while compass < 360:
    draw_line(compass, 80)
    compass = compass + 90

# Loop forever taking readings
while True:

    # Instantiate a wind vane object
    # 0 = adc channel, wind_direction.json = file
    our_wind_vane = wind_vane.wind_direction(0, "wind_direction.json")

    # Print the direction value after testing for 10 seconds
    interval = 10
    degrees = our_wind_vane.get_value(interval)

    # Calculate the direction
    if degrees >= 338 or degrees < 23:
        print("N")
    elif degrees >= 23 and degrees < 68:
        print("NE")
    elif degrees >= 68 and degrees < 113:
        print("E")
    elif degrees >= 113 and degrees < 158:
        print("SE")
    elif degrees >= 158 and degrees < 203:
        print("S")
    elif degrees >= 203 and degrees < 248:
        print("SW")
    elif degrees >= 248 and degrees < 293:
        print("W")
    elif degrees >= 293 and degrees < 338:
        print("NW")
    else:
        print("No idea!")


    # Draw the wind direction
    direction = round(degrees)
    print("Direction: " + str(direction))

    ben.pencolor("red")   
    draw_line(direction, 40)
    
    

