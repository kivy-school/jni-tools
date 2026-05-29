from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URIResolver"]

class URIResolver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/URIResolver"
    resolve = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljavax/xml/transform/Source;")