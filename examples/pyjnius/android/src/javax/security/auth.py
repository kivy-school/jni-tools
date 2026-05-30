from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SubjectDomainCombiner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/SubjectDomainCombiner"
    __javaconstructor__ = [("(Ljavax/security/auth/Subject;)V", False)]
    getSubject = JavaMethod("()Ljavax/security/auth/Subject;")
    combine = JavaMethod("([Ljava/security/ProtectionDomain;[Ljava/security/ProtectionDomain;)[Ljava/security/ProtectionDomain;")

class PrivateCredentialPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/PrivateCredentialPermission"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    newPermissionCollection = JavaMethod("()Ljava/security/PermissionCollection;")
    getCredentialClass = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getActions = JavaMethod("()Ljava/lang/String;")
    getPrincipals = JavaMethod("()[[Ljava/lang/String;")

class Subject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/Subject"
    __javaconstructor__ = [("()V", False), ("(ZLjava/util/Set;Ljava/util/Set;Ljava/util/Set;)V", False)]
    getSubject = JavaStaticMethod("(Ljava/security/AccessControlContext;)Ljavax/security/auth/Subject;")
    doAs = JavaMultipleMethod([("(Ljavax/security/auth/Subject;Ljava/security/PrivilegedExceptionAction;)Ljava/lang/Object;", True, False), ("(Ljavax/security/auth/Subject;Ljava/security/PrivilegedAction;)Ljava/lang/Object;", True, False)])
    callAs = JavaStaticMethod("(Ljavax/security/auth/Subject;Ljava/util/concurrent/Callable;)Ljava/lang/Object;")
    doAsPrivileged = JavaMultipleMethod([("(Ljavax/security/auth/Subject;Ljava/security/PrivilegedExceptionAction;Ljava/security/AccessControlContext;)Ljava/lang/Object;", True, False), ("(Ljavax/security/auth/Subject;Ljava/security/PrivilegedAction;Ljava/security/AccessControlContext;)Ljava/lang/Object;", True, False)])
    getPublicCredentials = JavaMultipleMethod([("(Ljava/lang/Class;)Ljava/util/Set;", False, False), ("()Ljava/util/Set;", False, False)])
    getPrivateCredentials = JavaMultipleMethod([("(Ljava/lang/Class;)Ljava/util/Set;", False, False), ("()Ljava/util/Set;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    setReadOnly = JavaMethod("()V")
    getPrincipals = JavaMultipleMethod([("()Ljava/util/Set;", False, False), ("(Ljava/lang/Class;)Ljava/util/Set;", False, False)])
    current = JavaStaticMethod("()Ljavax/security/auth/Subject;")
    isReadOnly = JavaMethod("()Z")

class Destroyable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/Destroyable"
    isDestroyed = JavaMethod("()Z")
    destroy = JavaMethod("()V")

class AuthPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/AuthPermission"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]

class DestroyFailedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/DestroyFailedException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]