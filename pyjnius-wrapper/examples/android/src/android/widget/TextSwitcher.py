from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextSwitcher"]

class TextSwitcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/TextSwitcher"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    addView = JavaMethod("(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V")
    setText = JavaMethod("(Ljava/lang/CharSequence;)V")
    setCurrentText = JavaMethod("(Ljava/lang/CharSequence;)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")