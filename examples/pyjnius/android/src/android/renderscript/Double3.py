from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Double3"]

class Double3(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Double3"
    __javaconstructor__ = [("()V", False), ("(DDD)V", False)]
    x = JavaField("D")
    y = JavaField("D")
    z = JavaField("D")