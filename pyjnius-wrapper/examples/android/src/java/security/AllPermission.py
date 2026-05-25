from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AllPermission"]

class AllPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AllPermission"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getActions = JavaMethod("()Ljava/lang/String;")