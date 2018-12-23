import pigpio
import time

pi = pigpio.pi()

light=[18, 23]

delay=0.1

try:
    while (1):

        for intensity in range(0, 50):
            print(intensity)
            pi.set_PWM_dutycycle(light[0], intensity)
            pi.set_PWM_dutycycle(light[1], intensity)
            time.sleep(delay)

        for intensity in range(50, 0, -1):
            print(intensity)
            pi.set_PWM_dutycycle(light[0], intensity)
            pi.set_PWM_dutycycle(light[1], intensity)
            time.sleep(delay)


except:
    pi.set_PWM_dutycycle(light[0], 0)
    pi.set_PWM_dutycycle(light[1], 0)

finally:

    pi.stop()