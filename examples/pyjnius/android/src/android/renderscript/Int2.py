from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Int2"]

class Int2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Int2"
    __javaconstructor__ = [("()V", False), ("(II)V", False)]
    x = JavaField("I")
    y = JavaField("I")