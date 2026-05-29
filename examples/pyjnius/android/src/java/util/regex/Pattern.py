from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Pattern"]

class Pattern(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/regex/Pattern"
    UNIX_LINES = JavaStaticField("I")
    CASE_INSENSITIVE = JavaStaticField("I")
    COMMENTS = JavaStaticField("I")
    MULTILINE = JavaStaticField("I")
    LITERAL = JavaStaticField("I")
    DOTALL = JavaStaticField("I")
    UNICODE_CASE = JavaStaticField("I")
    CANON_EQ = JavaStaticField("I")
    UNICODE_CHARACTER_CLASS = JavaStaticField("I")
    namedGroups = JavaMethod("()Ljava/util/Map;")
    toString = JavaMethod("()Ljava/lang/String;")
    flags = JavaMethod("()I")
    matches = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/CharSequence;)Z")
    compile = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/util/regex/Pattern;", True, False), ("(Ljava/lang/String;I)Ljava/util/regex/Pattern;", True, False)])
    matcher = JavaMethod("(Ljava/lang/CharSequence;)Ljava/util/regex/Matcher;")
    split = JavaMultipleMethod([("(Ljava/lang/CharSequence;I)[Ljava/lang/String;", False, False), ("(Ljava/lang/CharSequence;)[Ljava/lang/String;", False, False)])
    splitWithDelimiters = JavaMethod("(Ljava/lang/CharSequence;I)[Ljava/lang/String;")
    pattern = JavaMethod("()Ljava/lang/String;")
    asPredicate = JavaMethod("()Ljava/util/function/Predicate;")
    asMatchPredicate = JavaMethod("()Ljava/util/function/Predicate;")
    splitAsStream = JavaMethod("(Ljava/lang/CharSequence;)Ljava/util/stream/Stream;")
    quote = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")