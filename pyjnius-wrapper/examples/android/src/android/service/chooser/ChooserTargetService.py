from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChooserTargetService"]

class ChooserTargetService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/chooser/ChooserTargetService"
    __javaconstructor__ = [("()V", False)]
    BIND_PERMISSION = JavaStaticField("Ljava/lang/String;")
    META_DATA_NAME = JavaStaticField("Ljava/lang/String;")
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onGetChooserTargets = JavaMethod("(Landroid/content/ComponentName;Landroid/content/IntentFilter;)Ljava/util/List;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")