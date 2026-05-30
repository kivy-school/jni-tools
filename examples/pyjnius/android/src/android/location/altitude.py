from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AltitudeConverter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/altitude/AltitudeConverter"
    __javaconstructor__ = [("()V", False)]
    tryAddMslAltitudeToLocation = JavaMethod("(Landroid/location/Location;)Z")
    addMslAltitudeToLocation = JavaMethod("(Landroid/content/Context;Landroid/location/Location;)V")