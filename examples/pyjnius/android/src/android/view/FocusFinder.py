from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FocusFinder"]

class FocusFinder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/FocusFinder"
    getInstance = JavaStaticMethod("()Landroid/view/FocusFinder;")
    findNextFocus = JavaMethod("(Landroid/view/ViewGroup;Landroid/view/View;I)Landroid/view/View;")
    findNextFocusFromRect = JavaMethod("(Landroid/view/ViewGroup;Landroid/graphics/Rect;I)Landroid/view/View;")
    findNextKeyboardNavigationCluster = JavaMethod("(Landroid/view/View;Landroid/view/View;I)Landroid/view/View;")
    findNearestTouchable = JavaMethod("(Landroid/view/ViewGroup;III[I)Landroid/view/View;")