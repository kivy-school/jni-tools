from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OperationCanceledException"]

class OperationCanceledException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/OperationCanceledException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]