from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BeginGetCredentialRequest"]

class BeginGetCredentialRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/BeginGetCredentialRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCallingAppInfo = JavaMethod("()Landroid/service/credentials/CallingAppInfo;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getBeginGetCredentialOptions = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/credentials/BeginGetCredentialRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setBeginGetCredentialOptions = JavaMethod("(Ljava/util/List;)Landroid/service/credentials/BeginGetCredentialRequest$Builder;")
        addBeginGetCredentialOption = JavaMethod("(Landroid/service/credentials/BeginGetCredentialOption;)Landroid/service/credentials/BeginGetCredentialRequest$Builder;")
        setCallingAppInfo = JavaMethod("(Landroid/service/credentials/CallingAppInfo;)Landroid/service/credentials/BeginGetCredentialRequest$Builder;")
        build = JavaMethod("()Landroid/service/credentials/BeginGetCredentialRequest;")