from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NavigateToAndroidSettingsForLocation"]

class NavigateToAndroidSettingsForLocation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/NavigateToAndroidSettingsForLocation"
    INSTANCE = JavaStaticField("Lcom/onesignal/NavigateToAndroidSettingsForLocation;")
    show = JavaMethod("(Landroid/content/Context;)V")