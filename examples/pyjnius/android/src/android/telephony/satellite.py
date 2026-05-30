from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SatelliteStateChangeListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/satellite/SatelliteStateChangeListener"
    onEnabledStateChanged = JavaMethod("(Z)V")

class SatelliteManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/satellite/SatelliteManager"
    unregisterStateChangeListener = JavaMethod("(Landroid/telephony/satellite/SatelliteStateChangeListener;)V")
    registerStateChangeListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/satellite/SatelliteStateChangeListener;)V")