from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LSException"]

class LSException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSException"
    __javaconstructor__ = [("(SLjava/lang/String;)V", False)]
    code = JavaField("S")
    PARSE_ERR = JavaStaticField("S")
    SERIALIZE_ERR = JavaStaticField("S")