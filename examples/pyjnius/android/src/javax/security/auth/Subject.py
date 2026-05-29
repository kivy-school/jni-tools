from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Subject"]

class Subject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/Subject"
    __javaconstructor__ = [("()V", False), ("(ZLjava/util/Set;Ljava/util/Set;Ljava/util/Set;)V", False)]
    getSubject = JavaStaticMethod("(Ljava/security/AccessControlContext;)Ljavax/security/auth/Subject;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    current = JavaStaticMethod("()Ljavax/security/auth/Subject;")
    setReadOnly = JavaMethod("()V")
    getPrincipals = JavaMultipleMethod([("(Ljava/lang/Class;)Ljava/util/Set;", False, False), ("()Ljava/util/Set;", False, False)])
    callAs = JavaStaticMethod("(Ljavax/security/auth/Subject;Ljava/util/concurrent/Callable;)Ljava/lang/Object;")
    doAs = JavaMultipleMethod([("(Ljavax/security/auth/Subject;Ljava/security/PrivilegedAction;)Ljava/lang/Object;", True, False), ("(Ljavax/security/auth/Subject;Ljava/security/PrivilegedExceptionAction;)Ljava/lang/Object;", True, False)])
    doAsPrivileged = JavaMultipleMethod([("(Ljavax/security/auth/Subject;Ljava/security/PrivilegedExceptionAction;Ljava/security/AccessControlContext;)Ljava/lang/Object;", True, False), ("(Ljavax/security/auth/Subject;Ljava/security/PrivilegedAction;Ljava/security/AccessControlContext;)Ljava/lang/Object;", True, False)])
    getPublicCredentials = JavaMultipleMethod([("(Ljava/lang/Class;)Ljava/util/Set;", False, False), ("()Ljava/util/Set;", False, False)])
    getPrivateCredentials = JavaMultipleMethod([("(Ljava/lang/Class;)Ljava/util/Set;", False, False), ("()Ljava/util/Set;", False, False)])
    isReadOnly = JavaMethod("()Z")