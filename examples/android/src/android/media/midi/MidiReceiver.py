from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MidiReceiver"]

class MidiReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/midi/MidiReceiver"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    onSend = JavaMethod("([BIIJ)V")
    flush = JavaMethod("()V")
    onFlush = JavaMethod("()V")
    getMaxMessageSize = JavaMethod("()I")
    send = JavaMultipleMethod([("([BII)V", False, False), ("([BIIJ)V", False, False)])