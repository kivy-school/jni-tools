from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLException"]

class SQLException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;I)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;ILjava/lang/Throwable;)V", False)]
    getSQLState = JavaMethod("()Ljava/lang/String;")
    getErrorCode = JavaMethod("()I")
    getNextException = JavaMethod("()Ljava/sql/SQLException;")
    setNextException = JavaMethod("(Ljava/sql/SQLException;)V")
    iterator = JavaMethod("()Ljava/util/Iterator;")