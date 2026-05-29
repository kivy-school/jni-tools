from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioMixerAttributes"]

class AudioMixerAttributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioMixerAttributes"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    MIXER_BEHAVIOR_BIT_PERFECT = JavaStaticField("I")
    MIXER_BEHAVIOR_DEFAULT = JavaStaticField("I")
    getFormat = JavaMethod("()Landroid/media/AudioFormat;")
    getMixerBehavior = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/AudioMixerAttributes/Builder"
        __javaconstructor__ = [("(Landroid/media/AudioFormat;)V", False)]
        build = JavaMethod("()Landroid/media/AudioMixerAttributes;")
        setMixerBehavior = JavaMethod("(I)Landroid/media/AudioMixerAttributes$Builder;")