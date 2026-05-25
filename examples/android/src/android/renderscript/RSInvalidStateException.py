from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSInvalidStateException"]

class RSInvalidStateException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/RSInvalidStateException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]