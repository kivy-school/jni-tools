from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExternalStorageStats"]

class ExternalStorageStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/ExternalStorageStats"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTotalBytes = JavaMethod("()J")
    getAppBytes = JavaMethod("()J")
    getAudioBytes = JavaMethod("()J")
    getImageBytes = JavaMethod("()J")
    getVideoBytes = JavaMethod("()J")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")