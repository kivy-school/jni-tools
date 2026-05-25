from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransformerHandler"]

class TransformerHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/TransformerHandler"
    setResult = JavaMethod("(Ljavax/xml/transform/Result;)V")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getTransformer = JavaMethod("()Ljavax/xml/transform/Transformer;")