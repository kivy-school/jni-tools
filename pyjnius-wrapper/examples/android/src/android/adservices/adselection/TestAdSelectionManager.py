from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TestAdSelectionManager"]

class TestAdSelectionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/TestAdSelectionManager"
    overrideAdSelectionConfigRemoteInfo = JavaMethod("(Landroid/adservices/adselection/AddAdSelectionOverrideRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    removeAdSelectionConfigRemoteInfoOverride = JavaMethod("(Landroid/adservices/adselection/RemoveAdSelectionOverrideRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    resetAllAdSelectionConfigRemoteOverrides = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    overrideAdSelectionFromOutcomesConfigRemoteInfo = JavaMethod("(Landroid/adservices/adselection/AddAdSelectionFromOutcomesOverrideRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    removeAdSelectionFromOutcomesConfigRemoteInfoOverride = JavaMethod("(Landroid/adservices/adselection/RemoveAdSelectionFromOutcomesOverrideRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    resetAllAdSelectionFromOutcomesConfigRemoteOverrides = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")