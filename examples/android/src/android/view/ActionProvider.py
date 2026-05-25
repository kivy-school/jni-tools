from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ActionProvider"]

class ActionProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ActionProvider"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    onCreateActionView = JavaMultipleMethod([("()Landroid/view/View;", False, False), ("(Landroid/view/MenuItem;)Landroid/view/View;", False, False)])
    overridesItemVisibility = JavaMethod("()Z")
    isVisible = JavaMethod("()Z")
    refreshVisibility = JavaMethod("()V")
    onPerformDefaultAction = JavaMethod("()Z")
    hasSubMenu = JavaMethod("()Z")
    onPrepareSubMenu = JavaMethod("(Landroid/view/SubMenu;)V")
    setVisibilityListener = JavaMethod("(Landroid/view/ActionProvider$VisibilityListener;)V")

    class VisibilityListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ActionProvider/VisibilityListener"
        onActionProviderVisibilityChanged = JavaMethod("(Z)V")