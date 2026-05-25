from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrepareGetCredentialResponse"]

class PrepareGetCredentialResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/PrepareGetCredentialResponse"
    hasCredentialResults = JavaMethod("(Ljava/lang/String;)Z")
    hasAuthenticationResults = JavaMethod("()Z")
    hasRemoteResults = JavaMethod("()Z")
    getPendingGetCredentialHandle = JavaMethod("()Landroid/credentials/PrepareGetCredentialResponse$PendingGetCredentialHandle;")

    class PendingGetCredentialHandle(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/credentials/PrepareGetCredentialResponse/PendingGetCredentialHandle"