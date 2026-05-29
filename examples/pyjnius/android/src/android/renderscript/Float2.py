from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Float2"]

class Float2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Float2"
    __javaconstructor__ = [("()V", False), ("(FF)V", False)]
    x = JavaField("F")
    y = JavaField("F")