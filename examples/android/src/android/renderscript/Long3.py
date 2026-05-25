from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Long3"]

class Long3(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Long3"
    __javaconstructor__ = [("()V", False), ("(JJJ)V", False)]
    x = JavaField("J")
    y = JavaField("J")
    z = JavaField("J")