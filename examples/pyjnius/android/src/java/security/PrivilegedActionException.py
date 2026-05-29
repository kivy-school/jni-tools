from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrivilegedActionException"]

class PrivilegedActionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PrivilegedActionException"
    __javaconstructor__ = [("(Ljava/lang/Exception;)V", False)]
    getException = JavaMethod("()Ljava/lang/Exception;")
    getCause = JavaMethod("()Ljava/lang/Throwable;")
    toString = JavaMethod("()Ljava/lang/String;")