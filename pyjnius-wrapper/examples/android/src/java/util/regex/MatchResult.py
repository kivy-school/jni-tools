from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MatchResult"]

class MatchResult(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/regex/MatchResult"
    start = JavaMultipleMethod([("()I", False, False), ("(I)I", False, False)])
    end = JavaMultipleMethod([("()I", False, False), ("(I)I", False, False)])
    group = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])
    groupCount = JavaMethod("()I")