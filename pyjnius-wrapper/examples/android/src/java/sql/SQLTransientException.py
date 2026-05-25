from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLTransientException"]

class SQLTransientException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLTransientException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;I)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;ILjava/lang/Throwable;)V", False)]