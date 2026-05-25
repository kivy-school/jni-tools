from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Byte2"]

class Byte2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Byte2"
    __javaconstructor__ = [("()V", False), ("(BB)V", False)]
    x = JavaField("B")
    y = JavaField("B")