from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Pattern"]

class Pattern(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/regex/Pattern"
    CANON_EQ = JavaStaticField("I")
    CASE_INSENSITIVE = JavaStaticField("I")
    COMMENTS = JavaStaticField("I")
    DOTALL = JavaStaticField("I")
    LITERAL = JavaStaticField("I")
    MULTILINE = JavaStaticField("I")
    UNICODE_CASE = JavaStaticField("I")
    UNICODE_CHARACTER_CLASS = JavaStaticField("I")
    UNIX_LINES = JavaStaticField("I")
    compile = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/util/regex/Pattern;", True, False), ("(Ljava/lang/String;I)Ljava/util/regex/Pattern;", True, False)])
    pattern = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    matcher = JavaMethod("(Ljava/lang/CharSequence;)Ljava/util/regex/Matcher;")
    flags = JavaMethod("()I")
    matches = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/CharSequence;)Z")
    split = JavaMultipleMethod([("(Ljava/lang/CharSequence;I)[Ljava/lang/String;", False, False), ("(Ljava/lang/CharSequence;)[Ljava/lang/String;", False, False)])
    quote = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    asPredicate = JavaMethod("()Ljava/util/function/Predicate;")
    asMatchPredicate = JavaMethod("()Ljava/util/function/Predicate;")
    splitAsStream = JavaMethod("(Ljava/lang/CharSequence;)Ljava/util/stream/Stream;")