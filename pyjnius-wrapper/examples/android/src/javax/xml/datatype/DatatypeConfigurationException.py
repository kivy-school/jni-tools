from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatatypeConfigurationException"]

class DatatypeConfigurationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/datatype/DatatypeConfigurationException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False)]
    printStackTrace = JavaMultipleMethod([("()V", False, False), ("(Ljava/io/PrintStream;)V", False, False), ("(Ljava/io/PrintWriter;)V", False, False)])