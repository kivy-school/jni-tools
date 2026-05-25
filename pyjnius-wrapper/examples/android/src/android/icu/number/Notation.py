from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Notation"]

class Notation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/Notation"
    scientific = JavaStaticMethod("()Landroid/icu/number/ScientificNotation;")
    engineering = JavaStaticMethod("()Landroid/icu/number/ScientificNotation;")
    compactShort = JavaStaticMethod("()Landroid/icu/number/CompactNotation;")
    compactLong = JavaStaticMethod("()Landroid/icu/number/CompactNotation;")
    simple = JavaStaticMethod("()Landroid/icu/number/SimpleNotation;")