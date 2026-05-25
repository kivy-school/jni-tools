from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VirtualDevice"]

class VirtualDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/virtual/VirtualDevice"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getDeviceId = JavaMethod("()I")
    getPersistentDeviceId = JavaMethod("()Ljava/lang/String;")
    getName = JavaMethod("()Ljava/lang/String;")
    getDisplayName = JavaMethod("()Ljava/lang/CharSequence;")
    getDisplayIds = JavaMethod("()[I")
    hasCustomSensorSupport = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")