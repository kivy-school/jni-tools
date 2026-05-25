from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MutableDouble"]

class MutableDouble(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/MutableDouble"
    __javaconstructor__ = [("(D)V", False)]
    value = JavaField("D")