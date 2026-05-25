from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BeginCreateCredentialResponse"]

class BeginCreateCredentialResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/BeginCreateCredentialResponse"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getCreateEntries = JavaMethod("()Ljava/util/List;")
    getRemoteCreateEntry = JavaMethod("()Landroid/service/credentials/RemoteEntry;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/credentials/BeginCreateCredentialResponse/Builder"
        __javaconstructor__ = [("()V", False)]
        setCreateEntries = JavaMethod("(Ljava/util/List;)Landroid/service/credentials/BeginCreateCredentialResponse$Builder;")
        addCreateEntry = JavaMethod("(Landroid/service/credentials/CreateEntry;)Landroid/service/credentials/BeginCreateCredentialResponse$Builder;")
        setRemoteCreateEntry = JavaMethod("(Landroid/service/credentials/RemoteEntry;)Landroid/service/credentials/BeginCreateCredentialResponse$Builder;")
        build = JavaMethod("()Landroid/service/credentials/BeginCreateCredentialResponse;")