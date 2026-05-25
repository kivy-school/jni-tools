from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocationListener"]

class LocationListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/LocationListener"
    onLocationChanged = JavaMultipleMethod([("(Landroid/location/Location;)V", False, False), ("(Ljava/util/List;)V", False, False)])
    onFlushComplete = JavaMethod("(I)V")
    onStatusChanged = JavaMethod("(Ljava/lang/String;ILandroid/os/Bundle;)V")
    onProviderEnabled = JavaMethod("(Ljava/lang/String;)V")
    onProviderDisabled = JavaMethod("(Ljava/lang/String;)V")