from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncStatusObserver"]

class SyncStatusObserver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/SyncStatusObserver"
    onStatusChanged = JavaMethod("(I)V")