This library can control up to 4 DC motors by I2C interface. The I2C usually can't support big current for motors, so please use extenal power for the driver board. 



Demo code: 

mt = qwiic_motor.DCMOTOR(i2c=i2c, addr=0x40, freq=1000)

mt.go_ahead(0) # motor A101 is number 0
mt.speed(0,50) # 0 is motor number, 50 is speed, speed range is 0 to 100, when the speed is 0, the motor 
pyb.delay(1000)
mt.go_back(0)
mt.speed(0,50)
pyb.delay(1000)

Note: 
go_ahead() will not make the motor move, it just sets a direction, you need to use speed() method to add speed. 
When the speed is close to 0, ususally the motor will not move. 
Motor Name    Motor NO.
      A101:     0
      B101:     1
      A201:     2
      B201:     3
