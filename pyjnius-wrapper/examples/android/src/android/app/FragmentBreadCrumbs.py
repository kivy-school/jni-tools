from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FragmentBreadCrumbs"]

class FragmentBreadCrumbs(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/FragmentBreadCrumbs"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False)]
    setActivity = JavaMethod("(Landroid/app/Activity;)V")
    setMaxVisible = JavaMethod("(I)V")
    setParentTitle = JavaMethod("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;Landroid/view/View$OnClickListener;)V")
    setOnBreadCrumbClickListener = JavaMethod("(Landroid/app/FragmentBreadCrumbs$OnBreadCrumbClickListener;)V")
    setTitle = JavaMethod("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)V")
    onLayout = JavaMethod("(ZIIII)V")
    onMeasure = JavaMethod("(II)V")
    onBackStackChanged = JavaMethod("()V")

    class OnBreadCrumbClickListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/FragmentBreadCrumbs/OnBreadCrumbClickListener"
        onBreadCrumbClick = JavaMethod("(Landroid/app/FragmentManager$BackStackEntry;I)Z")