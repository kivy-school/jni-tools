from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Float3"]

class Float3(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Float3"
    __javaconstructor__ = [("()V", False), ("(FFF)V", False)]
    x = JavaField("F")
    y = JavaField("F")
    z = JavaField("F")