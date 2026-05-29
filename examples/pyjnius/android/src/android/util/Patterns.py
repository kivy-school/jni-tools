from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Patterns"]

class Patterns(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Patterns"
    DOMAIN_NAME = JavaStaticField("Ljava/util/regex/Pattern;")
    EMAIL_ADDRESS = JavaStaticField("Ljava/util/regex/Pattern;")
    GOOD_IRI_CHAR = JavaStaticField("Ljava/lang/String;")
    IP_ADDRESS = JavaStaticField("Ljava/util/regex/Pattern;")
    PHONE = JavaStaticField("Ljava/util/regex/Pattern;")
    TOP_LEVEL_DOMAIN = JavaStaticField("Ljava/util/regex/Pattern;")
    TOP_LEVEL_DOMAIN_STR = JavaStaticField("Ljava/lang/String;")
    TOP_LEVEL_DOMAIN_STR_FOR_WEB_URL = JavaStaticField("Ljava/lang/String;")
    WEB_URL = JavaStaticField("Ljava/util/regex/Pattern;")
    concatGroups = JavaStaticMethod("(Ljava/util/regex/Matcher;)Ljava/lang/String;")
    digitsAndPlusOnly = JavaStaticMethod("(Ljava/util/regex/Matcher;)Ljava/lang/String;")