from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GenericSignatureFormatError"]

class GenericSignatureFormatError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/GenericSignatureFormatError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]