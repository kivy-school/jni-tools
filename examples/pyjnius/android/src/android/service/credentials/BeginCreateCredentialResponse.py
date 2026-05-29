from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BeginCreateCredentialResponse"]

class BeginCreateCredentialResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/BeginCreateCredentialResponse"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCreateEntries = JavaMethod("()Ljava/util/List;")
    getRemoteCreateEntry = JavaMethod("()Landroid/service/credentials/RemoteEntry;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/credentials/BeginCreateCredentialResponse$Builder"
        __javaconstructor__ = [("()V", False)]
        setRemoteCreateEntry = JavaMethod("(Landroid/service/credentials/RemoteEntry;)Landroid/service/credentials/BeginCreateCredentialResponse$Builder;")
        addCreateEntry = JavaMethod("(Landroid/service/credentials/CreateEntry;)Landroid/service/credentials/BeginCreateCredentialResponse$Builder;")
        setCreateEntries = JavaMethod("(Ljava/util/List;)Landroid/service/credentials/BeginCreateCredentialResponse$Builder;")
        build = JavaMethod("()Landroid/service/credentials/BeginCreateCredentialResponse;")