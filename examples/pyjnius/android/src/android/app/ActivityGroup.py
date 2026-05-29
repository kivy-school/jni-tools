from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ActivityGroup"]

class ActivityGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/ActivityGroup"
    __javaconstructor__ = [("()V", False), ("(Z)V", False)]
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    onResume = JavaMethod("()V")
    onSaveInstanceState = JavaMethod("(Landroid/os/Bundle;)V")
    onPause = JavaMethod("()V")
    onStop = JavaMethod("()V")
    onDestroy = JavaMethod("()V")
    getCurrentActivity = JavaMethod("()Landroid/app/Activity;")
    getLocalActivityManager = JavaMethod("()Landroid/app/LocalActivityManager;")