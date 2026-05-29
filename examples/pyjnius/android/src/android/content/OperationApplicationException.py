from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OperationApplicationException"]

class OperationApplicationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/OperationApplicationException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;I)V", False), ("()V", False), ("(I)V", False), ("(Ljava/lang/String;)V", False)]
    getNumSuccessfulYieldPoints = JavaMethod("()I")