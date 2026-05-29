from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransformerFactoryConfigurationError"]

class TransformerFactoryConfigurationError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/TransformerFactoryConfigurationError"
    __javaconstructor__ = [("(Ljava/lang/Exception;Ljava/lang/String;)V", False), ("(Ljava/lang/Exception;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]
    getCause = JavaMethod("()Ljava/lang/Throwable;")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getException = JavaMethod("()Ljava/lang/Exception;")