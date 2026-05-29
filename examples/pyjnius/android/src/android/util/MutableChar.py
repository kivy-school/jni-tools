from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MutableChar"]

class MutableChar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/MutableChar"
    __javaconstructor__ = [("(C)V", False)]
    value = JavaField("C")