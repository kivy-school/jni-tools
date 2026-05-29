from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Permissions"]

class Permissions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Permissions"
    __javaconstructor__ = [("()V", False)]
    add = JavaMethod("(Ljava/security/Permission;)V")
    elements = JavaMethod("()Ljava/util/Enumeration;")
    implies = JavaMethod("(Ljava/security/Permission;)Z")