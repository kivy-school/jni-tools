from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MutableInt"]

class MutableInt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/MutableInt"
    __javaconstructor__ = [("(I)V", False)]
    value = JavaField("I")