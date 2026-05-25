from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContextMenu"]

class ContextMenu(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ContextMenu"
    setHeaderTitle = JavaMultipleMethod([("(I)Landroid/view/ContextMenu;", False, False), ("(Ljava/lang/CharSequence;)Landroid/view/ContextMenu;", False, False)])
    setHeaderIcon = JavaMultipleMethod([("(I)Landroid/view/ContextMenu;", False, False), ("(Landroid/graphics/drawable/Drawable;)Landroid/view/ContextMenu;", False, False)])
    setHeaderView = JavaMethod("(Landroid/view/View;)Landroid/view/ContextMenu;")
    clearHeader = JavaMethod("()V")

    class ContextMenuInfo(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ContextMenu/ContextMenuInfo"