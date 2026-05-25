from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransformerFactory"]

class TransformerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/TransformerFactory"
    __javaconstructor__ = [("()V", False)]
    newInstance = JavaMultipleMethod([("()Ljavax/xml/transform/TransformerFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/transform/TransformerFactory;", True, False)])
    newTransformer = JavaMultipleMethod([("(Ljavax/xml/transform/Source;)Ljavax/xml/transform/Transformer;", False, False), ("()Ljavax/xml/transform/Transformer;", False, False)])
    newTemplates = JavaMethod("(Ljavax/xml/transform/Source;)Ljavax/xml/transform/Templates;")
    getAssociatedStylesheet = JavaMethod("(Ljavax/xml/transform/Source;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljavax/xml/transform/Source;")
    setURIResolver = JavaMethod("(Ljavax/xml/transform/URIResolver;)V")
    getURIResolver = JavaMethod("()Ljavax/xml/transform/URIResolver;")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    setErrorListener = JavaMethod("(Ljavax/xml/transform/ErrorListener;)V")
    getErrorListener = JavaMethod("()Ljavax/xml/transform/ErrorListener;")