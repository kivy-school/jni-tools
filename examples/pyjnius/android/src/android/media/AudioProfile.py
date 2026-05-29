from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioProfile"]

class AudioProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioProfile"
    AUDIO_ENCAPSULATION_TYPE_IEC61937 = JavaStaticField("I")
    AUDIO_ENCAPSULATION_TYPE_NONE = JavaStaticField("I")
    AUDIO_ENCAPSULATION_TYPE_PCM = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getChannelIndexMasks = JavaMethod("()[I")
    getChannelMasks = JavaMethod("()[I")
    getSampleRates = JavaMethod("()[I")
    getEncapsulationType = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getFormat = JavaMethod("()I")