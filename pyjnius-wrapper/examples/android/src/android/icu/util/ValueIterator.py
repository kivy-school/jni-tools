from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ValueIterator"]

class ValueIterator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/ValueIterator"
    next = JavaMethod("(Landroid/icu/util/ValueIterator$Element;)Z")
    reset = JavaMethod("()V")
    setRange = JavaMethod("(II)V")

    class Element(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/util/ValueIterator/Element"
        __javaconstructor__ = [("()V", False)]
        integer = JavaField("I")
        value = JavaField("Ljava/lang/Object;")