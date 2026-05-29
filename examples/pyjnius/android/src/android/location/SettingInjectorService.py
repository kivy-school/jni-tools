from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SettingInjectorService"]

class SettingInjectorService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/SettingInjectorService"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    ACTION_INJECTED_SETTING_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_SERVICE_INTENT = JavaStaticField("Ljava/lang/String;")
    ATTRIBUTES_NAME = JavaStaticField("Ljava/lang/String;")
    META_DATA_NAME = JavaStaticField("Ljava/lang/String;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onStart = JavaMethod("(Landroid/content/Intent;I)V")
    onStartCommand = JavaMethod("(Landroid/content/Intent;II)I")
    onGetSummary = JavaMethod("()Ljava/lang/String;")
    onGetEnabled = JavaMethod("()Z")
    refreshSettings = JavaStaticMethod("(Landroid/content/Context;)V")