from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessControlException"]

class AccessControlException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AccessControlException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/security/Permission;)V", False)]
    getPermission = JavaMethod("()Ljava/security/Permission;")