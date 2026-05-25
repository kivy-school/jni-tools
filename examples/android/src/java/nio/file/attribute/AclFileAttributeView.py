from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AclFileAttributeView"]

class AclFileAttributeView(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/AclFileAttributeView"
    name = JavaMethod("()Ljava/lang/String;")
    getAcl = JavaMethod("()Ljava/util/List;")
    setAcl = JavaMethod("(Ljava/util/List;)V")