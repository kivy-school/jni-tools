from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TvAdServiceInfo"]

class TvAdServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/ad/TvAdServiceInfo"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/ComponentName;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSupportedTypes = JavaMethod("()Ljava/util/List;")
    getId = JavaMethod("()Ljava/lang/String;")
    getServiceInfo = JavaMethod("()Landroid/content/pm/ServiceInfo;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")