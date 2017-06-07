import HTU21D as temp_humid

humidity_sensor = temp_humid.HTU21D()

current_humidity = humidity_sensor.read_humidity()
print( str(current_humidity) + "%")
