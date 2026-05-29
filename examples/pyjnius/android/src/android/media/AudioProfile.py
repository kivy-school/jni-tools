from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioProfile"]

class AudioProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioProfile"
    AUDIO_ENCAPSULATION_TYPE_IEC61937 = JavaStaticField("I")
    AUDIO_ENCAPSULATION_TYPE_NONE = JavaStaticField("I")
    AUDIO_ENCAPSULATION_TYPE_PCM = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getFormat = JavaMethod("()I")
    getChannelMasks = JavaMethod("()[I")
    getChannelIndexMasks = JavaMethod("()[I")
    getSampleRates = JavaMethod("()[I")
    getEncapsulationType = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")