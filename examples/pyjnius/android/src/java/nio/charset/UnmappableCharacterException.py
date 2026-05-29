from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnmappableCharacterException"]

class UnmappableCharacterException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/UnmappableCharacterException"
    __javaconstructor__ = [("(I)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getInputLength = JavaMethod("()I")