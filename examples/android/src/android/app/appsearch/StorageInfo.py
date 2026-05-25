from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StorageInfo"]

class StorageInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/StorageInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSizeBytes = JavaMethod("()J")
    getAliveDocumentsCount = JavaMethod("()I")
    getAliveNamespacesCount = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/StorageInfo/Builder"
        __javaconstructor__ = [("()V", False)]
        setSizeBytes = JavaMethod("(J)Landroid/app/appsearch/StorageInfo$Builder;")
        setAliveDocumentsCount = JavaMethod("(I)Landroid/app/appsearch/StorageInfo$Builder;")
        setAliveNamespacesCount = JavaMethod("(I)Landroid/app/appsearch/StorageInfo$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/StorageInfo;")