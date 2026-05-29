from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocalActivityManager"]

class LocalActivityManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/LocalActivityManager"
    __javaconstructor__ = [("(Landroid/app/Activity;Z)V", False)]
    getActivity = JavaMethod("(Ljava/lang/String;)Landroid/app/Activity;")
    dispatchResume = JavaMethod("()V")
    dispatchStop = JavaMethod("()V")
    getCurrentId = JavaMethod("()Ljava/lang/String;")
    getCurrentActivity = JavaMethod("()Landroid/app/Activity;")
    dispatchPause = JavaMethod("(Z)V")
    dispatchDestroy = JavaMethod("(Z)V")
    saveInstanceState = JavaMethod("()Landroid/os/Bundle;")
    dispatchCreate = JavaMethod("(Landroid/os/Bundle;)V")
    removeAllActivities = JavaMethod("()V")
    destroyActivity = JavaMethod("(Ljava/lang/String;Z)Landroid/view/Window;")
    startActivity = JavaMethod("(Ljava/lang/String;Landroid/content/Intent;)Landroid/view/Window;")