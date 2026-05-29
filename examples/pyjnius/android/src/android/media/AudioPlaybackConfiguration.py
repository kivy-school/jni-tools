from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioPlaybackConfiguration"]

class AudioPlaybackConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioPlaybackConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getAudioAttributes = JavaMethod("()Landroid/media/AudioAttributes;")
    getAudioDeviceInfo = JavaMethod("()Landroid/media/AudioDeviceInfo;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")