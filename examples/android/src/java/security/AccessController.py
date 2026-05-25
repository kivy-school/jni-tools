from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessController"]

class AccessController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AccessController"
    doPrivileged = JavaMultipleMethod([("(Ljava/security/PrivilegedAction;)Ljava/lang/Object;", True, False), ("(Ljava/security/PrivilegedAction;Ljava/security/AccessControlContext;)Ljava/lang/Object;", True, False), ("(Ljava/security/PrivilegedExceptionAction;)Ljava/lang/Object;", True, False), ("(Ljava/security/PrivilegedExceptionAction;Ljava/security/AccessControlContext;)Ljava/lang/Object;", True, False)])
    doPrivilegedWithCombiner = JavaMultipleMethod([("(Ljava/security/PrivilegedAction;)Ljava/lang/Object;", True, False), ("(Ljava/security/PrivilegedExceptionAction;)Ljava/lang/Object;", True, False)])
    getContext = JavaStaticMethod("()Ljava/security/AccessControlContext;")
    checkPermission = JavaStaticMethod("(Ljava/security/Permission;)V")