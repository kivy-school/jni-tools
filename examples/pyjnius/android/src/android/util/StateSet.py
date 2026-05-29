from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StateSet"]

class StateSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/StateSet"
    NOTHING = JavaStaticField("[I")
    WILD_CARD = JavaStaticField("[I")
    stateSetMatches = JavaMultipleMethod([("([I[I)Z", True, False), ("([II)Z", True, False)])
    trimStateSet = JavaStaticMethod("([II)[I")
    isWildCard = JavaStaticMethod("([I)Z")
    dump = JavaStaticMethod("([I)Ljava/lang/String;")