from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Int3"]

class Int3(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Int3"
    __javaconstructor__ = [("()V", False), ("(III)V", False)]
    x = JavaField("I")
    y = JavaField("I")
    z = JavaField("I")