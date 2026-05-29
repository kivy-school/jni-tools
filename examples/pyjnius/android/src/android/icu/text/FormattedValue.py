from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FormattedValue"]

class FormattedValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/FormattedValue"
    appendTo = JavaMethod("(Ljava/lang/Appendable;)Ljava/lang/Appendable;")
    nextPosition = JavaMethod("(Landroid/icu/text/ConstrainedFieldPosition;)Z")
    toCharacterIterator = JavaMethod("()Ljava/text/AttributedCharacterIterator;")
    toString = JavaMethod("()Ljava/lang/String;")