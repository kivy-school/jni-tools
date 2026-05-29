from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MatchResult"]

class MatchResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/regex/MatchResult"
    namedGroups = JavaMethod("()Ljava/util/Map;")
    group = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("()Ljava/lang/String;", False, False)])
    end = JavaMultipleMethod([("()I", False, False), ("(Ljava/lang/String;)I", False, False), ("(I)I", False, False)])
    start = JavaMultipleMethod([("(I)I", False, False), ("(Ljava/lang/String;)I", False, False), ("()I", False, False)])
    hasMatch = JavaMethod("()Z")
    groupCount = JavaMethod("()I")