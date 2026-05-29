from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Int4"]

class Int4(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Int4"
    __javaconstructor__ = [("()V", False), ("(IIII)V", False)]
    w = JavaField("I")
    x = JavaField("I")
    y = JavaField("I")
    z = JavaField("I")