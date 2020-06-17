from machine import Pin,I2C
import motor


i2c = I2C(sda=Pin("Y10"), scl=Pin("Y9"))
print(i2c.scan())

mt = motor.DCMOTOR(i2c=i2c, addr=0x40, freq=1000)
pyb.delay(1000)

while True:

    for i in range(10,50):
        mt.motor_go_ahead(0)
        mt.motor_speed(0,i)
        print("cw speed:" + str(i))
        pyb.delay(1000)
        mt.motor_go_back(0)
        mt.motor_speed(0,i)
        print("ccw speed:" + str(i))
        pyb.delay(1000)
    mt.motor_stop(0)
    pyb.delay(1000)
