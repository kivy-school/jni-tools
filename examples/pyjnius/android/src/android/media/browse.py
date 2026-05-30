from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class MediaBrowser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/browse/MediaBrowser"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/ComponentName;Landroid/media/browse/MediaBrowser$ConnectionCallback;Landroid/os/Bundle;)V", False)]
    EXTRA_PAGE = JavaStaticField("Ljava/lang/String;")
    EXTRA_PAGE_SIZE = JavaStaticField("Ljava/lang/String;")
    getSessionToken = JavaMethod("()Landroid/media/session/MediaSession$Token;")
    isConnected = JavaMethod("()Z")
    disconnect = JavaMethod("()V")
    getServiceComponent = JavaMethod("()Landroid/content/ComponentName;")
    unsubscribe = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Landroid/media/browse/MediaBrowser$SubscriptionCallback;)V", False, False)])
    connect = JavaMethod("()V")
    getRoot = JavaMethod("()Ljava/lang/String;")
    subscribe = JavaMultipleMethod([("(Ljava/lang/String;Landroid/media/browse/MediaBrowser$SubscriptionCallback;)V", False, False), ("(Ljava/lang/String;Landroid/os/Bundle;Landroid/media/browse/MediaBrowser$SubscriptionCallback;)V", False, False)])
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getItem = JavaMethod("(Ljava/lang/String;Landroid/media/browse/MediaBrowser$ItemCallback;)V")

    class SubscriptionCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/browse/MediaBrowser$SubscriptionCallback"
        __javaconstructor__ = [("()V", False)]
        onChildrenLoaded = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/List;Landroid/os/Bundle;)V", False, False), ("(Ljava/lang/String;Ljava/util/List;)V", False, False)])
        onError = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Landroid/os/Bundle;)V", False, False)])

    class MediaItem(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/browse/MediaBrowser$MediaItem"
        __javaconstructor__ = [("(Landroid/media/MediaDescription;I)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        FLAG_BROWSABLE = JavaStaticField("I")
        FLAG_PLAYABLE = JavaStaticField("I")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getMediaId = JavaMethod("()Ljava/lang/String;")
        isBrowsable = JavaMethod("()Z")
        isPlayable = JavaMethod("()Z")
        toString = JavaMethod("()Ljava/lang/String;")
        getDescription = JavaMethod("()Landroid/media/MediaDescription;")
        getFlags = JavaMethod("()I")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class ItemCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/browse/MediaBrowser$ItemCallback"
        __javaconstructor__ = [("()V", False)]
        onItemLoaded = JavaMethod("(Landroid/media/browse/MediaBrowser$MediaItem;)V")
        onError = JavaMethod("(Ljava/lang/String;)V")

    class ConnectionCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/browse/MediaBrowser$ConnectionCallback"
        __javaconstructor__ = [("()V", False)]
        onConnected = JavaMethod("()V")
        onConnectionFailed = JavaMethod("()V")
        onConnectionSuspended = JavaMethod("()V")