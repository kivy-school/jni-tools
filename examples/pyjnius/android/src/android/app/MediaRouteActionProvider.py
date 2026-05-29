from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaRouteActionProvider"]

class MediaRouteActionProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/MediaRouteActionProvider"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    setRouteTypes = JavaMethod("(I)V")
    setExtendedSettingsClickListener = JavaMethod("(Landroid/view/View$OnClickListener;)V")
    isVisible = JavaMethod("()Z")
    onPerformDefaultAction = JavaMethod("()Z")
    overridesItemVisibility = JavaMethod("()Z")
    onCreateActionView = JavaMultipleMethod([("()Landroid/view/View;", False, False), ("(Landroid/view/MenuItem;)Landroid/view/View;", False, False)])