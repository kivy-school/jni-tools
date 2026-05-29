from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FactoryConfigurationError"]

class FactoryConfigurationError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/parsers/FactoryConfigurationError"
    __javaconstructor__ = [("(Ljava/lang/Exception;Ljava/lang/String;)V", False), ("(Ljava/lang/Exception;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]
    getCause = JavaMethod("()Ljava/lang/Throwable;")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getException = JavaMethod("()Ljava/lang/Exception;")