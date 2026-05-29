from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MidiDevice"]

class MidiDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/midi/MidiDevice"
    getInfo = JavaMethod("()Landroid/media/midi/MidiDeviceInfo;")
    openInputPort = JavaMethod("(I)Landroid/media/midi/MidiInputPort;")
    connectPorts = JavaMethod("(Landroid/media/midi/MidiInputPort;I)Landroid/media/midi/MidiDevice$MidiConnection;")
    openOutputPort = JavaMethod("(I)Landroid/media/midi/MidiOutputPort;")
    toString = JavaMethod("()Ljava/lang/String;")
    close = JavaMethod("()V")

    class MidiConnection(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/midi/MidiDevice$MidiConnection"
        close = JavaMethod("()V")