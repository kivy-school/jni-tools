from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MidiManager"]

class MidiManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/midi/MidiManager"
    TRANSPORT_MIDI_BYTE_STREAM = JavaStaticField("I")
    TRANSPORT_UNIVERSAL_MIDI_PACKETS = JavaStaticField("I")
    registerDeviceCallback = JavaMultipleMethod([("(Landroid/media/midi/MidiManager$DeviceCallback;Landroid/os/Handler;)V", False, False), ("(ILjava/util/concurrent/Executor;Landroid/media/midi/MidiManager$DeviceCallback;)V", False, False)])
    unregisterDeviceCallback = JavaMethod("(Landroid/media/midi/MidiManager$DeviceCallback;)V")
    getDevices = JavaMethod("()[Landroid/media/midi/MidiDeviceInfo;")
    getDevicesForTransport = JavaMethod("(I)Ljava/util/Set;")
    openDevice = JavaMethod("(Landroid/media/midi/MidiDeviceInfo;Landroid/media/midi/MidiManager$OnDeviceOpenedListener;Landroid/os/Handler;)V")
    openBluetoothDevice = JavaMethod("(Landroid/bluetooth/BluetoothDevice;Landroid/media/midi/MidiManager$OnDeviceOpenedListener;Landroid/os/Handler;)V")

    class DeviceCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/midi/MidiManager/DeviceCallback"
        __javaconstructor__ = [("()V", False)]
        onDeviceAdded = JavaMethod("(Landroid/media/midi/MidiDeviceInfo;)V")
        onDeviceRemoved = JavaMethod("(Landroid/media/midi/MidiDeviceInfo;)V")
        onDeviceStatusChanged = JavaMethod("(Landroid/media/midi/MidiDeviceStatus;)V")

    class OnDeviceOpenedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/midi/MidiManager/OnDeviceOpenedListener"
        onDeviceOpened = JavaMethod("(Landroid/media/midi/MidiDevice;)V")