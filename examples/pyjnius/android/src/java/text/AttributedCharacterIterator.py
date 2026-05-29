from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributedCharacterIterator"]

class AttributedCharacterIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/AttributedCharacterIterator"
    DONE = JavaStaticField("C")
    getAttributes = JavaMethod("()Ljava/util/Map;")
    getRunStart = JavaMultipleMethod([("(Ljava/util/Set;)I", False, False), ("(Ljava/text/AttributedCharacterIterator$Attribute;)I", False, False), ("()I", False, False)])
    getRunLimit = JavaMultipleMethod([("(Ljava/util/Set;)I", False, False), ("(Ljava/text/AttributedCharacterIterator$Attribute;)I", False, False), ("()I", False, False)])
    getAllAttributeKeys = JavaMethod("()Ljava/util/Set;")
    getAttribute = JavaMethod("(Ljava/text/AttributedCharacterIterator$Attribute;)Ljava/lang/Object;")

    class Attribute(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/text/AttributedCharacterIterator$Attribute"
        LANGUAGE = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
        READING = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
        INPUT_METHOD_SEGMENT = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")