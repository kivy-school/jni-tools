from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatatypeConfigurationException"]

class DatatypeConfigurationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/datatype/DatatypeConfigurationException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]