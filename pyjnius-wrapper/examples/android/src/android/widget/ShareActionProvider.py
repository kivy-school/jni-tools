from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ShareActionProvider"]

class ShareActionProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ShareActionProvider"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    DEFAULT_SHARE_HISTORY_FILE_NAME = JavaStaticField("Ljava/lang/String;")
    setOnShareTargetSelectedListener = JavaMethod("(Landroid/widget/ShareActionProvider$OnShareTargetSelectedListener;)V")
    onCreateActionView = JavaMethod("()Landroid/view/View;")
    hasSubMenu = JavaMethod("()Z")
    onPrepareSubMenu = JavaMethod("(Landroid/view/SubMenu;)V")
    setShareHistoryFileName = JavaMethod("(Ljava/lang/String;)V")
    setShareIntent = JavaMethod("(Landroid/content/Intent;)V")

    class OnShareTargetSelectedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/ShareActionProvider/OnShareTargetSelectedListener"
        onShareTargetSelected = JavaMethod("(Landroid/widget/ShareActionProvider;Landroid/content/Intent;)Z")