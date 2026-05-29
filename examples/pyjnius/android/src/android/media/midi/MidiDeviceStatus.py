from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MidiDeviceStatus"]

class MidiDeviceStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/midi/MidiDeviceStatus"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDeviceInfo = JavaMethod("()Landroid/media/midi/MidiDeviceInfo;")
    isInputPortOpen = JavaMethod("(I)Z")
    getOutputPortOpenCount = JavaMethod("(I)I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")