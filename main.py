import pigpio
import time

pi = pigpio.pi()

light=[18, 23]

button = 21

last_tick =0
mode = 0
max_mode = 3


# Callback for button press
def button_press(gpio, level, tick):
    global last_tick
    global mode
    global max_mode

    print("Button Pressed {} {} {} {}".format(gpio, level, tick, last_tick))
    if last_tick is 0 or tick - last_tick > 500000:
        mode += 1
        if mode == max_mode:
            mode =0

        print("button press - change mode to mode {}" .format(mode))

    last_tick = tick


pi.set_mode(button, pigpio.INPUT)
pi.set_pull_up_down(button, pigpio.PUD_UP)
pi.callback(button, pigpio.FALLING_EDGE, button_press)

delay=0.1


try:
    while (1):

        # Mode 0 -
        if mode == 0:


            for intensity in range(0, 100):
                #print(intensity)
                pi.set_PWM_dutycycle(light[0], intensity)
                pi.set_PWM_dutycycle(light[1], 100 - intensity)
                time.sleep(0.02)

            for flash in range(0,2):
                if flash == 0:
                    pi.set_PWM_dutycycle(light[0], 0)
                    pi.set_PWM_dutycycle(light[1], 175)

                else:
                    pi.set_PWM_dutycycle(light[0], 175)
                    pi.set_PWM_dutycycle(light[1], 0)

                time.sleep(delay)

            pi.set_PWM_dutycycle(light[1], 100)
            pi.set_PWM_dutycycle(light[0], 100)

            for intensity in range(0, 100):
                #print(intensity)
                pi.set_PWM_dutycycle(light[0], intensity)
                pi.set_PWM_dutycycle(light[1], intensity)
                time.sleep(0.02)


            time.sleep(delay)

            for intensity in range(0, 100):
                #print(intensity)
                pi.set_PWM_dutycycle(light[0], 100 - intensity)
                pi.set_PWM_dutycycle(light[1], intensity)
                time.sleep(0.02)

        elif mode == 1:
            for intensity in range(0, 50):
                pi.set_PWM_dutycycle(light[0], intensity)
                pi.set_PWM_dutycycle(light[1], intensity)
                time.sleep(delay)

            for intensity in range(50, 0, -1):
                pi.set_PWM_dutycycle(light[0], intensity)
                pi.set_PWM_dutycycle(light[1], intensity)
                time.sleep(delay)

        elif mode == 2:

            pi.set_PWM_dutycycle(light[1], 255)
            pi.set_PWM_dutycycle(light[0], 255)


except:
    pi.set_PWM_dutycycle(light[0], 0)
    pi.set_PWM_dutycycle(light[1], 0)
    raise()

finally:

    pi.stop()