from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPorts = JavaMethod("()[Landroid/media/midi/MidiDeviceInfo$PortInfo;")
    getInputPortCount = JavaMethod("()I")
    getDefaultProtocol = JavaMethod("()I")
    getOutputPortCount = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getProperties = JavaMethod("()Landroid/os/Bundle;")
    getId = JavaMethod("()I")
    getType = JavaMethod("()I")
    isPrivate = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class PortInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/midi/MidiDeviceInfo$PortInfo"
        TYPE_INPUT = JavaStaticField("I")
        TYPE_OUTPUT = JavaStaticField("I")
        getPortNumber = JavaMethod("()I")
        getName = JavaMethod("()Ljava/lang/String;")
        getType = JavaMethod("()I")