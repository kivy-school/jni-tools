from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimedMetaData"]

class TimedMetaData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/TimedMetaData"
    __javaconstructor__ = [("(J[B)V", False)]
    getTimestamp = JavaMethod("()J")
    getMetaData = JavaMethod("()[B")