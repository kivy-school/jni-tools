from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewManager"]

class ViewManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ViewManager"
    updateViewLayout = JavaMethod("(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V")
    addView = JavaMethod("(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V")
    removeView = JavaMethod("(Landroid/view/View;)V")