from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrivilegedExceptionAction"]

class PrivilegedExceptionAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PrivilegedExceptionAction"
    run = JavaMethod("()Ljava/lang/Object;")