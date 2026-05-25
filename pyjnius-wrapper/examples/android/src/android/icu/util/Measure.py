from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Measure"]

class Measure(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/Measure"
    __javaconstructor__ = [("(Ljava/lang/Number;Landroid/icu/util/MeasureUnit;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getNumber = JavaMethod("()Ljava/lang/Number;")
    getUnit = JavaMethod("()Landroid/icu/util/MeasureUnit;")