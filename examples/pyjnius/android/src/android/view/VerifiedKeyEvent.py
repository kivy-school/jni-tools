from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VerifiedKeyEvent"]

class VerifiedKeyEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/VerifiedKeyEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getFlag = JavaMethod("(I)Ljava/lang/Boolean;")
    getAction = JavaMethod("()I")
    getDownTimeNanos = JavaMethod("()J")
    getKeyCode = JavaMethod("()I")
    getScanCode = JavaMethod("()I")
    getMetaState = JavaMethod("()I")
    getRepeatCount = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")