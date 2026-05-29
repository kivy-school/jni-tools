from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChangeLogsRequest"]

class ChangeLogsRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/changelog/ChangeLogsRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getToken = JavaMethod("()Ljava/lang/String;")
    getPageSize = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/changelog/ChangeLogsRequest/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setPageSize = JavaMethod("(I)Landroid/health/connect/changelog/ChangeLogsRequest$Builder;")
        build = JavaMethod("()Landroid/health/connect/changelog/ChangeLogsRequest;")