from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLWarning"]

class SQLWarning(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLWarning"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;I)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;ILjava/lang/Throwable;)V", False)]
    getNextWarning = JavaMethod("()Ljava/sql/SQLWarning;")
    setNextWarning = JavaMethod("(Ljava/sql/SQLWarning;)V")