from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrepareGetCredentialResponse"]

class PrepareGetCredentialResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/PrepareGetCredentialResponse"
    hasRemoteResults = JavaMethod("()Z")
    getPendingGetCredentialHandle = JavaMethod("()Landroid/credentials/PrepareGetCredentialResponse$PendingGetCredentialHandle;")
    hasAuthenticationResults = JavaMethod("()Z")
    hasCredentialResults = JavaMethod("(Ljava/lang/String;)Z")

    class PendingGetCredentialHandle(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/credentials/PrepareGetCredentialResponse$PendingGetCredentialHandle"