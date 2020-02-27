# from https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/
import socket
import I2C_LCD_driver


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1)) # Doesn't really matter what ip, just have to try to connect to something
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def write_to_lcd():
    address = 0x3f  # check correct address
    mylcd = I2C_LCD_driver.lcd(address)
    mylcd.lcd_display_string(get_local_ip(), 1, 0)


if __name__ == "__main__":
    # To run on startup: https://stackoverflow.com/questions/24518522/run-python-script-at-startup-in-ubuntu
    write_to_lcd()
