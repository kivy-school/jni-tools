from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransformerHandler"]

class TransformerHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/TransformerHandler"
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setResult = JavaMethod("(Ljavax/xml/transform/Result;)V")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getTransformer = JavaMethod("()Ljavax/xml/transform/Transformer;")