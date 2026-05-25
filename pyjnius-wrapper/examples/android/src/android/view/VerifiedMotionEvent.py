from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VerifiedMotionEvent"]

class VerifiedMotionEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/VerifiedMotionEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getFlag = JavaMethod("(I)Ljava/lang/Boolean;")
    getRawX = JavaMethod("()F")
    getRawY = JavaMethod("()F")
    getActionMasked = JavaMethod("()I")
    getDownTimeNanos = JavaMethod("()J")
    getMetaState = JavaMethod("()I")
    getButtonState = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")