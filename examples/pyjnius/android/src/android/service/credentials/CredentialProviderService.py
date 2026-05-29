from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CredentialProviderService"]

class CredentialProviderService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/CredentialProviderService"
    __javaconstructor__ = [("()V", False)]
    EXTRA_BEGIN_GET_CREDENTIAL_REQUEST = JavaStaticField("Ljava/lang/String;")
    EXTRA_BEGIN_GET_CREDENTIAL_RESPONSE = JavaStaticField("Ljava/lang/String;")
    EXTRA_CREATE_CREDENTIAL_EXCEPTION = JavaStaticField("Ljava/lang/String;")
    EXTRA_CREATE_CREDENTIAL_REQUEST = JavaStaticField("Ljava/lang/String;")
    EXTRA_CREATE_CREDENTIAL_RESPONSE = JavaStaticField("Ljava/lang/String;")
    EXTRA_GET_CREDENTIAL_EXCEPTION = JavaStaticField("Ljava/lang/String;")
    EXTRA_GET_CREDENTIAL_REQUEST = JavaStaticField("Ljava/lang/String;")
    EXTRA_GET_CREDENTIAL_RESPONSE = JavaStaticField("Ljava/lang/String;")
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    onCreate = JavaMethod("()V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onBeginGetCredential = JavaMethod("(Landroid/service/credentials/BeginGetCredentialRequest;Landroid/os/CancellationSignal;Landroid/os/OutcomeReceiver;)V")
    onBeginCreateCredential = JavaMethod("(Landroid/service/credentials/BeginCreateCredentialRequest;Landroid/os/CancellationSignal;Landroid/os/OutcomeReceiver;)V")
    onClearCredentialState = JavaMethod("(Landroid/service/credentials/ClearCredentialStateRequest;Landroid/os/CancellationSignal;Landroid/os/OutcomeReceiver;)V")