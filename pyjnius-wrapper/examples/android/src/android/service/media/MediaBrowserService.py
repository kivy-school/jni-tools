from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaBrowserService"]

class MediaBrowserService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/media/MediaBrowserService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onCreate = JavaMethod("()V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    dump = JavaMethod("(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
    onGetRoot = JavaMethod("(Ljava/lang/String;ILandroid/os/Bundle;)Landroid/service/media/MediaBrowserService$BrowserRoot;")
    onLoadChildren = JavaMultipleMethod([("(Ljava/lang/String;Landroid/service/media/MediaBrowserService$Result;)V", False, False), ("(Ljava/lang/String;Landroid/service/media/MediaBrowserService$Result;Landroid/os/Bundle;)V", False, False)])
    onLoadItem = JavaMethod("(Ljava/lang/String;Landroid/service/media/MediaBrowserService$Result;)V")
    setSessionToken = JavaMethod("(Landroid/media/session/MediaSession$Token;)V")
    getSessionToken = JavaMethod("()Landroid/media/session/MediaSession$Token;")
    getBrowserRootHints = JavaMethod("()Landroid/os/Bundle;")
    getCurrentBrowserInfo = JavaMethod("()Landroid/media/session/MediaSessionManager$RemoteUserInfo;")
    notifyChildrenChanged = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Landroid/os/Bundle;)V", False, False)])

    class BrowserRoot(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/media/MediaBrowserService/BrowserRoot"
        __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;)V", False)]
        EXTRA_OFFLINE = JavaStaticField("Ljava/lang/String;")
        EXTRA_RECENT = JavaStaticField("Ljava/lang/String;")
        EXTRA_SUGGESTED = JavaStaticField("Ljava/lang/String;")
        getRootId = JavaMethod("()Ljava/lang/String;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")

    class Result(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/media/MediaBrowserService/Result"
        sendResult = JavaMethod("(Ljava/lang/Object;)V")
        detach = JavaMethod("()V")