from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Base64"]

class Base64(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Base64"
    CRLF = JavaStaticField("I")
    DEFAULT = JavaStaticField("I")
    NO_CLOSE = JavaStaticField("I")
    NO_PADDING = JavaStaticField("I")
    NO_WRAP = JavaStaticField("I")
    URL_SAFE = JavaStaticField("I")
    decode = JavaMultipleMethod([("(Ljava/lang/String;I)[B", True, False), ("([BIII)[B", True, False), ("([BI)[B", True, False)])
    encode = JavaMultipleMethod([("([BIII)[B", True, False), ("([BI)[B", True, False)])
    encodeToString = JavaMultipleMethod([("([BI)Ljava/lang/String;", True, False), ("([BIII)Ljava/lang/String;", True, False)])