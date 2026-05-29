from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BeginGetCredentialResponse"]

class BeginGetCredentialResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/BeginGetCredentialResponse"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCredentialEntries = JavaMethod("()Ljava/util/List;")
    getRemoteCredentialEntry = JavaMethod("()Landroid/service/credentials/RemoteEntry;")
    getAuthenticationActions = JavaMethod("()Ljava/util/List;")
    getActions = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/credentials/BeginGetCredentialResponse$Builder"
        __javaconstructor__ = [("()V", False)]
        setActions = JavaMethod("(Ljava/util/List;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        addCredentialEntry = JavaMethod("(Landroid/service/credentials/CredentialEntry;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        addAuthenticationAction = JavaMethod("(Landroid/service/credentials/Action;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        setAuthenticationActions = JavaMethod("(Ljava/util/List;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        setCredentialEntries = JavaMethod("(Ljava/util/List;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        setRemoteCredentialEntry = JavaMethod("(Landroid/service/credentials/RemoteEntry;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        addAction = JavaMethod("(Landroid/service/credentials/Action;)Landroid/service/credentials/BeginGetCredentialResponse$Builder;")
        build = JavaMethod("()Landroid/service/credentials/BeginGetCredentialResponse;")