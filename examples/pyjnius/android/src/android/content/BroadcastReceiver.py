from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BroadcastReceiver"]

class BroadcastReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/BroadcastReceiver"
    __javaconstructor__ = [("()V", False)]
    abortBroadcast = JavaMethod("()V")
    getDebugUnregister = JavaMethod("()Z")
    clearAbortBroadcast = JavaMethod("()V")
    getAbortBroadcast = JavaMethod("()Z")
    getResultCode = JavaMethod("()I")
    getResultData = JavaMethod("()Ljava/lang/String;")
    getResultExtras = JavaMethod("(Z)Landroid/os/Bundle;")
    getSentFromPackage = JavaMethod("()Ljava/lang/String;")
    getSentFromUid = JavaMethod("()I")
    goAsync = JavaMethod("()Landroid/content/BroadcastReceiver$PendingResult;")
    isInitialStickyBroadcast = JavaMethod("()Z")
    isOrderedBroadcast = JavaMethod("()Z")
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")
    peekService = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)Landroid/os/IBinder;")
    setDebugUnregister = JavaMethod("(Z)V")
    setOrderedHint = JavaMethod("(Z)V")
    setResultCode = JavaMethod("(I)V")
    setResultData = JavaMethod("(Ljava/lang/String;)V")
    setResultExtras = JavaMethod("(Landroid/os/Bundle;)V")
    setResult = JavaMethod("(ILjava/lang/String;Landroid/os/Bundle;)V")

    class PendingResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/BroadcastReceiver$PendingResult"
        abortBroadcast = JavaMethod("()V")
        clearAbortBroadcast = JavaMethod("()V")
        getAbortBroadcast = JavaMethod("()Z")
        getResultCode = JavaMethod("()I")
        getResultData = JavaMethod("()Ljava/lang/String;")
        getResultExtras = JavaMethod("(Z)Landroid/os/Bundle;")
        setResultCode = JavaMethod("(I)V")
        setResultData = JavaMethod("(Ljava/lang/String;)V")
        setResultExtras = JavaMethod("(Landroid/os/Bundle;)V")
        finish = JavaMethod("()V")
        setResult = JavaMethod("(ILjava/lang/String;Landroid/os/Bundle;)V")