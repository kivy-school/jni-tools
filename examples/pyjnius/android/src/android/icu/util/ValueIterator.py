from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ValueIterator"]

class ValueIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/ValueIterator"
    setRange = JavaMethod("(II)V")
    reset = JavaMethod("()V")
    next = JavaMethod("(Landroid/icu/util/ValueIterator$Element;)Z")

    class Element(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/util/ValueIterator$Element"
        __javaconstructor__ = [("()V", False)]
        integer = JavaField("I")
        value = JavaField("Ljava/lang/Object;")