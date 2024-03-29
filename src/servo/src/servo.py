import RPi.GPIO as GPIO
import time

SERVO_PIN = 18

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    pwm = GPIO.PWM(SERVO_PIN, 50)  # 50 Гц
    pwm.start(0)

    try:
        while True:
            set_angle(0) 
            time.sleep(2)
            set_angle(180)  # Поворачиваем на 180 градусов
            time.sleep(2)
    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()

