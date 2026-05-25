from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FormattedValue"]

class FormattedValue(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/FormattedValue"
    toString = JavaMethod("()Ljava/lang/String;")
    appendTo = JavaMethod("(Ljava/lang/Appendable;)Ljava/lang/Appendable;")
    nextPosition = JavaMethod("(Landroid/icu/text/ConstrainedFieldPosition;)Z")
    toCharacterIterator = JavaMethod("()Ljava/text/AttributedCharacterIterator;")