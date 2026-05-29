from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SettingsSlicesContract"]

class SettingsSlicesContract(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/SettingsSlicesContract"
    AUTHORITY = JavaStaticField("Ljava/lang/String;")
    BASE_URI = JavaStaticField("Landroid/net/Uri;")
    KEY_AIRPLANE_MODE = JavaStaticField("Ljava/lang/String;")
    KEY_BATTERY_SAVER = JavaStaticField("Ljava/lang/String;")
    KEY_BLUETOOTH = JavaStaticField("Ljava/lang/String;")
    KEY_LOCATION = JavaStaticField("Ljava/lang/String;")
    KEY_WIFI = JavaStaticField("Ljava/lang/String;")
    PATH_SETTING_ACTION = JavaStaticField("Ljava/lang/String;")
    PATH_SETTING_INTENT = JavaStaticField("Ljava/lang/String;")