from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributedString"]

class AttributedString(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/AttributedString"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/util/Map;)V", False), ("(Ljava/text/AttributedCharacterIterator;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/text/AttributedCharacterIterator;II[Ljava/text/AttributedCharacterIterator$Attribute;)V", False), ("(Ljava/text/AttributedCharacterIterator;II)V", False)]
    addAttributes = JavaMethod("(Ljava/util/Map;II)V")
    getIterator = JavaMultipleMethod([("()Ljava/text/AttributedCharacterIterator;", False, False), ("([Ljava/text/AttributedCharacterIterator$Attribute;)Ljava/text/AttributedCharacterIterator;", False, False), ("([Ljava/text/AttributedCharacterIterator$Attribute;II)Ljava/text/AttributedCharacterIterator;", False, False)])
    addAttribute = JavaMultipleMethod([("(Ljava/text/AttributedCharacterIterator$Attribute;Ljava/lang/Object;)V", False, False), ("(Ljava/text/AttributedCharacterIterator$Attribute;Ljava/lang/Object;II)V", False, False)])