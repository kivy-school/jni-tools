from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChangeLogTokenRequest"]

class ChangeLogTokenRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/changelog/ChangeLogTokenRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDataOriginFilters = JavaMethod("()Ljava/util/Set;")
    getRecordTypes = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/changelog/ChangeLogTokenRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        addRecordType = JavaMethod("(Ljava/lang/Class;)Landroid/health/connect/changelog/ChangeLogTokenRequest$Builder;")
        addDataOriginFilter = JavaMethod("(Landroid/health/connect/datatypes/DataOrigin;)Landroid/health/connect/changelog/ChangeLogTokenRequest$Builder;")
        build = JavaMethod("()Landroid/health/connect/changelog/ChangeLogTokenRequest;")