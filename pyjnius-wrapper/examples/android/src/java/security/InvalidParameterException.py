from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidParameterException"]

class InvalidParameterException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/InvalidParameterException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]