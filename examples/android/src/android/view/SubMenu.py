from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SubMenu"]

class SubMenu(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/SubMenu"
    setHeaderTitle = JavaMultipleMethod([("(I)Landroid/view/SubMenu;", False, False), ("(Ljava/lang/CharSequence;)Landroid/view/SubMenu;", False, False)])
    setHeaderIcon = JavaMultipleMethod([("(I)Landroid/view/SubMenu;", False, False), ("(Landroid/graphics/drawable/Drawable;)Landroid/view/SubMenu;", False, False)])
    setHeaderView = JavaMethod("(Landroid/view/View;)Landroid/view/SubMenu;")
    clearHeader = JavaMethod("()V")
    setIcon = JavaMultipleMethod([("(I)Landroid/view/SubMenu;", False, False), ("(Landroid/graphics/drawable/Drawable;)Landroid/view/SubMenu;", False, False)])
    getItem = JavaMethod("()Landroid/view/MenuItem;")