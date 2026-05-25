from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NavigateToAndroidSettingsForNotifications"]

class NavigateToAndroidSettingsForNotifications(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/NavigateToAndroidSettingsForNotifications"
    INSTANCE = JavaStaticField("Lcom/onesignal/NavigateToAndroidSettingsForNotifications;")
    show = JavaMethod("(Landroid/content/Context;)V")