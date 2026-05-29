from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParserConfigurationException"]

class ParserConfigurationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/parsers/ParserConfigurationException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]