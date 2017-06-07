import tgs2600 as aqsensor

air_qual = aqsensor.TGS2600()

print( str(air_qual.get_value()) +"%")


