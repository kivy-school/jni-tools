from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MutableShort"]

class MutableShort(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/MutableShort"
    __javaconstructor__ = [("(S)V", False)]
    value = JavaField("S")