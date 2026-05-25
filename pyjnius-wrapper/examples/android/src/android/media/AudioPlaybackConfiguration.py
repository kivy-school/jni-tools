from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioPlaybackConfiguration"]

class AudioPlaybackConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioPlaybackConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getAudioAttributes = JavaMethod("()Landroid/media/AudioAttributes;")
    getAudioDeviceInfo = JavaMethod("()Landroid/media/AudioDeviceInfo;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")