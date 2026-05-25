from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributedCharacterIterator"]

class AttributedCharacterIterator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/AttributedCharacterIterator"
    getRunStart = JavaMultipleMethod([("()I", False, False), ("(Ljava/text/AttributedCharacterIterator$Attribute;)I", False, False), ("(Ljava/util/Set;)I", False, False)])
    getRunLimit = JavaMultipleMethod([("()I", False, False), ("(Ljava/text/AttributedCharacterIterator$Attribute;)I", False, False), ("(Ljava/util/Set;)I", False, False)])
    getAttributes = JavaMethod("()Ljava/util/Map;")
    getAttribute = JavaMethod("(Ljava/text/AttributedCharacterIterator$Attribute;)Ljava/lang/Object;")
    getAllAttributeKeys = JavaMethod("()Ljava/util/Set;")

    class Attribute(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/text/AttributedCharacterIterator/Attribute"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        INPUT_METHOD_SEGMENT = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
        LANGUAGE = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
        READING = JavaStaticField("Ljava/text/AttributedCharacterIterator$Attribute;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")
        getName = JavaMethod("()Ljava/lang/String;")
        readResolve = JavaMethod("()Ljava/lang/Object;")