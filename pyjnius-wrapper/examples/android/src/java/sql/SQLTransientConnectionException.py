from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLTransientConnectionException"]

class SQLTransientConnectionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLTransientConnectionException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;I)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;ILjava/lang/Throwable;)V", False)]