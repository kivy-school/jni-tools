from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSPermissionObserver"]

class OSPermissionObserver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSPermissionObserver"
    onOSPermissionChanged = JavaMethod("(Lcom/onesignal/OSPermissionStateChanges;)V")