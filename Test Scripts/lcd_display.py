from RPLCD.i2c import CharLCD
import time

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2, dotsize=8)
lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string('Solar2Can')
lcd.cursor_pos = (1, 0)
lcd.write_string('12-Lavoisier')