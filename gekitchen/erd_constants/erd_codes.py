"""ERD Codes for GE appliances"""
import enum


@enum.unique
class ErdCode(enum.Enum):
    """
    ERD codes for GE kitchen appliance properties.
    These were mostly lifted from ERD.smali in the the GE SmartHQ app v1.0.3.13
    """
    APPLIANCE_TYPE = "0x0008"
    CLOCK_FORMAT = "0x0006"
    CLOCK_TIME = "0x0005"
    MODEL_NUMBER = "0x0001"
    SABBATH_MODE = "0x0009"
    SERIAL_NUMBER = "0x0002"
    SOUND_LEVEL = "0x000a"
    TEMPERATURE_UNIT = "0x0007"
    USER_INTERFACE_LOCKED = "0x0004"

    # Low-level-type things
    WIFI_MODULE_SW_VERSION = "0x0100"
    WIFI_MODULE_SW_VERSION_AVAILABLE = "0x0101"
    ACM_UPDATING = "0x0102"
    APPLIANCE_SW_VERSION = "0x0103"
    APPLIANCE_SW_VERSION_AVAILABLE = "0x0104"
    APPLIANCE_UPDATING = "0x0105"
    LCD_SW_VERSION = "0x0106"
    LCD_SW_VERSION_AVAILABLE = "0x0107"
    LCD_UPDATING = "0x0108"

    # Dishwasher Codes
    CYCLE_NAME = "0x301c"
    CYCLE_STATE = "0x300e"
    OPERATING_MODE = "0x3001"
    PODS_REMAINING_VALUE = "0x301f"
    RINSE_AGENT = "0x3003"
    SOUND = "0x3007"
    TIME_REMAINING = "0xd004"

    # Fridge codes
    AIR_FILTER_STATUS = "0x101c"
    DOOR_STATUS = "0x1016"
    FRIDGE_MODEL_INFO = "0x101d"
    HOT_WATER_IN_USE = "0x1018"
    HOT_WATER_SET_TEMP = "0x1011"
    HOT_WATER_STATUS = "0x1010"
    ICE_MAKER_BUCKET_STATUS = "0x1007"
    ICE_MAKER_CONTROL = "0x100a"
    SETPOINT_LIMITS = "0x100b"
    CURRENT_TEMPERATURE = "0x1004"
    TEMPERATURE_SETTING = "0x1005"
    TURBO_COOL_STATUS = "0x100f"
    TURBO_FREEZE_STATUS = "0x100e"
    WATER_FILTER_STATUS = "0x1009"

    # Oven codes
    ACTIVE_F_CODE_STATUS = "0x5005"
    CONVECTION_CONVERSION = "0x5003"
    ELAPSED_ON_TIME = "0x5004"
    END_TONE = "0x5001"
    HOUR_12_SHUTOFF_ENABLED = "0x5000"
    KEY_PRESSED = "0x5006"
    LIGHT_BAR = "0x5002"
    LOWER_OVEN_AVAILABLE_COOK_MODES = "0x520b"
    LOWER_OVEN_COOK_MODE = "0x5200"
    LOWER_OVEN_COOK_TIME_REMAINING = "0x5204"
    LOWER_OVEN_CURRENT_STATE = "0x5201"
    LOWER_OVEN_DELAY_TIME_REMAINING = "0x5202"
    LOWER_OVEN_DISPLAY_TEMPERATURE = "0x5209"
    LOWER_OVEN_ELAPSED_COOK_TIME = "0x5208"
    LOWER_OVEN_KITCHEN_TIMER = "0x5205"
    LOWER_OVEN_PROBE_DISPLAY_TEMP = "0x5203"
    LOWER_OVEN_PROBE_PRESENT = "0x5207"
    LOWER_OVEN_REMOTE_ENABLED = "0x520a"
    LOWER_OVEN_USER_TEMP_OFFSET = "0x5206"
    LOWER_OVEN_WARMING_DRAWER_STATE = "0x520c"
    LOWER_OVEN_RAW_TEMPERATURE = "0x520d"
    OVEN_CONFIGURATION = "0x5007"
    OVEN_MODE_MIN_MAX_TEMP = "0x5008"
    UPPER_OVEN_AVAILABLE_COOK_MODES = "0x510b"
    UPPER_OVEN_COOK_MODE = "0x5100"
    UPPER_OVEN_COOK_TIME_REMAINING = "0x5104"
    UPPER_OVEN_CURRENT_STATE = "0x5101"
    UPPER_OVEN_DELAY_TIME_REMAINING = "0x5102"
    UPPER_OVEN_DISPLAY_TEMPERATURE = "0x5109"
    UPPER_OVEN_ELAPSED_COOK_TIME = "0x5108"
    UPPER_OVEN_KITCHEN_TIMER = "0x5105"
    UPPER_OVEN_PROBE_DISPLAY_TEMP = "0x5103"
    UPPER_OVEN_PROBE_PRESENT = "0x5107"
    UPPER_OVEN_REMOTE_ENABLED = "0x510a"
    UPPER_OVEN_USER_TEMP_OFFSET = "0x5106"
    UPPER_OVEN_WARMING_DRAWER_STATE = "0x510c"
    UPPER_OVEN_RAW_TEMPERATURE = "0x510d"
    WARMING_DRAWER_STATE = "0x5009"

    # Microwave
    MICROWAVE_RECIPE_STATUS = "0x5300"
    # Lots more in 0x5Cxx

    # Hood
