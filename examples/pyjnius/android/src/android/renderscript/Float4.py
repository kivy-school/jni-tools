from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Float4"]

class Float4(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Float4"
    __javaconstructor__ = [("()V", False), ("(FFFF)V", False)]
    w = JavaField("F")
    x = JavaField("F")
    y = JavaField("F")
    z = JavaField("F")