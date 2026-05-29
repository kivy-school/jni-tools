from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Measure"]

class Measure(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/Measure"
    __javaconstructor__ = [("(Ljava/lang/Number;Landroid/icu/util/MeasureUnit;)V", False)]
    getUnit = JavaMethod("()Landroid/icu/util/MeasureUnit;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getNumber = JavaMethod("()Ljava/lang/Number;")