from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharacterCodingException"]

class CharacterCodingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CharacterCodingException"
    __javaconstructor__ = [("()V", False)]