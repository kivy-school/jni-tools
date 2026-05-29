from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrivilegedAction"]

class PrivilegedAction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PrivilegedAction"
    run = JavaMethod("()Ljava/lang/Object;")