from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MetadataRequest"]

class MetadataRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/settings/preferences/MetadataRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/settings/preferences/MetadataRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/service/settings/preferences/MetadataRequest;")