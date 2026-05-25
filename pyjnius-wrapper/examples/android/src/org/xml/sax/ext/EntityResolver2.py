from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EntityResolver2"]

class EntityResolver2(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/EntityResolver2"
    getExternalSubset = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")
    resolveEntity = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")