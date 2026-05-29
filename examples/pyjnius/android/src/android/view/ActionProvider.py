from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ActionProvider"]

class ActionProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ActionProvider"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    isVisible = JavaMethod("()Z")
    onPerformDefaultAction = JavaMethod("()Z")
    refreshVisibility = JavaMethod("()V")
    overridesItemVisibility = JavaMethod("()Z")
    setVisibilityListener = JavaMethod("(Landroid/view/ActionProvider$VisibilityListener;)V")
    onPrepareSubMenu = JavaMethod("(Landroid/view/SubMenu;)V")
    onCreateActionView = JavaMultipleMethod([("(Landroid/view/MenuItem;)Landroid/view/View;", False, False), ("()Landroid/view/View;", False, False)])
    hasSubMenu = JavaMethod("()Z")

    class VisibilityListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ActionProvider$VisibilityListener"
        onActionProviderVisibilityChanged = JavaMethod("(Z)V")