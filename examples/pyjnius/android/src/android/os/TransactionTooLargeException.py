from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransactionTooLargeException"]

class TransactionTooLargeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/TransactionTooLargeException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]