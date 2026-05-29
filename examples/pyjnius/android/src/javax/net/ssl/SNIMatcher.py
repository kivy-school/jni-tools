from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SNIMatcher"]

class SNIMatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SNIMatcher"
    matches = JavaMethod("(Ljavax/net/ssl/SNIServerName;)Z")
    getType = JavaMethod("()I")