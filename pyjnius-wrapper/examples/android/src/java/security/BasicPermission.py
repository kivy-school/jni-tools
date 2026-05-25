from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BasicPermission"]

class BasicPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/BasicPermission"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getActions = JavaMethod("()Ljava/lang/String;")