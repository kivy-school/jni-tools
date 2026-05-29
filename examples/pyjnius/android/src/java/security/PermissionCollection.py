from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PermissionCollection"]

class PermissionCollection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PermissionCollection"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    add = JavaMethod("(Ljava/security/Permission;)V")
    elements = JavaMethod("()Ljava/util/Enumeration;")
    setReadOnly = JavaMethod("()V")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    isReadOnly = JavaMethod("()Z")
    elementsAsStream = JavaMethod("()Ljava/util/stream/Stream;")