from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaBrowser"]

class MediaBrowser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/browse/MediaBrowser"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/ComponentName;Landroid/media/browse/MediaBrowser$ConnectionCallback;Landroid/os/Bundle;)V", False)]
    EXTRA_PAGE = JavaStaticField("Ljava/lang/String;")
    EXTRA_PAGE_SIZE = JavaStaticField("Ljava/lang/String;")
    connect = JavaMethod("()V")
    disconnect = JavaMethod("()V")
    isConnected = JavaMethod("()Z")
    getServiceComponent = JavaMethod("()Landroid/content/ComponentName;")
    getRoot = JavaMethod("()Ljava/lang/String;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getSessionToken = JavaMethod("()Landroid/media/session/MediaSession$Token;")
    subscribe = JavaMultipleMethod([("(Ljava/lang/String;Landroid/media/browse/MediaBrowser$SubscriptionCallback;)V", False, False), ("(Ljava/lang/String;Landroid/os/Bundle;Landroid/media/browse/MediaBrowser$SubscriptionCallback;)V", False, False)])
    unsubscribe = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Landroid/media/browse/MediaBrowser$SubscriptionCallback;)V", False, False)])
    getItem = JavaMethod("(Ljava/lang/String;Landroid/media/browse/MediaBrowser$ItemCallback;)V")

    class ConnectionCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/browse/MediaBrowser/ConnectionCallback"
        __javaconstructor__ = [("()V", False)]
        onConnected = JavaMethod("()V")
        onConnectionSuspended = JavaMethod("()V")
        onConnectionFailed = JavaMethod("()V")

    class ItemCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/browse/MediaBrowser/ItemCallback"
        __javaconstructor__ = [("()V", False)]
        onItemLoaded = JavaMethod("(Landroid/media/browse/MediaBrowser$MediaItem;)V")
        onError = JavaMethod("(Ljava/lang/String;)V")

    class MediaItem(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/browse/MediaBrowser/MediaItem"
        __javaconstructor__ = [("(Landroid/media/MediaDescription;I)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        FLAG_BROWSABLE = JavaStaticField("I")
        FLAG_PLAYABLE = JavaStaticField("I")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        toString = JavaMethod("()Ljava/lang/String;")
        getFlags = JavaMethod("()I")
        isBrowsable = JavaMethod("()Z")
        isPlayable = JavaMethod("()Z")
        getDescription = JavaMethod("()Landroid/media/MediaDescription;")
        getMediaId = JavaMethod("()Ljava/lang/String;")

    class SubscriptionCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/browse/MediaBrowser/SubscriptionCallback"
        __javaconstructor__ = [("()V", False)]
        onChildrenLoaded = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/List;)V", False, False), ("(Ljava/lang/String;Ljava/util/List;Landroid/os/Bundle;)V", False, False)])
        onError = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Landroid/os/Bundle;)V", False, False)])