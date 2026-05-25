from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransformerFactoryConfigurationError"]

class TransformerFactoryConfigurationError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/TransformerFactoryConfigurationError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/Exception;)V", False), ("(Ljava/lang/Exception;Ljava/lang/String;)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getException = JavaMethod("()Ljava/lang/Exception;")