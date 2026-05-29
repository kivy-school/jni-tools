from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WriteAbortedException"]

class WriteAbortedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/WriteAbortedException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Exception;)V", False)]
    detail = JavaField("Ljava/lang/Exception;")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getCause = JavaMethod("()Ljava/lang/Throwable;")