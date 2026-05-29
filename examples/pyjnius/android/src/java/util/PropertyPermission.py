from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyPermission"]

class PropertyPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/PropertyPermission"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getActions = JavaMethod("()Ljava/lang/String;")
    newPermissionCollection = JavaMethod("()Ljava/security/PermissionCollection;")