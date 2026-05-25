from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Short4"]

class Short4(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Short4"
    __javaconstructor__ = [("()V", False), ("(SSSS)V", False)]
    w = JavaField("S")
    x = JavaField("S")
    y = JavaField("S")
    z = JavaField("S")