from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnresolvedPermission"]

class UnresolvedPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/UnresolvedPermission"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;[Ljava/security/cert/Certificate;)V", False)]
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getActions = JavaMethod("()Ljava/lang/String;")
    getUnresolvedType = JavaMethod("()Ljava/lang/String;")
    getUnresolvedName = JavaMethod("()Ljava/lang/String;")
    getUnresolvedActions = JavaMethod("()Ljava/lang/String;")
    getUnresolvedCerts = JavaMethod("()[Ljava/security/cert/Certificate;")