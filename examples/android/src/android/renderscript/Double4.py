from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Double4"]

class Double4(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Double4"
    __javaconstructor__ = [("()V", False), ("(DDDD)V", False)]
    w = JavaField("D")
    x = JavaField("D")
    y = JavaField("D")
    z = JavaField("D")