from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MidiOutputPort"]

class MidiOutputPort(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/midi/MidiOutputPort"
    getPortNumber = JavaMethod("()I")
    onConnect = JavaMethod("(Landroid/media/midi/MidiReceiver;)V")
    close = JavaMethod("()V")
    onDisconnect = JavaMethod("(Landroid/media/midi/MidiReceiver;)V")