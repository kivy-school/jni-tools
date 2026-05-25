from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Permission"]

class Permission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Permission"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    checkGuard = JavaMethod("(Ljava/lang/Object;)V")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getName = JavaMethod("()Ljava/lang/String;")
    getActions = JavaMethod("()Ljava/lang/String;")
    newPermissionCollection = JavaMethod("()Ljava/security/PermissionCollection;")