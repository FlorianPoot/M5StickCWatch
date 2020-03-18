import ustruct
import i2c_bus


class Axp192:
    
    def __init__(self):
        self.addr = 0x34
        self.i2c = i2c_bus.get(i2c_bus.M_BUS)
    
    def power_all(self):
        regchar = self._regchar
        regchar(0x10, 0xff)
        regchar(0x28, 0xff)
        regchar(0x82, 0xff)
        regchar(0x33, 0xc0)
        regchar(0x33, 0xc3)
        regchar(0xb8, 0x80)
        regchar(0x12, 0x4d)
        regchar(0x36, 0x5c)
        regchar(0x90, 0x02)

    def screen_breath(self, brightness):
        self._regchar(0x28, ((brightness & 0x0f) << 4))

    def enable_coulomb_counter(self):
        self._regchar(0xb8, 0x80)

    def disable_coulomb_counter(self):
        self._regchar(0xb8, 0x00)

    def stop_coulomb_counter(self):
        self._regchar(0xb8, 0xc0)

    def clear_coulomb_counter(self):
        self._regchar(0xb8, 0xa0)

    def get_coulomb_charge_data(self):
        buf = self._regchar(0xb0)
        buf1 = self._regchar(0xb1)
        buf2 = self._regchar(0xb2)
        buf3 = self._regchar(0xb3)

        return (buf << 24) + (buf1 << 16) + (buf2 << 8) + buf3

    def get_coulomb_discharge_data(self):
        buf = self._regchar(0xb4)
        buf1 = self._regchar(0xb5)
        buf2 = self._regchar(0xb6)
        buf3 = self._regchar(0xb7)

        return (buf << 24) + (buf1 << 16) + (buf2 << 8) + buf3

    def get_coulomb_data(self):
        coin = self.get_coulomb_charge_data()
        coout = self.get_coulomb_discharge_data()

        return 65536 * 0.5 * (coin - coout) / 3600.0 / 25.0

    def get_vbat_data(self):
        buf = self._regchar(0x78)
        buf1 = self._regchar(0x79)

        return (buf << 4) + buf1

    def get_vin_data(self):
        buf = self._regchar(0x56)
        buf1 = self._regchar(0x57)

        return (buf << 4) + buf1

    def get_iin_data(self):
        buf = self._regchar(0x58)
        buf1 = self._regchar(0x59)

        return (buf << 4) + buf1

    def get_icharge_data(self):
        buf = self._regchar(0x7a)
        buf1 = self._regchar(0x7b)

        return (buf << 5) + buf1

    def get_idischarge_data(self):
        buf = self._regchar(0x7c)
        buf1 = self._regchar(0x7d)

        return (buf << 5) + buf1

    def get_temp_data(self):
        buf = self._regchar(0x5e)
        buf1 = self._regchar(0x5f)

        return (buf << 4) + buf1

    def get_power_bat_data(self):
        buf = self._regchar(0x70)
        buf1 = self._regchar(0x71)
        buf2 = self._regchar(0x72)

        return (buf << 16) + (buf1 << 8) + buf2

    def get_vaps_data(self):
        buf = self._regchar(0x7e)
        buf1 = self._regchar(0x7f)

        return (buf << 4) + buf1

    def set_sleep(self):
        buf = self._regchar(0x31)
        buf = (1 << 3) | buf

        self._regchar(0x31, buf)
        self._regchar(0x12, 0x41)

    def get_warning_level(self):
        buf = self._regchar(0x47)

        return buf & 0x01

    def _regchar(self, reg, value=None, buf=bytearray(1)):
        if value is None:
            self.i2c.readfrom_mem_into(self.addr, reg, buf)
            return buf[0]

        ustruct.pack_into('<b', buf, 0, value)
        return self.i2c.writeto_mem(self.addr, reg, buf)

    def deinit(self):
        pass
