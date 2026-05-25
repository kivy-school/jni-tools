from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MidiDeviceService"]

class MidiDeviceService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/midi/MidiDeviceService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onCreate = JavaMethod("()V")
    onGetInputPortReceivers = JavaMethod("()[Landroid/media/midi/MidiReceiver;")
    getOutputPortReceivers = JavaMethod("()[Landroid/media/midi/MidiReceiver;")
    getDeviceInfo = JavaMethod("()Landroid/media/midi/MidiDeviceInfo;")
    onDeviceStatusChanged = JavaMethod("(Landroid/media/midi/MidiDeviceStatus;)V")
    onClose = JavaMethod("()V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")