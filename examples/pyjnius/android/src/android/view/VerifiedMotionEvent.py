from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VerifiedMotionEvent"]

class VerifiedMotionEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/VerifiedMotionEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getDownTimeNanos = JavaMethod("()J")
    getFlag = JavaMethod("(I)Ljava/lang/Boolean;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getActionMasked = JavaMethod("()I")
    getButtonState = JavaMethod("()I")
    getRawX = JavaMethod("()F")
    getRawY = JavaMethod("()F")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getMetaState = JavaMethod("()I")