from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LSParser"]

class LSParser(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSParser"
    ACTION_APPEND_AS_CHILDREN = JavaStaticField("S")
    ACTION_INSERT_AFTER = JavaStaticField("S")
    ACTION_INSERT_BEFORE = JavaStaticField("S")
    ACTION_REPLACE = JavaStaticField("S")
    ACTION_REPLACE_CHILDREN = JavaStaticField("S")
    getDomConfig = JavaMethod("()Lorg/w3c/dom/DOMConfiguration;")
    getFilter = JavaMethod("()Lorg/w3c/dom/ls/LSParserFilter;")
    setFilter = JavaMethod("(Lorg/w3c/dom/ls/LSParserFilter;)V")
    getAsync = JavaMethod("()Z")
    getBusy = JavaMethod("()Z")
    parse = JavaMethod("(Lorg/w3c/dom/ls/LSInput;)Lorg/w3c/dom/Document;")
    parseURI = JavaMethod("(Ljava/lang/String;)Lorg/w3c/dom/Document;")
    parseWithContext = JavaMethod("(Lorg/w3c/dom/ls/LSInput;Lorg/w3c/dom/Node;S)Lorg/w3c/dom/Node;")
    abort = JavaMethod("()V")