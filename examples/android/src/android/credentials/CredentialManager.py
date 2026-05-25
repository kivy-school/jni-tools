from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CredentialManager"]

class CredentialManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/CredentialManager"
    getCredential = JavaMultipleMethod([("(Landroid/content/Context;Landroid/credentials/GetCredentialRequest;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/content/Context;Landroid/credentials/PrepareGetCredentialResponse$PendingGetCredentialHandle;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False)])
    prepareGetCredential = JavaMethod("(Landroid/credentials/GetCredentialRequest;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    createCredential = JavaMethod("(Landroid/content/Context;Landroid/credentials/CreateCredentialRequest;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    clearCredentialState = JavaMethod("(Landroid/credentials/ClearCredentialStateRequest;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    isEnabledCredentialProviderService = JavaMethod("(Landroid/content/ComponentName;)Z")
    registerCredentialDescription = JavaMethod("(Landroid/credentials/RegisterCredentialDescriptionRequest;)V")
    unregisterCredentialDescription = JavaMethod("(Landroid/credentials/UnregisterCredentialDescriptionRequest;)V")