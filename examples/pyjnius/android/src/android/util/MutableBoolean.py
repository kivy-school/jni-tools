from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MutableBoolean"]

class MutableBoolean(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/MutableBoolean"
    __javaconstructor__ = [("(Z)V", False)]
    value = JavaField("Z")