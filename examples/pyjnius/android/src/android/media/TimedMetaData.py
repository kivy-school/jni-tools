from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimedMetaData"]

class TimedMetaData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/TimedMetaData"
    __javaconstructor__ = [("(J[B)V", False)]
    getMetaData = JavaMethod("()[B")
    getTimestamp = JavaMethod("()J")