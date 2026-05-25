from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SNIMatcher"]

class SNIMatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SNIMatcher"
    __javaconstructor__ = [("(I)V", False)]
    getType = JavaMethod("()I")
    matches = JavaMethod("(Ljavax/net/ssl/SNIServerName;)Z")