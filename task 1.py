class AirConditioning:
    """
    The AirConditioning class an air conditioner.

        Features:
            - __status (bool): The status of the air conditioner (on/off).
            - __temperature (int): The current temperature (degrees Celsius).

        Methods:
            - switch_on(): Turns on the air conditioner and sets the temperature to 18°C.
            - switch_off(): Turns off the air conditioner.
            - reset(): Resets the temperature to 18°C if the air conditioner is on.
            - get_temperature(): Returns the current temperature.
            - raise_temperature(): Increases the temperature by 1°C if the air conditioner is turned on
            and the current temperature is less than 43°C.
            - lower_temperature(): Lowers the temperature by 1°C if the air conditioner is on
            and the current temperature is greater than 0°C.

        Limitations:
            - Control of the air conditioner is possible only when it is switched on.
            - In the off state, the __temperature property is set to None.
            - It is impossible to raise or lower the temperature indefinitely.
            - You can restart only when the air conditioner is on.
        """

    def __init__(self):
        self.__status = False
        self.__temperature = None

    def switch_on(self):
        """Turns on the air conditioner and sets the temperature to 18°C."""
        self.__status = True
        self.__temperature = 18

    def switch_off(self):
        """Turns off the air conditioner."""
        self.__status = False

    def reset(self):
        """Resets the temperature to 18°C if the air conditioner is on."""
        if self.__status:
            self.__temperature = 18

    def get_temperature(self):
        """Returns the current temperature."""
        return self.__temperature

    def raise_temperature(self):
        """Increases the temperature by 1°C if the air conditioner is turned on
        and the current temperature is less than 43°C."""
        if self.__status and self.__temperature < 43:
            self.__temperature += 1

    def lower_temperature(self):
        """Lowers the temperature by 1°C if the air conditioner is turned on
        and the current temperature is greater than 0°C."""
        if self.__status and self.__temperature > 0:
            self.__temperature -= 1

    @property
    def temperature(self):
        """Property for getting the current temperature."""
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        """Property for setting the temperature value."""
        if self.__status and 0 <= value <= 43:
            self.__temperature = value

    @property
    def status(self):
        """Property for obtaining the condition of the air conditioner."""
        return self.__status

    @status.setter
    def status(self, condition):
        """Property for setting the condition of the air conditioner."""
        self.__status = condition

    def __str__(self):
        """Returns a string representation of the condition of the air conditioner."""
        if self.__status:
            return f"{'Включен'}"
        else:
            return f"{'Выключен'}"


air = AirConditioning()
