from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MidiDeviceStatus"]

class MidiDeviceStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/midi/MidiDeviceStatus"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getDeviceInfo = JavaMethod("()Landroid/media/midi/MidiDeviceInfo;")
    isInputPortOpen = JavaMethod("(I)Z")
    getOutputPortOpenCount = JavaMethod("(I)I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")