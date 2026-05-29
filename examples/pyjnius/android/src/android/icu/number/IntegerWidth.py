from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntegerWidth"]

class IntegerWidth(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/IntegerWidth"
    zeroFillTo = JavaStaticMethod("(I)Landroid/icu/number/IntegerWidth;")
    truncateAt = JavaMethod("(I)Landroid/icu/number/IntegerWidth;")