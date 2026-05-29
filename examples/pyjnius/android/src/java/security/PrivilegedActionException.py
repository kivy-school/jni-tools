from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrivilegedActionException"]

class PrivilegedActionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PrivilegedActionException"
    __javaconstructor__ = [("(Ljava/lang/Exception;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getException = JavaMethod("()Ljava/lang/Exception;")