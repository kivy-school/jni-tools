from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdapterViewAnimator"]

class AdapterViewAnimator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/AdapterViewAnimator"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    setDisplayedChild = JavaMethod("(I)V")
    getDisplayedChild = JavaMethod("()I")
    showNext = JavaMethod("()V")
    showPrevious = JavaMethod("()V")
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onMeasure = JavaMethod("(II)V")
    onLayout = JavaMethod("(ZIIII)V")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Parcelable;)V")
    getCurrentView = JavaMethod("()Landroid/view/View;")
    getInAnimation = JavaMethod("()Landroid/animation/ObjectAnimator;")
    setInAnimation = JavaMultipleMethod([("(Landroid/animation/ObjectAnimator;)V", False, False), ("(Landroid/content/Context;I)V", False, False)])
    getOutAnimation = JavaMethod("()Landroid/animation/ObjectAnimator;")
    setOutAnimation = JavaMultipleMethod([("(Landroid/animation/ObjectAnimator;)V", False, False), ("(Landroid/content/Context;I)V", False, False)])
    setAnimateFirstView = JavaMethod("(Z)V")
    getBaseline = JavaMethod("()I")
    getAdapter = JavaMethod("()Landroid/widget/Adapter;")
    setAdapter = JavaMethod("(Landroid/widget/Adapter;)V")
    setRemoteViewsAdapter = JavaMethod("(Landroid/content/Intent;)V")
    setSelection = JavaMethod("(I)V")
    getSelectedView = JavaMethod("()Landroid/view/View;")
    deferNotifyDataSetChanged = JavaMethod("()V")
    onRemoteAdapterConnected = JavaMethod("()Z")
    onRemoteAdapterDisconnected = JavaMethod("()V")
    advance = JavaMethod("()V")
    fyiWillBeAdvancedByHostKThx = JavaMethod("()V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")