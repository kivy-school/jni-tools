from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Permission"]

class Permission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Permission"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getActions = JavaMethod("()Ljava/lang/String;")
    checkGuard = JavaMethod("(Ljava/lang/Object;)V")
    newPermissionCollection = JavaMethod("()Ljava/security/PermissionCollection;")