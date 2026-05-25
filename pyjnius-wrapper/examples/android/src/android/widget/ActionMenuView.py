from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ActionMenuView"]

class ActionMenuView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ActionMenuView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    setPopupTheme = JavaMethod("(I)V")
    getPopupTheme = JavaMethod("()I")
    onConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    setOnMenuItemClickListener = JavaMethod("(Landroid/widget/ActionMenuView$OnMenuItemClickListener;)V")
    onMeasure = JavaMethod("(II)V")
    onLayout = JavaMethod("(ZIIII)V")
    onDetachedFromWindow = JavaMethod("()V")
    setOverflowIcon = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    getOverflowIcon = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    generateDefaultLayoutParams = JavaMethod("()Landroid/widget/ActionMenuView$LayoutParams;")
    generateLayoutParams = JavaMultipleMethod([("(Landroid/util/AttributeSet;)Landroid/widget/ActionMenuView$LayoutParams;", False, False), ("(Landroid/view/ViewGroup$LayoutParams;)Landroid/widget/ActionMenuView$LayoutParams;", False, False)])
    checkLayoutParams = JavaMethod("(Landroid/view/ViewGroup$LayoutParams;)Z")
    getMenu = JavaMethod("()Landroid/view/Menu;")
    showOverflowMenu = JavaMethod("()Z")
    hideOverflowMenu = JavaMethod("()Z")
    isOverflowMenuShowing = JavaMethod("()Z")
    dismissPopupMenus = JavaMethod("()V")

    class LayoutParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/ActionMenuView/LayoutParams"
        __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/view/ViewGroup$LayoutParams;)V", False), ("(Landroid/widget/ActionMenuView$LayoutParams;)V", False), ("(II)V", False)]

    class OnMenuItemClickListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/ActionMenuView/OnMenuItemClickListener"
        onMenuItemClick = JavaMethod("(Landroid/view/MenuItem;)Z")