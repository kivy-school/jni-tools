from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSDriverException"]

class RSDriverException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/RSDriverException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]