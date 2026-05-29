from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BeginGetCredentialResponse"]

class BeginGetCredentialResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/BeginGetCredentialResponse"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getCredentialEntries = JavaMethod("()Ljava/util/List;")
    getAuthenticationActions = JavaMethod("()Ljava/util/List;")
    getActions = JavaMethod("()Ljava/util/List;")
    getRemoteCredentialEntry = JavaMethod("()Landroid/service/credentials/RemoteEntry;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/credentials/BeginGetCredentialResponse/Builder"
        __javaconstructor__ = [("()V", False)]
        setRemoteCredentialEntry = JavaMethod("(Landroid/service/credentials/RemoteEntry;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        addCredentialEntry = JavaMethod("(Landroid/service/credentials/CredentialEntry;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        addAuthenticationAction = JavaMethod("(Landroid/service/credentials/Action;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        addAction = JavaMethod("(Landroid/service/credentials/Action;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        setActions = JavaMethod("(Ljava/util/List;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        setCredentialEntries = JavaMethod("(Ljava/util/List;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        setAuthenticationActions = JavaMethod("(Ljava/util/List;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        build = JavaMethod("()Landroid/service/credentials/BeginGetCredentialResponse;")