from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MidiDevice"]

class MidiDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/midi/MidiDevice"
    getInfo = JavaMethod("()Landroid/media/midi/MidiDeviceInfo;")
    openInputPort = JavaMethod("(I)Landroid/media/midi/MidiInputPort;")
    openOutputPort = JavaMethod("(I)Landroid/media/midi/MidiOutputPort;")
    connectPorts = JavaMethod("(Landroid/media/midi/MidiInputPort;I)Landroid/media/midi/MidiDevice$MidiConnection;")
    close = JavaMethod("()V")
    finalize = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")

    class MidiConnection(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/midi/MidiDevice/MidiConnection"
        close = JavaMethod("()V")
        finalize = JavaMethod("()V")