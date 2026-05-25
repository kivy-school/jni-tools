from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Matcher"]

class Matcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/regex/Matcher"
    pattern = JavaMethod("()Ljava/util/regex/Pattern;")
    toMatchResult = JavaMethod("()Ljava/util/regex/MatchResult;")
    usePattern = JavaMethod("(Ljava/util/regex/Pattern;)Ljava/util/regex/Matcher;")
    reset = JavaMultipleMethod([("()Ljava/util/regex/Matcher;", False, False), ("(Ljava/lang/CharSequence;)Ljava/util/regex/Matcher;", False, False)])
    start = JavaMultipleMethod([("()I", False, False), ("(I)I", False, False), ("(Ljava/lang/String;)I", False, False)])
    end = JavaMultipleMethod([("()I", False, False), ("(I)I", False, False), ("(Ljava/lang/String;)I", False, False)])
    group = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    groupCount = JavaMethod("()I")
    matches = JavaMethod("()Z")
    find = JavaMultipleMethod([("()Z", False, False), ("(I)Z", False, False)])
    lookingAt = JavaMethod("()Z")
    quoteReplacement = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    appendReplacement = JavaMultipleMethod([("(Ljava/lang/StringBuffer;Ljava/lang/String;)Ljava/util/regex/Matcher;", False, False), ("(Ljava/lang/StringBuilder;Ljava/lang/String;)Ljava/util/regex/Matcher;", False, False)])
    appendTail = JavaMultipleMethod([("(Ljava/lang/StringBuffer;)Ljava/lang/StringBuffer;", False, False), ("(Ljava/lang/StringBuilder;)Ljava/lang/StringBuilder;", False, False)])
    replaceAll = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/util/function/Function;)Ljava/lang/String;", False, False)])
    results = JavaMethod("()Ljava/util/stream/Stream;")
    replaceFirst = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/util/function/Function;)Ljava/lang/String;", False, False)])
    region = JavaMethod("(II)Ljava/util/regex/Matcher;")
    regionStart = JavaMethod("()I")
    regionEnd = JavaMethod("()I")
    hasTransparentBounds = JavaMethod("()Z")
    useTransparentBounds = JavaMethod("(Z)Ljava/util/regex/Matcher;")
    hasAnchoringBounds = JavaMethod("()Z")
    useAnchoringBounds = JavaMethod("(Z)Ljava/util/regex/Matcher;")
    toString = JavaMethod("()Ljava/lang/String;")
    hitEnd = JavaMethod("()Z")
    requireEnd = JavaMethod("()Z")