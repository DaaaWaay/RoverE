#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/pwm.h"


int main()
{
    stdio_init_all();
    const uint pin = 15;

    gpio_set_function(pin, GPIO_FUNC_PWM);

    uint slice = pwm_gpio_to_slice_num(pin);

    pwm_set_clkdiv(slice, 125.0f);
    pwm_set_wrap(slice, 999);
    pwm_set_gpio_level(pin, 500);
    pwm_set_enabled(slice, true);

    while (true) {
        int data = getchar_timeout_us(1000);

        if (data == '0')
            pwm_set_gpio_level(pin, 0);

        if (data == '1')
            pwm_set_gpio_level(pin, 250);

        if (data == '2')
            pwm_set_gpio_level(pin, 500);

        if (data == '3')
            pwm_set_gpio_level(pin, 750);
    }
    
}
