from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StorageInfo"]

class StorageInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/StorageInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSizeBytes = JavaMethod("()J")
    getAliveDocumentsCount = JavaMethod("()I")
    getBlobsCount = JavaMethod("()I")
    getBlobsSizeBytes = JavaMethod("()J")
    getAliveNamespacesCount = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/StorageInfo$Builder"
        __javaconstructor__ = [("()V", False)]
        setSizeBytes = JavaMethod("(J)Landroid/app/appsearch/StorageInfo$Builder;")
        setBlobsCount = JavaMethod("(I)Landroid/app/appsearch/StorageInfo$Builder;")
        setBlobsSizeBytes = JavaMethod("(J)Landroid/app/appsearch/StorageInfo$Builder;")
        setAliveDocumentsCount = JavaMethod("(I)Landroid/app/appsearch/StorageInfo$Builder;")
        setAliveNamespacesCount = JavaMethod("(I)Landroid/app/appsearch/StorageInfo$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/StorageInfo;")