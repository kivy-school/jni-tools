from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MutableByte"]

class MutableByte(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/MutableByte"
    __javaconstructor__ = [("(B)V", False)]
    value = JavaField("B")