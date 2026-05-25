from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSTime"]

class OSTime(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSTime"
    getCurrentTimeMillis = JavaMethod("()J")
    getElapsedRealtime = JavaMethod("()J")