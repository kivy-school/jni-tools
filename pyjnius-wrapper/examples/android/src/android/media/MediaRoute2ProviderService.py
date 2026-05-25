from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaRoute2ProviderService"]

class MediaRoute2ProviderService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaRoute2ProviderService"
    __javaconstructor__ = [("()V", False)]
    REASON_INVALID_COMMAND = JavaStaticField("I")
    REASON_NETWORK_ERROR = JavaStaticField("I")
    REASON_REJECTED = JavaStaticField("I")
    REASON_ROUTE_NOT_AVAILABLE = JavaStaticField("I")
    REASON_UNKNOWN_ERROR = JavaStaticField("I")
    REQUEST_ID_NONE = JavaStaticField("J")
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onSetRouteVolume = JavaMethod("(JLjava/lang/String;I)V")
    onSetSessionVolume = JavaMethod("(JLjava/lang/String;I)V")
    getSessionInfo = JavaMethod("(Ljava/lang/String;)Landroid/media/RoutingSessionInfo;")
    getAllSessionInfo = JavaMethod("()Ljava/util/List;")
    notifySessionCreated = JavaMethod("(JLandroid/media/RoutingSessionInfo;)V")
    notifySessionUpdated = JavaMethod("(Landroid/media/RoutingSessionInfo;)V")
    notifySessionReleased = JavaMethod("(Ljava/lang/String;)V")
    notifyRequestFailed = JavaMethod("(JI)V")
    onCreateSession = JavaMethod("(JLjava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)V")
    onReleaseSession = JavaMethod("(JLjava/lang/String;)V")
    onSelectRoute = JavaMethod("(JLjava/lang/String;Ljava/lang/String;)V")
    onDeselectRoute = JavaMethod("(JLjava/lang/String;Ljava/lang/String;)V")
    onTransferToRoute = JavaMethod("(JLjava/lang/String;Ljava/lang/String;)V")
    onDiscoveryPreferenceChanged = JavaMethod("(Landroid/media/RouteDiscoveryPreference;)V")
    notifyRoutes = JavaMethod("(Ljava/util/Collection;)V")