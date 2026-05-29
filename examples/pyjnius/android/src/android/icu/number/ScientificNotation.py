from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScientificNotation"]

class ScientificNotation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/ScientificNotation"
    withMinExponentDigits = JavaMethod("(I)Landroid/icu/number/ScientificNotation;")
    withExponentSignDisplay = JavaMethod("(Landroid/icu/number/NumberFormatter$SignDisplay;)Landroid/icu/number/ScientificNotation;")