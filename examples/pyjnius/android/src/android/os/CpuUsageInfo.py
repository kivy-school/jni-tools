from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CpuUsageInfo"]

class CpuUsageInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/CpuUsageInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getActive = JavaMethod("()J")
    getTotal = JavaMethod("()J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")