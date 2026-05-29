from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractThreadedSyncAdapter"]

class AbstractThreadedSyncAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/AbstractThreadedSyncAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;Z)V", False), ("(Landroid/content/Context;ZZ)V", False)]
    LOG_SYNC_DETAILS = JavaStaticField("I")
    getContext = JavaMethod("()Landroid/content/Context;")
    getSyncAdapterBinder = JavaMethod("()Landroid/os/IBinder;")
    onPerformSync = JavaMethod("(Landroid/accounts/Account;Landroid/os/Bundle;Ljava/lang/String;Landroid/content/ContentProviderClient;Landroid/content/SyncResult;)V")
    onSyncCanceled = JavaMultipleMethod([("(Ljava/lang/Thread;)V", False, False), ("()V", False, False)])
    onSecurityException = JavaMethod("(Landroid/accounts/Account;Landroid/os/Bundle;Ljava/lang/String;Landroid/content/SyncResult;)V")
    onUnsyncableAccount = JavaMethod("()Z")