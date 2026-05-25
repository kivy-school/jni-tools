from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextClock"]

class TextClock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/TextClock"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    DEFAULT_FORMAT_12_HOUR = JavaStaticField("Ljava/lang/CharSequence;")
    DEFAULT_FORMAT_24_HOUR = JavaStaticField("Ljava/lang/CharSequence;")
    getFormat12Hour = JavaMethod("()Ljava/lang/CharSequence;")
    setFormat12Hour = JavaMethod("(Ljava/lang/CharSequence;)V")
    getFormat24Hour = JavaMethod("()Ljava/lang/CharSequence;")
    setFormat24Hour = JavaMethod("(Ljava/lang/CharSequence;)V")
    refreshTime = JavaMethod("()V")
    is24HourModeEnabled = JavaMethod("()Z")
    getTimeZone = JavaMethod("()Ljava/lang/String;")
    setTimeZone = JavaMethod("(Ljava/lang/String;)V")
    onAttachedToWindow = JavaMethod("()V")
    onVisibilityAggregated = JavaMethod("(Z)V")
    onDetachedFromWindow = JavaMethod("()V")