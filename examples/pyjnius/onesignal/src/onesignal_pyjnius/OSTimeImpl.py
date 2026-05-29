from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSTimeImpl"]

class OSTimeImpl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSTimeImpl"
    __javaconstructor__ = [("()V", False)]
    getCurrentTimeMillis = JavaMethod("()J")
    getElapsedRealtime = JavaMethod("()J")