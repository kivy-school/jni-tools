from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MetadataResult"]

class MetadataResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/settings/preferences/MetadataResult"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESULT_INTERNAL_ERROR = JavaStaticField("I")
    RESULT_OK = JavaStaticField("I")
    RESULT_UNSUPPORTED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getResultCode = JavaMethod("()I")
    getMetadataList = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/settings/preferences/MetadataResult$Builder"
        __javaconstructor__ = [("(I)V", False)]
        setMetadataList = JavaMethod("(Ljava/util/List;)Landroid/service/settings/preferences/MetadataResult$Builder;")
        build = JavaMethod("()Landroid/service/settings/preferences/MetadataResult;")