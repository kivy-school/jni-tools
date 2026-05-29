from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EntityResolver2"]

class EntityResolver2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/EntityResolver2"
    resolveEntity = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")
    getExternalSubset = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")