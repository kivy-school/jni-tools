from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeFormatException"]

class TimeFormatException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/TimeFormatException"