from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ErrorManager"]

class ErrorManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/ErrorManager"
    __javaconstructor__ = [("()V", False)]
    CLOSE_FAILURE = JavaStaticField("I")
    FLUSH_FAILURE = JavaStaticField("I")
    FORMAT_FAILURE = JavaStaticField("I")
    GENERIC_FAILURE = JavaStaticField("I")
    OPEN_FAILURE = JavaStaticField("I")
    WRITE_FAILURE = JavaStaticField("I")
    error = JavaMethod("(Ljava/lang/String;Ljava/lang/Exception;I)V")