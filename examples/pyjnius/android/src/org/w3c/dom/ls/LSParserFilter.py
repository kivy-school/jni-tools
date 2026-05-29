from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LSParserFilter"]

class LSParserFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSParserFilter"
    FILTER_ACCEPT = JavaStaticField("S")
    FILTER_REJECT = JavaStaticField("S")
    FILTER_SKIP = JavaStaticField("S")
    FILTER_INTERRUPT = JavaStaticField("S")
    acceptNode = JavaMethod("(Lorg/w3c/dom/Node;)S")
    getWhatToShow = JavaMethod("()I")
    startElement = JavaMethod("(Lorg/w3c/dom/Element;)S")