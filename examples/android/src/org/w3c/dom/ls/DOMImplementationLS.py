from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMImplementationLS"]

class DOMImplementationLS(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/DOMImplementationLS"
    MODE_ASYNCHRONOUS = JavaStaticField("S")
    MODE_SYNCHRONOUS = JavaStaticField("S")
    createLSParser = JavaMethod("(SLjava/lang/String;)Lorg/w3c/dom/ls/LSParser;")
    createLSSerializer = JavaMethod("()Lorg/w3c/dom/ls/LSSerializer;")
    createLSInput = JavaMethod("()Lorg/w3c/dom/ls/LSInput;")
    createLSOutput = JavaMethod("()Lorg/w3c/dom/ls/LSOutput;")