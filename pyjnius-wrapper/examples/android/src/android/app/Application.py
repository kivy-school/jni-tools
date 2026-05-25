from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Application"]

class Application(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/Application"
    __javaconstructor__ = [("()V", False)]
    onCreate = JavaMethod("()V")
    onTerminate = JavaMethod("()V")
    onConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    onLowMemory = JavaMethod("()V")
    onTrimMemory = JavaMethod("(I)V")
    registerComponentCallbacks = JavaMethod("(Landroid/content/ComponentCallbacks;)V")
    unregisterComponentCallbacks = JavaMethod("(Landroid/content/ComponentCallbacks;)V")
    registerActivityLifecycleCallbacks = JavaMethod("(Landroid/app/Application$ActivityLifecycleCallbacks;)V")
    unregisterActivityLifecycleCallbacks = JavaMethod("(Landroid/app/Application$ActivityLifecycleCallbacks;)V")
    registerOnProvideAssistDataListener = JavaMethod("(Landroid/app/Application$OnProvideAssistDataListener;)V")
    unregisterOnProvideAssistDataListener = JavaMethod("(Landroid/app/Application$OnProvideAssistDataListener;)V")
    getProcessName = JavaStaticMethod("()Ljava/lang/String;")

    class ActivityLifecycleCallbacks(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/Application/ActivityLifecycleCallbacks"
        onActivityPreCreated = JavaMethod("(Landroid/app/Activity;Landroid/os/Bundle;)V")
        onActivityCreated = JavaMethod("(Landroid/app/Activity;Landroid/os/Bundle;)V")
        onActivityPostCreated = JavaMethod("(Landroid/app/Activity;Landroid/os/Bundle;)V")
        onActivityPreStarted = JavaMethod("(Landroid/app/Activity;)V")
        onActivityStarted = JavaMethod("(Landroid/app/Activity;)V")
        onActivityPostStarted = JavaMethod("(Landroid/app/Activity;)V")
        onActivityPreResumed = JavaMethod("(Landroid/app/Activity;)V")
        onActivityResumed = JavaMethod("(Landroid/app/Activity;)V")
        onActivityPostResumed = JavaMethod("(Landroid/app/Activity;)V")
        onActivityPrePaused = JavaMethod("(Landroid/app/Activity;)V")
        onActivityPaused = JavaMethod("(Landroid/app/Activity;)V")
        onActivityPostPaused = JavaMethod("(Landroid/app/Activity;)V")
        onActivityPreStopped = JavaMethod("(Landroid/app/Activity;)V")
        onActivityStopped = JavaMethod("(Landroid/app/Activity;)V")
        onActivityPostStopped = JavaMethod("(Landroid/app/Activity;)V")
        onActivityPreSaveInstanceState = JavaMethod("(Landroid/app/Activity;Landroid/os/Bundle;)V")
        onActivitySaveInstanceState = JavaMethod("(Landroid/app/Activity;Landroid/os/Bundle;)V")
        onActivityPostSaveInstanceState = JavaMethod("(Landroid/app/Activity;Landroid/os/Bundle;)V")
        onActivityPreDestroyed = JavaMethod("(Landroid/app/Activity;)V")
        onActivityDestroyed = JavaMethod("(Landroid/app/Activity;)V")
        onActivityPostDestroyed = JavaMethod("(Landroid/app/Activity;)V")

    class OnProvideAssistDataListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/Application/OnProvideAssistDataListener"
        onProvideAssistData = JavaMethod("(Landroid/app/Activity;Landroid/os/Bundle;)V")