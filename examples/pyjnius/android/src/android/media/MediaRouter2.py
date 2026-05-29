from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaRouter2"]

class MediaRouter2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaRouter2"
    getControllers = JavaMethod("()Ljava/util/List;")
    requestScan = JavaMethod("(Landroid/media/MediaRouter2$ScanRequest;)Landroid/media/MediaRouter2$ScanToken;")
    cancelScanRequest = JavaMethod("(Landroid/media/MediaRouter2$ScanToken;)V")
    getRouteListingPreference = JavaMethod("()Landroid/media/RouteListingPreference;")
    getSystemController = JavaMethod("()Landroid/media/MediaRouter2$RoutingController;")
    registerControllerCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/MediaRouter2$ControllerCallback;)V")
    registerRouteCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/MediaRouter2$RouteCallback;Landroid/media/RouteDiscoveryPreference;)V")
    registerRouteListingPreferenceUpdatedCallback = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    registerTransferCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/MediaRouter2$TransferCallback;)V")
    setOnGetControllerHintsListener = JavaMethod("(Landroid/media/MediaRouter2$OnGetControllerHintsListener;)V")
    setRouteListingPreference = JavaMethod("(Landroid/media/RouteListingPreference;)V")
    setRouteVolume = JavaMethod("(Landroid/media/MediaRoute2Info;I)V")
    showSystemOutputSwitcher = JavaMethod("()Z")
    unregisterControllerCallback = JavaMethod("(Landroid/media/MediaRouter2$ControllerCallback;)V")
    unregisterRouteCallback = JavaMethod("(Landroid/media/MediaRouter2$RouteCallback;)V")
    unregisterRouteListingPreferenceUpdatedCallback = JavaMethod("(Ljava/util/function/Consumer;)V")
    unregisterTransferCallback = JavaMethod("(Landroid/media/MediaRouter2$TransferCallback;)V")
    getController = JavaMethod("(Ljava/lang/String;)Landroid/media/MediaRouter2$RoutingController;")
    getInstance = JavaMultipleMethod([("(Landroid/content/Context;Ljava/lang/String;Ljava/util/concurrent/Executor;Ljava/lang/Runnable;)Landroid/media/MediaRouter2;", True, False), ("(Landroid/content/Context;)Landroid/media/MediaRouter2;", True, False)])
    transferTo = JavaMethod("(Landroid/media/MediaRoute2Info;)V")
    stop = JavaMethod("()V")
    getRoutes = JavaMethod("()Ljava/util/List;")

    class TransferCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2$TransferCallback"
        __javaconstructor__ = [("()V", False)]
        onTransfer = JavaMethod("(Landroid/media/MediaRouter2$RoutingController;Landroid/media/MediaRouter2$RoutingController;)V")
        onTransferFailure = JavaMethod("(Landroid/media/MediaRoute2Info;)V")
        onStop = JavaMethod("(Landroid/media/MediaRouter2$RoutingController;)V")

    class ScanToken(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2$ScanToken"

    class ScanRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2$ScanRequest"
        isScreenOffScan = JavaMethod("()Z")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/media/MediaRouter2$ScanRequest$Builder"
            __javaconstructor__ = [("()V", False)]
            setScreenOffScan = JavaMethod("(Z)Landroid/media/MediaRouter2$ScanRequest$Builder;")
            build = JavaMethod("()Landroid/media/MediaRouter2$ScanRequest;")

    class RoutingController(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2$RoutingController"
        setVolume = JavaMethod("(I)V")
        deselectRoute = JavaMethod("(Landroid/media/MediaRoute2Info;)V")
        getControlHints = JavaMethod("()Landroid/os/Bundle;")
        getDeselectableRoutes = JavaMethod("()Ljava/util/List;")
        getRoutingSessionInfo = JavaMethod("()Landroid/media/RoutingSessionInfo;")
        getSelectableRoutes = JavaMethod("()Ljava/util/List;")
        getSelectedRoutes = JavaMethod("()Ljava/util/List;")
        getTransferableRoutes = JavaMethod("()Ljava/util/List;")
        getVolumeHandling = JavaMethod("()I")
        getVolumeMax = JavaMethod("()I")
        selectRoute = JavaMethod("(Landroid/media/MediaRoute2Info;)V")
        wasTransferInitiatedBySelf = JavaMethod("()Z")
        toString = JavaMethod("()Ljava/lang/String;")
        getId = JavaMethod("()Ljava/lang/String;")
        release = JavaMethod("()V")
        getVolume = JavaMethod("()I")
        isReleased = JavaMethod("()Z")

    class RouteCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2$RouteCallback"
        __javaconstructor__ = [("()V", False)]
        onRoutesAdded = JavaMethod("(Ljava/util/List;)V")
        onRoutesChanged = JavaMethod("(Ljava/util/List;)V")
        onRoutesRemoved = JavaMethod("(Ljava/util/List;)V")
        onRoutesUpdated = JavaMethod("(Ljava/util/List;)V")

    class OnGetControllerHintsListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2$OnGetControllerHintsListener"
        onGetControllerHints = JavaMethod("(Landroid/media/MediaRoute2Info;)Landroid/os/Bundle;")

    class ControllerCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaRouter2$ControllerCallback"
        __javaconstructor__ = [("()V", False)]
        onControllerUpdated = JavaMethod("(Landroid/media/MediaRouter2$RoutingController;)V")