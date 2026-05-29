from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSIllegalArgumentException"]

class RSIllegalArgumentException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/RSIllegalArgumentException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]