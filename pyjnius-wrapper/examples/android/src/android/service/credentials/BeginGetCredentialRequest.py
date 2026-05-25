from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BeginGetCredentialRequest"]

class BeginGetCredentialRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/BeginGetCredentialRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getCallingAppInfo = JavaMethod("()Landroid/service/credentials/CallingAppInfo;")
    getBeginGetCredentialOptions = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/credentials/BeginGetCredentialRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        setCallingAppInfo = JavaMethod("(Landroid/service/credentials/CallingAppInfo;)Landroid/service/credentials/BeginGetCredentialRequest$Builder;")
        setBeginGetCredentialOptions = JavaMethod("(Ljava/util/List;)Landroid/service/credentials/BeginGetCredentialRequest$Builder;")
        addBeginGetCredentialOption = JavaMethod("(Landroid/service/credentials/BeginGetCredentialOption;)Landroid/service/credentials/BeginGetCredentialRequest$Builder;")
        build = JavaMethod("()Landroid/service/credentials/BeginGetCredentialRequest;")