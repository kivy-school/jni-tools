from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnknownServiceException"]

class UnknownServiceException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/UnknownServiceException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]