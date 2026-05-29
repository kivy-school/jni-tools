from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VerifiedKeyEvent"]

class VerifiedKeyEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/VerifiedKeyEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getDownTimeNanos = JavaMethod("()J")
    getFlag = JavaMethod("(I)Ljava/lang/Boolean;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getAction = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getKeyCode = JavaMethod("()I")
    getMetaState = JavaMethod("()I")
    getRepeatCount = JavaMethod("()I")
    getScanCode = JavaMethod("()I")