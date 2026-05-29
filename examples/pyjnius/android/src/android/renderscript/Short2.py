from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Short2"]

class Short2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Short2"
    __javaconstructor__ = [("()V", False), ("(SS)V", False)]
    x = JavaField("S")
    y = JavaField("S")