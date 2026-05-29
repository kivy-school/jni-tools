from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MidiUmpDeviceService"]

class MidiUmpDeviceService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/midi/MidiUmpDeviceService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onCreate = JavaMethod("()V")
    onGetInputPortReceivers = JavaMethod("()Ljava/util/List;")
    getOutputPortReceivers = JavaMethod("()Ljava/util/List;")
    getDeviceInfo = JavaMethod("()Landroid/media/midi/MidiDeviceInfo;")
    onDeviceStatusChanged = JavaMethod("(Landroid/media/midi/MidiDeviceStatus;)V")
    onClose = JavaMethod("()V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")