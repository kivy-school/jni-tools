from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaRouter2"]

class MediaRouter2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaRouter2"
    getInstance = JavaMultipleMethod([("(Landroid/content/Context;)Landroid/media/MediaRouter2;", True, False), ("(Landroid/content/Context;Ljava/lang/String;Ljava/util/concurrent/Executor;Ljava/lang/Runnable;)Landroid/media/MediaRouter2;", True, False)])
    requestScan = JavaMethod("(Landroid/media/MediaRouter2$ScanRequest;)Landroid/media/MediaRouter2$ScanToken;")
    cancelScanRequest = JavaMethod("(Landroid/media/MediaRouter2$ScanToken;)V")
    registerRouteCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/MediaRouter2$RouteCallback;Landroid/media/RouteDiscoveryPreference;)V")
    unregisterRouteCallback = JavaMethod("(Landroid/media/MediaRouter2$RouteCallback;)V")
    registerRouteListingPreferenceUpdatedCallback = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    unregisterRouteListingPreferenceUpdatedCallback = JavaMethod("(Ljava/util/function/Consumer;)V")
    showSystemOutputSwitcher = JavaMethod("()Z")
    setRouteListingPreference = JavaMethod("(Landroid/media/RouteListingPreference;)V")
    getRouteListingPreference = JavaMethod("()Landroid/media/RouteListingPreference;")
    getRoutes = JavaMethod("()Ljava/util/List;")
    registerTransferCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/MediaRouter2$TransferCallback;)V")
    unregisterTransferCallback = JavaMethod("(Landroid/media/MediaRouter2$TransferCallback;)V")
    registerControllerCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/MediaRouter2$ControllerCallback;)V")
    unregisterControllerCallback = JavaMethod("(Landroid/media/MediaRouter2$ControllerCallback;)V")
    setOnGetControllerHintsListener = JavaMethod("(Landroid/media/MediaRouter2$OnGetControllerHintsListener;)V")
    transferTo = JavaMethod("(Landroid/media/MediaRoute2Info;)V")
    stop = JavaMethod("()V")
    getSystemController = JavaMethod("()Landroid/media/MediaRouter2$RoutingController;")
    getController = JavaMethod("(Ljava/lang/String;)Landroid/media/MediaRouter2$RoutingController;")
    getControllers = JavaMethod("()Ljava/util/List;")
    setRouteVolume = JavaMethod("(Landroid/media/MediaRoute2Info;I)V")

    class ControllerCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2/ControllerCallback"
        __javaconstructor__ = [("()V", False)]
        onControllerUpdated = JavaMethod("(Landroid/media/MediaRouter2$RoutingController;)V")

    class OnGetControllerHintsListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2/OnGetControllerHintsListener"
        onGetControllerHints = JavaMethod("(Landroid/media/MediaRoute2Info;)Landroid/os/Bundle;")

    class RouteCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2/RouteCallback"
        __javaconstructor__ = [("()V", False)]
        onRoutesAdded = JavaMethod("(Ljava/util/List;)V")
        onRoutesRemoved = JavaMethod("(Ljava/util/List;)V")
        onRoutesChanged = JavaMethod("(Ljava/util/List;)V")
        onRoutesUpdated = JavaMethod("(Ljava/util/List;)V")

    class RoutingController(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2/RoutingController"
        getId = JavaMethod("()Ljava/lang/String;")
        getControlHints = JavaMethod("()Landroid/os/Bundle;")
        getSelectedRoutes = JavaMethod("()Ljava/util/List;")
        getSelectableRoutes = JavaMethod("()Ljava/util/List;")
        getDeselectableRoutes = JavaMethod("()Ljava/util/List;")
        getTransferableRoutes = JavaMethod("()Ljava/util/List;")
        wasTransferInitiatedBySelf = JavaMethod("()Z")
        getRoutingSessionInfo = JavaMethod("()Landroid/media/RoutingSessionInfo;")
        getVolumeHandling = JavaMethod("()I")
        getVolumeMax = JavaMethod("()I")
        getVolume = JavaMethod("()I")
        isReleased = JavaMethod("()Z")
        selectRoute = JavaMethod("(Landroid/media/MediaRoute2Info;)V")
        deselectRoute = JavaMethod("(Landroid/media/MediaRoute2Info;)V")
        setVolume = JavaMethod("(I)V")
        release = JavaMethod("()V")
        toString = JavaMethod("()Ljava/lang/String;")

    class ScanRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2/ScanRequest"
        isScreenOffScan = JavaMethod("()Z")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/media/MediaRouter2/ScanRequest/Builder"
            __javaconstructor__ = [("()V", False)]
            setScreenOffScan = JavaMethod("(Z)Landroid/media/MediaRouter2$ScanRequest$Builder;")
            build = JavaMethod("()Landroid/media/MediaRouter2$ScanRequest;")

    class ScanToken(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2/ScanToken"

    class TransferCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2/TransferCallback"
        __javaconstructor__ = [("()V", False)]
        onTransfer = JavaMethod("(Landroid/media/MediaRouter2$RoutingController;Landroid/media/MediaRouter2$RoutingController;)V")
        onTransferFailure = JavaMethod("(Landroid/media/MediaRoute2Info;)V")
        onStop = JavaMethod("(Landroid/media/MediaRouter2$RoutingController;)V")