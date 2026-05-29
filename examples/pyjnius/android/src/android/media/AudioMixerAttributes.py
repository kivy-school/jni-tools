from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioMixerAttributes"]

class AudioMixerAttributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioMixerAttributes"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    MIXER_BEHAVIOR_BIT_PERFECT = JavaStaticField("I")
    MIXER_BEHAVIOR_DEFAULT = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMixerBehavior = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getFormat = JavaMethod("()Landroid/media/AudioFormat;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/AudioMixerAttributes$Builder"
        __javaconstructor__ = [("(Landroid/media/AudioFormat;)V", False)]
        setMixerBehavior = JavaMethod("(I)Landroid/media/AudioMixerAttributes$Builder;")
        build = JavaMethod("()Landroid/media/AudioMixerAttributes;")