from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BroadcastReceiver"]

class BroadcastReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/BroadcastReceiver"
    __javaconstructor__ = [("()V", False)]
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")
    goAsync = JavaMethod("()Landroid/content/BroadcastReceiver$PendingResult;")
    peekService = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)Landroid/os/IBinder;")
    setResultCode = JavaMethod("(I)V")
    getResultCode = JavaMethod("()I")
    setResultData = JavaMethod("(Ljava/lang/String;)V")
    getResultData = JavaMethod("()Ljava/lang/String;")
    setResultExtras = JavaMethod("(Landroid/os/Bundle;)V")
    getResultExtras = JavaMethod("(Z)Landroid/os/Bundle;")
    setResult = JavaMethod("(ILjava/lang/String;Landroid/os/Bundle;)V")
    getAbortBroadcast = JavaMethod("()Z")
    abortBroadcast = JavaMethod("()V")
    clearAbortBroadcast = JavaMethod("()V")
    isOrderedBroadcast = JavaMethod("()Z")
    isInitialStickyBroadcast = JavaMethod("()Z")
    setOrderedHint = JavaMethod("(Z)V")
    getSentFromUid = JavaMethod("()I")
    getSentFromPackage = JavaMethod("()Ljava/lang/String;")
    setDebugUnregister = JavaMethod("(Z)V")
    getDebugUnregister = JavaMethod("()Z")

    class PendingResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/BroadcastReceiver/PendingResult"
        setResultCode = JavaMethod("(I)V")
        getResultCode = JavaMethod("()I")
        setResultData = JavaMethod("(Ljava/lang/String;)V")
        getResultData = JavaMethod("()Ljava/lang/String;")
        setResultExtras = JavaMethod("(Landroid/os/Bundle;)V")
        getResultExtras = JavaMethod("(Z)Landroid/os/Bundle;")
        setResult = JavaMethod("(ILjava/lang/String;Landroid/os/Bundle;)V")
        getAbortBroadcast = JavaMethod("()Z")
        abortBroadcast = JavaMethod("()V")
        clearAbortBroadcast = JavaMethod("()V")
        finish = JavaMethod("()V")