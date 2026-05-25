from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataRemovalRequest"]

class DataRemovalRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/DataRemovalRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_IS_PREFIX = JavaStaticField("I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    isForEverything = JavaMethod("()Z")
    getLocusIdRequests = JavaMethod("()Ljava/util/List;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/contentcapture/DataRemovalRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        forEverything = JavaMethod("()Landroid/view/contentcapture/DataRemovalRequest$Builder;")
        addLocusId = JavaMethod("(Landroid/content/LocusId;I)Landroid/view/contentcapture/DataRemovalRequest$Builder;")
        build = JavaMethod("()Landroid/view/contentcapture/DataRemovalRequest;")

    class LocusIdRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/contentcapture/DataRemovalRequest/LocusIdRequest"
        getLocusId = JavaMethod("()Landroid/content/LocusId;")
        getFlags = JavaMethod("()I")