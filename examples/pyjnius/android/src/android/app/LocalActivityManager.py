from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocalActivityManager"]

class LocalActivityManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/LocalActivityManager"
    __javaconstructor__ = [("(Landroid/app/Activity;Z)V", False)]
    startActivity = JavaMethod("(Ljava/lang/String;Landroid/content/Intent;)Landroid/view/Window;")
    destroyActivity = JavaMethod("(Ljava/lang/String;Z)Landroid/view/Window;")
    getCurrentActivity = JavaMethod("()Landroid/app/Activity;")
    getCurrentId = JavaMethod("()Ljava/lang/String;")
    getActivity = JavaMethod("(Ljava/lang/String;)Landroid/app/Activity;")
    dispatchCreate = JavaMethod("(Landroid/os/Bundle;)V")
    saveInstanceState = JavaMethod("()Landroid/os/Bundle;")
    dispatchResume = JavaMethod("()V")
    dispatchPause = JavaMethod("(Z)V")
    dispatchStop = JavaMethod("()V")
    removeAllActivities = JavaMethod("()V")
    dispatchDestroy = JavaMethod("(Z)V")