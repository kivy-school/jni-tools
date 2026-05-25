from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Gallery"]

class Gallery(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Gallery"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    onAttachedToWindow = JavaMethod("()V")
    setCallbackDuringFling = JavaMethod("(Z)V")
    setAnimationDuration = JavaMethod("(I)V")
    setSpacing = JavaMethod("(I)V")
    setUnselectedAlpha = JavaMethod("(F)V")
    getChildStaticTransformation = JavaMethod("(Landroid/view/View;Landroid/view/animation/Transformation;)Z")
    computeHorizontalScrollExtent = JavaMethod("()I")
    computeHorizontalScrollOffset = JavaMethod("()I")
    computeHorizontalScrollRange = JavaMethod("()I")
    checkLayoutParams = JavaMethod("(Landroid/view/ViewGroup$LayoutParams;)Z")
    generateLayoutParams = JavaMultipleMethod([("(Landroid/view/ViewGroup$LayoutParams;)Landroid/view/ViewGroup$LayoutParams;", False, False), ("(Landroid/util/AttributeSet;)Landroid/view/ViewGroup$LayoutParams;", False, False)])
    generateDefaultLayoutParams = JavaMethod("()Landroid/view/ViewGroup$LayoutParams;")
    onLayout = JavaMethod("(ZIIII)V")
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onSingleTapUp = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onFling = JavaMethod("(Landroid/view/MotionEvent;Landroid/view/MotionEvent;FF)Z")
    onScroll = JavaMethod("(Landroid/view/MotionEvent;Landroid/view/MotionEvent;FF)Z")
    onDown = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onLongPress = JavaMethod("(Landroid/view/MotionEvent;)V")
    onShowPress = JavaMethod("(Landroid/view/MotionEvent;)V")
    dispatchSetSelected = JavaMethod("(Z)V")
    dispatchSetPressed = JavaMethod("(Z)V")
    getContextMenuInfo = JavaMethod("()Landroid/view/ContextMenu$ContextMenuInfo;")
    showContextMenuForChild = JavaMultipleMethod([("(Landroid/view/View;)Z", False, False), ("(Landroid/view/View;FF)Z", False, False)])
    showContextMenu = JavaMultipleMethod([("()Z", False, False), ("(FF)Z", False, False)])
    dispatchKeyEvent = JavaMethod("(Landroid/view/KeyEvent;)Z")
    onKeyDown = JavaMethod("(ILandroid/view/KeyEvent;)Z")
    onKeyUp = JavaMethod("(ILandroid/view/KeyEvent;)Z")
    setGravity = JavaMethod("(I)V")
    getChildDrawingOrder = JavaMethod("(II)I")
    onFocusChanged = JavaMethod("(ZILandroid/graphics/Rect;)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")

    class LayoutParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/Gallery/LayoutParams"
        __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(II)V", False), ("(Landroid/view/ViewGroup$LayoutParams;)V", False)]