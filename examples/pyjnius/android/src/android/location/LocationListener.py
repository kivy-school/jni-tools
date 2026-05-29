from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocationListener"]

class LocationListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/LocationListener"
    onStatusChanged = JavaMethod("(Ljava/lang/String;ILandroid/os/Bundle;)V")
    onFlushComplete = JavaMethod("(I)V")
    onLocationChanged = JavaMultipleMethod([("(Ljava/util/List;)V", False, False), ("(Landroid/location/Location;)V", False, False)])
    onProviderDisabled = JavaMethod("(Ljava/lang/String;)V")
    onProviderEnabled = JavaMethod("(Ljava/lang/String;)V")