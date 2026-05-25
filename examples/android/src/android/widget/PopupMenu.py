from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PopupMenu"]

class PopupMenu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/PopupMenu"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/view/View;)V", False), ("(Landroid/content/Context;Landroid/view/View;I)V", False), ("(Landroid/content/Context;Landroid/view/View;III)V", False)]
    setGravity = JavaMethod("(I)V")
    getGravity = JavaMethod("()I")
    getDragToOpenListener = JavaMethod("()Landroid/view/View$OnTouchListener;")
    getMenu = JavaMethod("()Landroid/view/Menu;")
    getMenuInflater = JavaMethod("()Landroid/view/MenuInflater;")
    inflate = JavaMethod("(I)V")
    show = JavaMethod("()V")
    dismiss = JavaMethod("()V")
    setOnMenuItemClickListener = JavaMethod("(Landroid/widget/PopupMenu$OnMenuItemClickListener;)V")
    setOnDismissListener = JavaMethod("(Landroid/widget/PopupMenu$OnDismissListener;)V")
    setForceShowIcon = JavaMethod("(Z)V")

    class OnDismissListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/PopupMenu/OnDismissListener"
        onDismiss = JavaMethod("(Landroid/widget/PopupMenu;)V")

    class OnMenuItemClickListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/PopupMenu/OnMenuItemClickListener"
        onMenuItemClick = JavaMethod("(Landroid/view/MenuItem;)Z")