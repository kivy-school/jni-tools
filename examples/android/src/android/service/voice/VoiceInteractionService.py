from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VoiceInteractionService"]

class VoiceInteractionService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/voice/VoiceInteractionService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    onLaunchVoiceAssistFromKeyguard = JavaMethod("()V")
    onPrepareToShowSession = JavaMethod("(Landroid/os/Bundle;I)V")
    onShowSessionFailed = JavaMethod("(Landroid/os/Bundle;)V")
    isActiveService = JavaStaticMethod("(Landroid/content/Context;Landroid/content/ComponentName;)Z")
    setDisabledShowContext = JavaMethod("(I)V")
    getDisabledShowContext = JavaMethod("()I")
    showSession = JavaMethod("(Landroid/os/Bundle;I)V")
    onGetSupportedVoiceActions = JavaMethod("(Ljava/util/Set;)Ljava/util/Set;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onReady = JavaMethod("()V")
    onShutdown = JavaMethod("()V")
    setUiHints = JavaMethod("(Landroid/os/Bundle;)V")
    dump = JavaMethod("(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")