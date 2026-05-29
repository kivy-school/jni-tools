from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MobileAds"]

class MobileAds(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/MobileAds"
    ERROR_DOMAIN = JavaStaticField("Ljava/lang/String;")
    initialize = JavaMultipleMethod([("(Landroid/content/Context;)V", True, False), ("(Landroid/content/Context;Lcom/google/android/gms/ads/initialization/OnInitializationCompleteListener;)V", True, False)])
    setAppVolume = JavaStaticMethod("(F)V")
    setAppMuted = JavaStaticMethod("(Z)V")
    openDebugMenu = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)V")
    registerRtbAdapter = JavaStaticMethod("(Ljava/lang/Class;)V")
    getInitializationStatus = JavaStaticMethod("()Lcom/google/android/gms/ads/initialization/InitializationStatus;")
    getRequestConfiguration = JavaStaticMethod("()Lcom/google/android/gms/ads/RequestConfiguration;")
    setRequestConfiguration = JavaStaticMethod("(Lcom/google/android/gms/ads/RequestConfiguration;)V")
    disableMediationAdapterInitialization = JavaStaticMethod("(Landroid/content/Context;)V")
    openAdInspector = JavaStaticMethod("(Landroid/content/Context;Lcom/google/android/gms/ads/OnAdInspectorClosedListener;)V")
    getVersion = JavaStaticMethod("()Lcom/google/android/gms/ads/VersionInfo;")
    registerWebView = JavaStaticMethod("(Landroid/webkit/WebView;)V")
    putPublisherFirstPartyIdEnabled = JavaStaticMethod("(Z)Z")
    registerCustomTabsSession = JavaStaticMethod("(Landroid/content/Context;Landroidx/browser/customtabs/CustomTabsClient;Ljava/lang/String;Landroidx/browser/customtabs/CustomTabsCallback;)Landroidx/browser/customtabs/CustomTabsSession;")
    startPreload = JavaStaticMethod("(Landroid/content/Context;Ljava/util/List;Lcom/google/android/gms/ads/preload/PreloadCallback;)V")