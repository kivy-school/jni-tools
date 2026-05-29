from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Scale"]

class Scale(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/Scale"
    powerOfTen = JavaStaticMethod("(I)Landroid/icu/number/Scale;")
    byBigDecimal = JavaStaticMethod("(Ljava/math/BigDecimal;)Landroid/icu/number/Scale;")
    byDouble = JavaStaticMethod("(D)Landroid/icu/number/Scale;")
    byDoubleAndPowerOfTen = JavaStaticMethod("(DI)Landroid/icu/number/Scale;")
    none = JavaStaticMethod("()Landroid/icu/number/Scale;")