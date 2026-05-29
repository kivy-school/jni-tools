from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MutableLong"]

class MutableLong(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/MutableLong"
    __javaconstructor__ = [("(J)V", False)]
    value = JavaField("J")