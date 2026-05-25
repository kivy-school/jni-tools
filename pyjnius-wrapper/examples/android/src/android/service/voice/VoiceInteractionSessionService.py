from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VoiceInteractionSessionService"]

class VoiceInteractionSessionService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/voice/VoiceInteractionSessionService"
    __javaconstructor__ = [("()V", False)]
    onCreate = JavaMethod("()V")
    onNewSession = JavaMethod("(Landroid/os/Bundle;)Landroid/service/voice/VoiceInteractionSession;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    onLowMemory = JavaMethod("()V")
    onTrimMemory = JavaMethod("(I)V")
    dump = JavaMethod("(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")