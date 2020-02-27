# from https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/
import netifaces
import I2C_LCD_driver


def get_local_ip():
    ip_obj = netifaces.ifaddresses('eth0')
    return ip_obj[netifaces.AF_INET][0]['addr']


def write_to_lcd():
    address = 0x27  # check correct address
    mylcd = I2C_LCD_driver.lcd(address)
    mylcd.lcd_display_string(get_local_ip(), 1, 0)


if __name__ == "__main__":
    # To run on startup: https://stackoverflow.com/questions/24518522/run-python-script-at-startup-in-ubuntu
    write_to_lcd()
