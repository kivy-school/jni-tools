from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class RootElement(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/RootElement"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    getContentHandler = JavaMethod("()Lorg/xml/sax/ContentHandler;")

class TextElementListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/TextElementListener"

class Element(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/Element"
    requireChild = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/sax/Element;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Landroid/sax/Element;", False, False)])
    setElementListener = JavaMethod("(Landroid/sax/ElementListener;)V")
    setEndElementListener = JavaMethod("(Landroid/sax/EndElementListener;)V")
    setEndTextElementListener = JavaMethod("(Landroid/sax/EndTextElementListener;)V")
    setStartElementListener = JavaMethod("(Landroid/sax/StartElementListener;)V")
    setTextElementListener = JavaMethod("(Landroid/sax/TextElementListener;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    getChild = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Landroid/sax/Element;", False, False), ("(Ljava/lang/String;)Landroid/sax/Element;", False, False)])

class StartElementListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/StartElementListener"
    start = JavaMethod("(Lorg/xml/sax/Attributes;)V")

class EndElementListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/EndElementListener"
    end = JavaMethod("()V")

class EndTextElementListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/EndTextElementListener"
    end = JavaMethod("(Ljava/lang/String;)V")

class ElementListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/ElementListener"