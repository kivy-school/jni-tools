from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Short3"]

class Short3(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Short3"
    __javaconstructor__ = [("()V", False), ("(SSS)V", False)]
    x = JavaField("S")
    y = JavaField("S")
    z = JavaField("S")