from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VerifiedInputEvent"]

class VerifiedInputEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/VerifiedInputEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getDeviceId = JavaMethod("()I")
    getEventTimeNanos = JavaMethod("()J")
    getSource = JavaMethod("()I")
    getDisplayId = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")