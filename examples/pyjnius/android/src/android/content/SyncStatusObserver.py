from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncStatusObserver"]

class SyncStatusObserver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/SyncStatusObserver"
    onStatusChanged = JavaMethod("(I)V")