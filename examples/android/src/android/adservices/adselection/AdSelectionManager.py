from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdSelectionManager"]

class AdSelectionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AdSelectionManager"
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/adselection/AdSelectionManager;")
    getTestAdSelectionManager = JavaMethod("()Landroid/adservices/adselection/TestAdSelectionManager;")
    getAdSelectionData = JavaMethod("(Landroid/adservices/adselection/GetAdSelectionDataRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    persistAdSelectionResult = JavaMethod("(Landroid/adservices/adselection/PersistAdSelectionResultRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    selectAds = JavaMultipleMethod([("(Landroid/adservices/adselection/AdSelectionConfig;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/adservices/adselection/AdSelectionFromOutcomesConfig;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False)])
    reportImpression = JavaMethod("(Landroid/adservices/adselection/ReportImpressionRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    reportEvent = JavaMethod("(Landroid/adservices/adselection/ReportEventRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    setAppInstallAdvertisers = JavaMethod("(Landroid/adservices/adselection/SetAppInstallAdvertisersRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    updateAdCounterHistogram = JavaMethod("(Landroid/adservices/adselection/UpdateAdCounterHistogramRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")