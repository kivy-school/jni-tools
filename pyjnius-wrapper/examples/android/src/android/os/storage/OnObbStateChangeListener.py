from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnObbStateChangeListener"]

class OnObbStateChangeListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/storage/OnObbStateChangeListener"
    __javaconstructor__ = [("()V", False)]
    ERROR_ALREADY_MOUNTED = JavaStaticField("I")
    ERROR_COULD_NOT_MOUNT = JavaStaticField("I")
    ERROR_COULD_NOT_UNMOUNT = JavaStaticField("I")
    ERROR_INTERNAL = JavaStaticField("I")
    ERROR_NOT_MOUNTED = JavaStaticField("I")
    ERROR_PERMISSION_DENIED = JavaStaticField("I")
    MOUNTED = JavaStaticField("I")
    UNMOUNTED = JavaStaticField("I")
    onObbStateChange = JavaMethod("(Ljava/lang/String;I)V")