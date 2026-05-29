from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URIResolver"]

class URIResolver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/URIResolver"
    resolve = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljavax/xml/transform/Source;")