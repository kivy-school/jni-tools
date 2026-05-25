from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewAnimator"]

class ViewAnimator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ViewAnimator"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    setDisplayedChild = JavaMethod("(I)V")
    getDisplayedChild = JavaMethod("()I")
    showNext = JavaMethod("()V")
    showPrevious = JavaMethod("()V")
    addView = JavaMethod("(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V")
    removeAllViews = JavaMethod("()V")
    removeView = JavaMethod("(Landroid/view/View;)V")
    removeViewAt = JavaMethod("(I)V")
    removeViewInLayout = JavaMethod("(Landroid/view/View;)V")
    removeViews = JavaMethod("(II)V")
    removeViewsInLayout = JavaMethod("(II)V")
    getCurrentView = JavaMethod("()Landroid/view/View;")
    getInAnimation = JavaMethod("()Landroid/view/animation/Animation;")
    setInAnimation = JavaMultipleMethod([("(Landroid/view/animation/Animation;)V", False, False), ("(Landroid/content/Context;I)V", False, False)])
    getOutAnimation = JavaMethod("()Landroid/view/animation/Animation;")
    setOutAnimation = JavaMultipleMethod([("(Landroid/view/animation/Animation;)V", False, False), ("(Landroid/content/Context;I)V", False, False)])
    getAnimateFirstView = JavaMethod("()Z")
    setAnimateFirstView = JavaMethod("(Z)V")
    getBaseline = JavaMethod("()I")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")