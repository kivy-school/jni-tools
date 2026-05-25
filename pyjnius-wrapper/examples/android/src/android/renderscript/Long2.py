from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Long2"]

class Long2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Long2"
    __javaconstructor__ = [("()V", False), ("(JJ)V", False)]
    x = JavaField("J")
    y = JavaField("J")