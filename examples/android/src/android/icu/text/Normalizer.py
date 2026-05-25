from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Normalizer"]

class Normalizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/Normalizer"
    COMPARE_CODE_POINT_ORDER = JavaStaticField("I")
    COMPARE_IGNORE_CASE = JavaStaticField("I")
    FOLD_CASE_DEFAULT = JavaStaticField("I")
    FOLD_CASE_EXCLUDE_SPECIAL_I = JavaStaticField("I")
    INPUT_IS_FCD = JavaStaticField("I")
    MAYBE = JavaStaticField("Landroid/icu/text/Normalizer$QuickCheckResult;")
    NO = JavaStaticField("Landroid/icu/text/Normalizer$QuickCheckResult;")
    YES = JavaStaticField("Landroid/icu/text/Normalizer$QuickCheckResult;")
    clone = JavaMethod("()Ljava/lang/Object;")
    compare = JavaMultipleMethod([("([CII[CIII)I", True, False), ("(Ljava/lang/String;Ljava/lang/String;I)I", True, False), ("([C[CI)I", True, False), ("(III)I", True, False), ("(ILjava/lang/String;I)I", True, False)])

    class QuickCheckResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/Normalizer/QuickCheckResult"