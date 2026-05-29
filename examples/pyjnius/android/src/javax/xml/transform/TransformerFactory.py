from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransformerFactory"]

class TransformerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/TransformerFactory"
    newInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/transform/TransformerFactory;", True, False), ("()Ljavax/xml/transform/TransformerFactory;", True, False)])
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    newDefaultInstance = JavaStaticMethod("()Ljavax/xml/transform/TransformerFactory;")
    setURIResolver = JavaMethod("(Ljavax/xml/transform/URIResolver;)V")
    getURIResolver = JavaMethod("()Ljavax/xml/transform/URIResolver;")
    setErrorListener = JavaMethod("(Ljavax/xml/transform/ErrorListener;)V")
    getErrorListener = JavaMethod("()Ljavax/xml/transform/ErrorListener;")
    newTransformer = JavaMultipleMethod([("(Ljavax/xml/transform/Source;)Ljavax/xml/transform/Transformer;", False, False), ("()Ljavax/xml/transform/Transformer;", False, False)])
    newTemplates = JavaMethod("(Ljavax/xml/transform/Source;)Ljavax/xml/transform/Templates;")
    getAssociatedStylesheet = JavaMethod("(Ljavax/xml/transform/Source;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljavax/xml/transform/Source;")
    getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")