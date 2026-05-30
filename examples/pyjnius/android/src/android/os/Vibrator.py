from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class VibratorFrequencyProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/vibrator/VibratorFrequencyProfile"
    getMaxFrequencyHz = JavaMethod("()F")
    getMaxOutputAccelerationGs = JavaMethod("()F")
    getMinFrequencyHz = JavaMethod("()F")
    getOutputAccelerationGs = JavaMethod("(F)F")
    getFrequenciesOutputAcceleration = JavaMethod("()Landroid/util/SparseArray;")
    getFrequencyRange = JavaMethod("(F)Landroid/util/Range;")