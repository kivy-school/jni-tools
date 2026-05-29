from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZipPathValidator"]

class ZipPathValidator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/ZipPathValidator"
    clearCallback = JavaStaticMethod("()V")
    setCallback = JavaStaticMethod("(Ldalvik/system/ZipPathValidator$Callback;)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "dalvik/system/ZipPathValidator$Callback"
        onZipEntryAccess = JavaMethod("(Ljava/lang/String;)V")