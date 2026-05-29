from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioRecordingConfiguration"]

class AudioRecordingConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioRecordingConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getClientEffects = JavaMethod("()Ljava/util/List;")
    getClientFormat = JavaMethod("()Landroid/media/AudioFormat;")
    getAudioSource = JavaMethod("()I")
    getAudioDevice = JavaMethod("()Landroid/media/AudioDeviceInfo;")
    getClientAudioSessionId = JavaMethod("()I")
    getClientAudioSource = JavaMethod("()I")
    getEffects = JavaMethod("()Ljava/util/List;")
    isClientSilenced = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getFormat = JavaMethod("()Landroid/media/AudioFormat;")