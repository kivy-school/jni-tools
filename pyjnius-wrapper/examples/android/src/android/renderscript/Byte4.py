from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Byte4"]

class Byte4(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Byte4"
    __javaconstructor__ = [("()V", False), ("(BBBB)V", False)]
    w = JavaField("B")
    x = JavaField("B")
    y = JavaField("B")
    z = JavaField("B")