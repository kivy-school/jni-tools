from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnrecoverableKeyException"]

class UnrecoverableKeyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/UnrecoverableKeyException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]