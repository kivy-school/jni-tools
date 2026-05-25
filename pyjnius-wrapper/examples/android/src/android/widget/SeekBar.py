from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SeekBar"]

class SeekBar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/SeekBar"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    setOnSeekBarChangeListener = JavaMethod("(Landroid/widget/SeekBar$OnSeekBarChangeListener;)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")

    class OnSeekBarChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SeekBar/OnSeekBarChangeListener"
        onProgressChanged = JavaMethod("(Landroid/widget/SeekBar;IZ)V")
        onStartTrackingTouch = JavaMethod("(Landroid/widget/SeekBar;)V")
        onStopTrackingTouch = JavaMethod("(Landroid/widget/SeekBar;)V")