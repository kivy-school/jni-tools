from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Subject"]

class Subject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/Subject"
    __javaconstructor__ = [("()V", False), ("(ZLjava/util/Set;Ljava/util/Set;Ljava/util/Set;)V", False)]
    setReadOnly = JavaMethod("()V")
    isReadOnly = JavaMethod("()Z")
    getSubject = JavaStaticMethod("(Ljava/security/AccessControlContext;)Ljavax/security/auth/Subject;")
    doAs = JavaMultipleMethod([("(Ljavax/security/auth/Subject;Ljava/security/PrivilegedAction;)Ljava/lang/Object;", True, False), ("(Ljavax/security/auth/Subject;Ljava/security/PrivilegedExceptionAction;)Ljava/lang/Object;", True, False)])
    doAsPrivileged = JavaMultipleMethod([("(Ljavax/security/auth/Subject;Ljava/security/PrivilegedAction;Ljava/security/AccessControlContext;)Ljava/lang/Object;", True, False), ("(Ljavax/security/auth/Subject;Ljava/security/PrivilegedExceptionAction;Ljava/security/AccessControlContext;)Ljava/lang/Object;", True, False)])
    getPrincipals = JavaMultipleMethod([("()Ljava/util/Set;", False, False), ("(Ljava/lang/Class;)Ljava/util/Set;", False, False)])
    getPublicCredentials = JavaMultipleMethod([("()Ljava/util/Set;", False, False), ("(Ljava/lang/Class;)Ljava/util/Set;", False, False)])
    getPrivateCredentials = JavaMultipleMethod([("()Ljava/util/Set;", False, False), ("(Ljava/lang/Class;)Ljava/util/Set;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")