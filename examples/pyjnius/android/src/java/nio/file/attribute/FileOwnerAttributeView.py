from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileOwnerAttributeView"]

class FileOwnerAttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/FileOwnerAttributeView"
    name = JavaMethod("()Ljava/lang/String;")
    getOwner = JavaMethod("()Ljava/nio/file/attribute/UserPrincipal;")
    setOwner = JavaMethod("(Ljava/nio/file/attribute/UserPrincipal;)V")