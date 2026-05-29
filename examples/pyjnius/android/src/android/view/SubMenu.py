from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SubMenu"]

class SubMenu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/SubMenu"
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
    setIcon = JavaMultipleMethod([("(I)Landroid/view/SubMenu;", False, False), ("(Landroid/graphics/drawable/Drawable;)Landroid/view/SubMenu;", False, False)])
    clearHeader = JavaMethod("()V")
    setHeaderView = JavaMethod("(Landroid/view/View;)Landroid/view/SubMenu;")
    setHeaderTitle = JavaMultipleMethod([("(I)Landroid/view/SubMenu;", False, False), ("(Ljava/lang/CharSequence;)Landroid/view/SubMenu;", False, False)])
    setHeaderIcon = JavaMultipleMethod([("(Landroid/graphics/drawable/Drawable;)Landroid/view/SubMenu;", False, False), ("(I)Landroid/view/SubMenu;", False, False)])
    getItem = JavaMethod("()Landroid/view/MenuItem;")