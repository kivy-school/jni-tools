from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Chronometer"]

class Chronometer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Chronometer"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    setCountDown = JavaMethod("(Z)V")
    isCountDown = JavaMethod("()Z")
    isTheFinalCountDown = JavaMethod("()Z")
    setBase = JavaMethod("(J)V")
    getBase = JavaMethod("()J")
    setFormat = JavaMethod("(Ljava/lang/String;)V")
    getFormat = JavaMethod("()Ljava/lang/String;")
    setOnChronometerTickListener = JavaMethod("(Landroid/widget/Chronometer$OnChronometerTickListener;)V")
    getOnChronometerTickListener = JavaMethod("()Landroid/widget/Chronometer$OnChronometerTickListener;")
    start = JavaMethod("()V")
    stop = JavaMethod("()V")
    onDetachedFromWindow = JavaMethod("()V")
    onWindowVisibilityChanged = JavaMethod("(I)V")
    onVisibilityChanged = JavaMethod("(Landroid/view/View;I)V")
    getContentDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")

    class OnChronometerTickListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/Chronometer/OnChronometerTickListener"
        onChronometerTick = JavaMethod("(Landroid/widget/Chronometer;)V")