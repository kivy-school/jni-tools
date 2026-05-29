from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VirtualDevice"]

class VirtualDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/virtual/VirtualDevice"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getDisplayIds = JavaMethod("()[I")
    getPersistentDeviceId = JavaMethod("()Ljava/lang/String;")
    hasCustomSensorSupport = JavaMethod("()Z")
    getDeviceId = JavaMethod("()I")
    getDisplayName = JavaMethod("()Ljava/lang/CharSequence;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")