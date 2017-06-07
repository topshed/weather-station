import wind_direction as wind_vane

# Loop forever taking readings
while True:

    # Instantiate a wind vane object
    # 0 = adc channel, wind_direction.json = file
    our_wind_vane = wind_vane.wind_direction(0, "wind_direction.json")

    # Print the direction value after testing for 10 seconds
    interval = 10
    print(our_wind_vane.get_value(interval))

