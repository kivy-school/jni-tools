from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EntityResolver"]

class EntityResolver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/EntityResolver"
    resolveEntity = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")