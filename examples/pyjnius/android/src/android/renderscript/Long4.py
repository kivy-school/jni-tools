from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Long4"]

class Long4(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Long4"
    __javaconstructor__ = [("()V", False), ("(JJJJ)V", False)]
    w = JavaField("J")
    x = JavaField("J")
    y = JavaField("J")
    z = JavaField("J")