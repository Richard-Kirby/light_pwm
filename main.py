import pigpio
import time

pi = pigpio.pi()

light=[18, 23]

button = 21

pi.set_mode(button, pigpio.INPUT)
pi.set_pull_up_down(button, pigpio.PUD_UP)


try:
    while (1):

        for intensity in range(0, 100):
            print(intensity)
            pi.set_PWM_dutycycle(light[0], intensity)
            pi.set_PWM_dutycycle(light[1], 100 - intensity)
            time.sleep(0.02)
            if pi.read(button) is 0:
                print("button pressed")


        for flash in range(0,2):
            if flash == 0:
                pi.set_PWM_dutycycle(light[0], 0)
                pi.set_PWM_dutycycle(light[1], 175)

            else:
                pi.set_PWM_dutycycle(light[0], 175)
                pi.set_PWM_dutycycle(light[1], 0)

            time.sleep(0.5)

        pi.set_PWM_dutycycle(light[1], 100)
        pi.set_PWM_dutycycle(light[0], 100)

        for intensity in range(0, 100):
            print(intensity)
            pi.set_PWM_dutycycle(light[0], intensity)
            pi.set_PWM_dutycycle(light[1], intensity)
            time.sleep(0.02)


        time.sleep(0.5)

        for intensity in range(0, 100):
            print(intensity)
            pi.set_PWM_dutycycle(light[0], 100 - intensity)
            pi.set_PWM_dutycycle(light[1], intensity)
            time.sleep(0.02)

except:
    pi.set_PWM_dutycycle(light[0], 0)
    pi.set_PWM_dutycycle(light[1], 0)

finally:

    pi.stop()