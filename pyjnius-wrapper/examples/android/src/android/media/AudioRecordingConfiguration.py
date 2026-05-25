from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioRecordingConfiguration"]

class AudioRecordingConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioRecordingConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getClientAudioSource = JavaMethod("()I")
    getClientAudioSessionId = JavaMethod("()I")
    getFormat = JavaMethod("()Landroid/media/AudioFormat;")
    getClientFormat = JavaMethod("()Landroid/media/AudioFormat;")
    getAudioDevice = JavaMethod("()Landroid/media/AudioDeviceInfo;")
    isClientSilenced = JavaMethod("()Z")
    getAudioSource = JavaMethod("()I")
    getClientEffects = JavaMethod("()Ljava/util/List;")
    getEffects = JavaMethod("()Ljava/util/List;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")