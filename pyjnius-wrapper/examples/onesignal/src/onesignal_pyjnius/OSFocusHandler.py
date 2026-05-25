from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSFocusHandler"]

class OSFocusHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSFocusHandler"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/OSFocusHandler$Companion;")
    hasBackgrounded = JavaMethod("()Z")
    hasCompleted = JavaMethod("()Z")
    startOnFocusWork = JavaMethod("()V")
    startOnStartFocusWork = JavaMethod("()V")
    startOnStopFocusWork = JavaMethod("()V")
    startOnLostFocusWorker = JavaMethod("(Ljava/lang/String;JLandroid/content/Context;)V")
    cancelOnLostFocusWorker = JavaMethod("(Ljava/lang/String;Landroid/content/Context;)V")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OSFocusHandler/Companion"
        onLostFocusDoWork = JavaMethod("()V")

    class OnLostFocusWorker(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/OSFocusHandler/OnLostFocusWorker"
        __javaconstructor__ = [("(Landroid/content/Context;Landroidx/work/WorkerParameters;)V", False)]
        doWork = JavaMethod("()Landroidx/work/ListenableWorker$Result;")