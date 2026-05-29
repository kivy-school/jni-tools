from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeclHandler"]

class DeclHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/DeclHandler"
    elementDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    attributeDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    internalEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    externalEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")