from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrivilegedAction"]

class PrivilegedAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PrivilegedAction"
    run = JavaMethod("()Ljava/lang/Object;")