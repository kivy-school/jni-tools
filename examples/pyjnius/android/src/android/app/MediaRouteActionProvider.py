from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaRouteActionProvider"]

class MediaRouteActionProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/MediaRouteActionProvider"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    setRouteTypes = JavaMethod("(I)V")
    setExtendedSettingsClickListener = JavaMethod("(Landroid/view/View$OnClickListener;)V")
    onCreateActionView = JavaMultipleMethod([("()Landroid/view/View;", False, False), ("(Landroid/view/MenuItem;)Landroid/view/View;", False, False)])
    onPerformDefaultAction = JavaMethod("()Z")
    overridesItemVisibility = JavaMethod("()Z")
    isVisible = JavaMethod("()Z")