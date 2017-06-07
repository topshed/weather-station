import HTU21D as temp_humid

ambient_temp = temp_humid.HTU21D()

current_temp = ambient_temp.read_temperature()
print( str(current_temp) + " degrees Celsius")
