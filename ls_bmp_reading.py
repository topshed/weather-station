import bmp085 as bmp

sensor = bmp.BMP085()

print( sensor.get_pressure())
