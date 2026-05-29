from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Double2"]

class Double2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Double2"
    __javaconstructor__ = [("()V", False), ("(DD)V", False)]
    x = JavaField("D")
    y = JavaField("D")