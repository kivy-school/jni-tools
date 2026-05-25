from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangeValueIterator"]

class RangeValueIterator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/RangeValueIterator"
    next = JavaMethod("(Landroid/icu/util/RangeValueIterator$Element;)Z")
    reset = JavaMethod("()V")

    class Element(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/util/RangeValueIterator/Element"
        __javaconstructor__ = [("()V", False)]
        limit = JavaField("I")
        start = JavaField("I")
        value = JavaField("I")