from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VibratorEnvelopeEffectInfo"]

class VibratorEnvelopeEffectInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/vibrator/VibratorEnvelopeEffectInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMaxControlPointDurationMillis = JavaMethod("()J")
    getMaxDurationMillis = JavaMethod("()J")
    getMinControlPointDurationMillis = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getMaxSize = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")