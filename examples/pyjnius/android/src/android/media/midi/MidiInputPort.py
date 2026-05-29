from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MidiInputPort"]

class MidiInputPort(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/midi/MidiInputPort"
    getPortNumber = JavaMethod("()I")
    onSend = JavaMethod("([BIIJ)V")
    onFlush = JavaMethod("()V")
    close = JavaMethod("()V")