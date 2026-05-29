from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OperationApplicationException"]

class OperationApplicationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/OperationApplicationException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(I)V", False), ("(Ljava/lang/String;I)V", False)]
    getNumSuccessfulYieldPoints = JavaMethod("()I")