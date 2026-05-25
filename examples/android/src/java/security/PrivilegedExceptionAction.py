from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrivilegedExceptionAction"]

class PrivilegedExceptionAction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PrivilegedExceptionAction"
    run = JavaMethod("()Ljava/lang/Object;")