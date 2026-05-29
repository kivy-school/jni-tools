from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataRemovalRequest"]

class DataRemovalRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/DataRemovalRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_IS_PREFIX = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLocusIdRequests = JavaMethod("()Ljava/util/List;")
    isForEverything = JavaMethod("()Z")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class LocusIdRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/contentcapture/DataRemovalRequest$LocusIdRequest"
        getFlags = JavaMethod("()I")
        getLocusId = JavaMethod("()Landroid/content/LocusId;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/contentcapture/DataRemovalRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        addLocusId = JavaMethod("(Landroid/content/LocusId;I)Landroid/view/contentcapture/DataRemovalRequest$Builder;")
        forEverything = JavaMethod("()Landroid/view/contentcapture/DataRemovalRequest$Builder;")
        build = JavaMethod("()Landroid/view/contentcapture/DataRemovalRequest;")