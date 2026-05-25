from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Element"]

class Element(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/Element"
    getChild = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/sax/Element;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Landroid/sax/Element;", False, False)])
    requireChild = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/sax/Element;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Landroid/sax/Element;", False, False)])
    setElementListener = JavaMethod("(Landroid/sax/ElementListener;)V")
    setTextElementListener = JavaMethod("(Landroid/sax/TextElementListener;)V")
    setStartElementListener = JavaMethod("(Landroid/sax/StartElementListener;)V")
    setEndElementListener = JavaMethod("(Landroid/sax/EndElementListener;)V")
    setEndTextElementListener = JavaMethod("(Landroid/sax/EndTextElementListener;)V")
    toString = JavaMethod("()Ljava/lang/String;")