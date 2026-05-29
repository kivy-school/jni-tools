from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Element"]

class Element(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/Element"
    setElementListener = JavaMethod("(Landroid/sax/ElementListener;)V")
    requireChild = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Landroid/sax/Element;", False, False), ("(Ljava/lang/String;)Landroid/sax/Element;", False, False)])
    setEndElementListener = JavaMethod("(Landroid/sax/EndElementListener;)V")
    setEndTextElementListener = JavaMethod("(Landroid/sax/EndTextElementListener;)V")
    setStartElementListener = JavaMethod("(Landroid/sax/StartElementListener;)V")
    setTextElementListener = JavaMethod("(Landroid/sax/TextElementListener;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    getChild = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Landroid/sax/Element;", False, False), ("(Ljava/lang/String;)Landroid/sax/Element;", False, False)])