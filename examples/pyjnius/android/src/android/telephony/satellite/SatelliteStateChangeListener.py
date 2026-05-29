from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SatelliteStateChangeListener"]

class SatelliteStateChangeListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/satellite/SatelliteStateChangeListener"
    onEnabledStateChanged = JavaMethod("(Z)V")