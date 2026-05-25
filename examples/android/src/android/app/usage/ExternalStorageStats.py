from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExternalStorageStats"]

class ExternalStorageStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/ExternalStorageStats"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTotalBytes = JavaMethod("()J")
    getAudioBytes = JavaMethod("()J")
    getVideoBytes = JavaMethod("()J")
    getImageBytes = JavaMethod("()J")
    getAppBytes = JavaMethod("()J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")