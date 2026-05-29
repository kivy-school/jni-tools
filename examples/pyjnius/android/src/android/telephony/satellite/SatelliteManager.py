from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SatelliteManager"]

class SatelliteManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/satellite/SatelliteManager"
    registerStateChangeListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/satellite/SatelliteStateChangeListener;)V")
    unregisterStateChangeListener = JavaMethod("(Landroid/telephony/satellite/SatelliteStateChangeListener;)V")