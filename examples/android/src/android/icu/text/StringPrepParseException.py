from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringPrepParseException"]

class StringPrepParseException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/StringPrepParseException"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False), ("(Ljava/lang/String;ILjava/lang/String;I)V", False), ("(Ljava/lang/String;ILjava/lang/String;II)V", False)]
    ACE_PREFIX_ERROR = JavaStaticField("I")
    BUFFER_OVERFLOW_ERROR = JavaStaticField("I")
    CHECK_BIDI_ERROR = JavaStaticField("I")
    DOMAIN_NAME_TOO_LONG_ERROR = JavaStaticField("I")
    ILLEGAL_CHAR_FOUND = JavaStaticField("I")
    INVALID_CHAR_FOUND = JavaStaticField("I")
    LABEL_TOO_LONG_ERROR = JavaStaticField("I")
    PROHIBITED_ERROR = JavaStaticField("I")
    STD3_ASCII_RULES_ERROR = JavaStaticField("I")
    UNASSIGNED_ERROR = JavaStaticField("I")
    VERIFICATION_ERROR = JavaStaticField("I")
    ZERO_LENGTH_LABEL = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getError = JavaMethod("()I")