from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MidiReceiver"]

class MidiReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/midi/MidiReceiver"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    onSend = JavaMethod("([BIIJ)V")
    onFlush = JavaMethod("()V")
    getMaxMessageSize = JavaMethod("()I")
    flush = JavaMethod("()V")
    send = JavaMultipleMethod([("([BIIJ)V", False, False), ("([BII)V", False, False)])