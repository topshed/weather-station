import ds18b20_therm as soil_temp

temp_probe = soil_temp.DS18B20()
print( temp_probe.read_temp() )
