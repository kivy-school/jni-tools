from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContextMenu"]

class ContextMenu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ContextMenu"
    CATEGORY_ALTERNATIVE = JavaStaticField("I")
    CATEGORY_CONTAINER = JavaStaticField("I")
    CATEGORY_SECONDARY = JavaStaticField("I")
    CATEGORY_SYSTEM = JavaStaticField("I")
    FIRST = JavaStaticField("I")
    FLAG_ALWAYS_PERFORM_CLOSE = JavaStaticField("I")
    FLAG_APPEND_TO_GROUP = JavaStaticField("I")
    FLAG_PERFORM_NO_CLOSE = JavaStaticField("I")
    NONE = JavaStaticField("I")
    SUPPORTED_MODIFIERS_MASK = JavaStaticField("I")
    clearHeader = JavaMethod("()V")
    setHeaderView = JavaMethod("(Landroid/view/View;)Landroid/view/ContextMenu;")
    setHeaderTitle = JavaMultipleMethod([("(I)Landroid/view/ContextMenu;", False, False), ("(Ljava/lang/CharSequence;)Landroid/view/ContextMenu;", False, False)])
    setHeaderIcon = JavaMultipleMethod([("(Landroid/graphics/drawable/Drawable;)Landroid/view/ContextMenu;", False, False), ("(I)Landroid/view/ContextMenu;", False, False)])

    class ContextMenuInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ContextMenu$ContextMenuInfo"