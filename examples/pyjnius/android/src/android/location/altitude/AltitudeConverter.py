from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AltitudeConverter"]

class AltitudeConverter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/altitude/AltitudeConverter"
    __javaconstructor__ = [("()V", False)]
    addMslAltitudeToLocation = JavaMethod("(Landroid/content/Context;Landroid/location/Location;)V")
    tryAddMslAltitudeToLocation = JavaMethod("(Landroid/location/Location;)Z")