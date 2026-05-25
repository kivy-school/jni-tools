from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdActivity"]

class AdActivity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/AdActivity"
    __javaconstructor__ = [("()V", False)]
    CLASS_NAME = JavaStaticField("Ljava/lang/String;")
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    onRestart = JavaMethod("()V")
    onStart = JavaMethod("()V")
    onUserLeaveHint = JavaMethod("()V")
    onResume = JavaMethod("()V")
    onPause = JavaMethod("()V")
    onSaveInstanceState = JavaMethod("(Landroid/os/Bundle;)V")
    onStop = JavaMethod("()V")
    onDestroy = JavaMethod("()V")
    setContentView = JavaMultipleMethod([("(I)V", False, False), ("(Landroid/view/View;)V", False, False), ("(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V", False, False)])
    onBackPressed = JavaMethod("()V")
    onActivityResult = JavaMethod("(IILandroid/content/Intent;)V")
    onConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    onRequestPermissionsResult = JavaMethod("(I[Ljava/lang/String;[I)V")