# Import modules
import ev3dev.ev3 as ev3

# Instantiate motors and sensors
ts = ev3.TouchSensor()
lm = ev3.LargeMotor('outA')

# The Loop
while True:
  # Check if you are holding down the touch sensor 
  if ts.value() == 1:
  # Run the motor!
    lm.run_timed(time_sp = 1, speed_sp = 1000)
