from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MidiSender"]

class MidiSender(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/midi/MidiSender"
    __javaconstructor__ = [("()V", False)]
    connect = JavaMethod("(Landroid/media/midi/MidiReceiver;)V")
    disconnect = JavaMethod("(Landroid/media/midi/MidiReceiver;)V")
    onConnect = JavaMethod("(Landroid/media/midi/MidiReceiver;)V")
    onDisconnect = JavaMethod("(Landroid/media/midi/MidiReceiver;)V")