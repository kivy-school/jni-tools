from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceConfigurationError"]

class ServiceConfigurationError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/ServiceConfigurationError"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]