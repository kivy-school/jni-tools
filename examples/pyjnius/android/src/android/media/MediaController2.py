from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaController2"]

class MediaController2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaController2"
    isPlaybackActive = JavaMethod("()Z")
    cancelSessionCommand = JavaMethod("(Ljava/lang/Object;)V")
    sendSessionCommand = JavaMethod("(Landroid/media/Session2Command;Landroid/os/Bundle;)Ljava/lang/Object;")
    getConnectedToken = JavaMethod("()Landroid/media/Session2Token;")
    close = JavaMethod("()V")

    class ControllerCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaController2$ControllerCallback"
        __javaconstructor__ = [("()V", False)]
        onDisconnected = JavaMethod("(Landroid/media/MediaController2;)V")
        onCommandResult = JavaMethod("(Landroid/media/MediaController2;Ljava/lang/Object;Landroid/media/Session2Command;Landroid/media/Session2Command$Result;)V")
        onPlaybackActiveChanged = JavaMethod("(Landroid/media/MediaController2;Z)V")
        onSessionCommand = JavaMethod("(Landroid/media/MediaController2;Landroid/media/Session2Command;Landroid/os/Bundle;)Landroid/media/Session2Command$Result;")
        onConnected = JavaMethod("(Landroid/media/MediaController2;Landroid/media/Session2CommandGroup;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaController2$Builder"
        __javaconstructor__ = [("(Landroid/content/Context;Landroid/media/Session2Token;)V", False)]
        setConnectionHints = JavaMethod("(Landroid/os/Bundle;)Landroid/media/MediaController2$Builder;")
        setControllerCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/MediaController2$ControllerCallback;)Landroid/media/MediaController2$Builder;")
        build = JavaMethod("()Landroid/media/MediaController2;")