from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewSwitcher"]

class ViewSwitcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ViewSwitcher"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    addView = JavaMethod("(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    getNextView = JavaMethod("()Landroid/view/View;")
    setFactory = JavaMethod("(Landroid/widget/ViewSwitcher$ViewFactory;)V")
    reset = JavaMethod("()V")

    class ViewFactory(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/ViewSwitcher/ViewFactory"
        makeView = JavaMethod("()Landroid/view/View;")