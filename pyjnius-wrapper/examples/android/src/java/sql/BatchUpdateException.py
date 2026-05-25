from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BatchUpdateException"]

class BatchUpdateException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/BatchUpdateException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;I[I)V", False), ("(Ljava/lang/String;Ljava/lang/String;[I)V", False), ("(Ljava/lang/String;[I)V", False), ("([I)V", False), ("()V", False), ("(Ljava/lang/Throwable;)V", False), ("([ILjava/lang/Throwable;)V", False), ("(Ljava/lang/String;[ILjava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;[ILjava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;I[ILjava/lang/Throwable;)V", False)]
    getUpdateCounts = JavaMethod("()[I")