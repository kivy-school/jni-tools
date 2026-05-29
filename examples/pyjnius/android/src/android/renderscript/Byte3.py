from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Byte3"]

class Byte3(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Byte3"
    __javaconstructor__ = [("()V", False), ("(BBB)V", False)]
    x = JavaField("B")
    y = JavaField("B")
    z = JavaField("B")