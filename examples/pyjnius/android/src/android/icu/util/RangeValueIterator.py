from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangeValueIterator"]

class RangeValueIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/RangeValueIterator"
    reset = JavaMethod("()V")
    next = JavaMethod("(Landroid/icu/util/RangeValueIterator$Element;)Z")

    class Element(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/util/RangeValueIterator$Element"
        __javaconstructor__ = [("()V", False)]
        limit = JavaField("I")
        start = JavaField("I")
        value = JavaField("I")