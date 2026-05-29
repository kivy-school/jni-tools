from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PopupMenu"]

class PopupMenu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/PopupMenu"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/view/View;III)V", False), ("(Landroid/content/Context;Landroid/view/View;I)V", False), ("(Landroid/content/Context;Landroid/view/View;)V", False)]
    inflate = JavaMethod("(I)V")
    show = JavaMethod("()V")
    getMenu = JavaMethod("()Landroid/view/Menu;")
    setOnMenuItemClickListener = JavaMethod("(Landroid/widget/PopupMenu$OnMenuItemClickListener;)V")
    getGravity = JavaMethod("()I")
    setGravity = JavaMethod("(I)V")
    dismiss = JavaMethod("()V")
    setOnDismissListener = JavaMethod("(Landroid/widget/PopupMenu$OnDismissListener;)V")
    setForceShowIcon = JavaMethod("(Z)V")
    getMenuInflater = JavaMethod("()Landroid/view/MenuInflater;")
    getDragToOpenListener = JavaMethod("()Landroid/view/View$OnTouchListener;")

    class OnMenuItemClickListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/PopupMenu$OnMenuItemClickListener"
        onMenuItemClick = JavaMethod("(Landroid/view/MenuItem;)Z")

    class OnDismissListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/PopupMenu$OnDismissListener"
        onDismiss = JavaMethod("(Landroid/widget/PopupMenu;)V")