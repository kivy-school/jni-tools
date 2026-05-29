from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LexicalHandler"]

class LexicalHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/LexicalHandler"
    startDTD = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    endDTD = JavaMethod("()V")
    startEntity = JavaMethod("(Ljava/lang/String;)V")
    endEntity = JavaMethod("(Ljava/lang/String;)V")
    startCDATA = JavaMethod("()V")
    endCDATA = JavaMethod("()V")
    comment = JavaMethod("([CII)V")