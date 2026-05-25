from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TabActivity"]

class TabActivity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/TabActivity"
    __javaconstructor__ = [("()V", False)]
    setDefaultTab = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(I)V", False, False)])
    onRestoreInstanceState = JavaMethod("(Landroid/os/Bundle;)V")
    onPostCreate = JavaMethod("(Landroid/os/Bundle;)V")
    onSaveInstanceState = JavaMethod("(Landroid/os/Bundle;)V")
    onContentChanged = JavaMethod("()V")
    onChildTitleChanged = JavaMethod("(Landroid/app/Activity;Ljava/lang/CharSequence;)V")
    getTabHost = JavaMethod("()Landroid/widget/TabHost;")
    getTabWidget = JavaMethod("()Landroid/widget/TabWidget;")