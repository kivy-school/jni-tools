from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Transformer"]

class Transformer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/Transformer"
    clearParameters = JavaMethod("()V")
    setParameter = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getParameter = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    reset = JavaMethod("()V")
    transform = JavaMethod("(Ljavax/xml/transform/Source;Ljavax/xml/transform/Result;)V")
    setURIResolver = JavaMethod("(Ljavax/xml/transform/URIResolver;)V")
    getURIResolver = JavaMethod("()Ljavax/xml/transform/URIResolver;")
    setOutputProperties = JavaMethod("(Ljava/util/Properties;)V")
    getOutputProperties = JavaMethod("()Ljava/util/Properties;")
    setOutputProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    getOutputProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    setErrorListener = JavaMethod("(Ljavax/xml/transform/ErrorListener;)V")
    getErrorListener = JavaMethod("()Ljavax/xml/transform/ErrorListener;")