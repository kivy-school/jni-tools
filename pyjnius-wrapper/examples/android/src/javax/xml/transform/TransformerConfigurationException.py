from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransformerConfigurationException"]

class TransformerConfigurationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/TransformerConfigurationException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljavax/xml/transform/SourceLocator;)V", False), ("(Ljava/lang/String;Ljavax/xml/transform/SourceLocator;Ljava/lang/Throwable;)V", False)]