from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PowerMonitor"]

class PowerMonitor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/PowerMonitor"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    POWER_MONITOR_TYPE_CONSUMER = JavaStaticField("I")
    POWER_MONITOR_TYPE_MEASUREMENT = JavaStaticField("I")
    getType = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")