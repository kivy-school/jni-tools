from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ErrorListener"]

class ErrorListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/ErrorListener"
    warning = JavaMethod("(Ljavax/xml/transform/TransformerException;)V")
    error = JavaMethod("(Ljavax/xml/transform/TransformerException;)V")
    fatalError = JavaMethod("(Ljavax/xml/transform/TransformerException;)V")