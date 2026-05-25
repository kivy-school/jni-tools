from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewManager"]

class ViewManager(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ViewManager"
    addView = JavaMethod("(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V")
    updateViewLayout = JavaMethod("(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V")
    removeView = JavaMethod("(Landroid/view/View;)V")