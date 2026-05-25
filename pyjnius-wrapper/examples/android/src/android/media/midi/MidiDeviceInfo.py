from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MidiDeviceInfo"]

class MidiDeviceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/midi/MidiDeviceInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PROPERTY_BLUETOOTH_DEVICE = JavaStaticField("Ljava/lang/String;")
    PROPERTY_MANUFACTURER = JavaStaticField("Ljava/lang/String;")
    PROPERTY_NAME = JavaStaticField("Ljava/lang/String;")
    PROPERTY_PRODUCT = JavaStaticField("Ljava/lang/String;")
    PROPERTY_SERIAL_NUMBER = JavaStaticField("Ljava/lang/String;")
    PROPERTY_USB_DEVICE = JavaStaticField("Ljava/lang/String;")
    PROPERTY_VERSION = JavaStaticField("Ljava/lang/String;")
    PROTOCOL_UMP_MIDI_1_0_UP_TO_128_BITS = JavaStaticField("I")
    PROTOCOL_UMP_MIDI_1_0_UP_TO_128_BITS_AND_JRTS = JavaStaticField("I")
    PROTOCOL_UMP_MIDI_1_0_UP_TO_64_BITS = JavaStaticField("I")
    PROTOCOL_UMP_MIDI_1_0_UP_TO_64_BITS_AND_JRTS = JavaStaticField("I")
    PROTOCOL_UMP_MIDI_2_0 = JavaStaticField("I")
    PROTOCOL_UMP_MIDI_2_0_AND_JRTS = JavaStaticField("I")
    PROTOCOL_UMP_USE_MIDI_CI = JavaStaticField("I")
    PROTOCOL_UNKNOWN = JavaStaticField("I")
    TYPE_BLUETOOTH = JavaStaticField("I")
    TYPE_USB = JavaStaticField("I")
    TYPE_VIRTUAL = JavaStaticField("I")
    getType = JavaMethod("()I")
    getId = JavaMethod("()I")
    getInputPortCount = JavaMethod("()I")
    getOutputPortCount = JavaMethod("()I")
    getPorts = JavaMethod("()[Landroid/media/midi/MidiDeviceInfo$PortInfo;")
    getProperties = JavaMethod("()Landroid/os/Bundle;")
    isPrivate = JavaMethod("()Z")
    getDefaultProtocol = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class PortInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/midi/MidiDeviceInfo/PortInfo"
        TYPE_INPUT = JavaStaticField("I")
        TYPE_OUTPUT = JavaStaticField("I")
        getType = JavaMethod("()I")
        getPortNumber = JavaMethod("()I")
        getName = JavaMethod("()Ljava/lang/String;")