from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Geocoder"]

class Geocoder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/Geocoder"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Ljava/util/Locale;)V", False)]
    getFromLocation = JavaMultipleMethod([("(DDI)Ljava/util/List;", False, False), ("(DDILandroid/location/Geocoder$GeocodeListener;)V", False, False)])
    getFromLocationName = JavaMultipleMethod([("(Ljava/lang/String;ILandroid/location/Geocoder$GeocodeListener;)V", False, False), ("(Ljava/lang/String;IDDDD)Ljava/util/List;", False, False), ("(Ljava/lang/String;I)Ljava/util/List;", False, False), ("(Ljava/lang/String;IDDDDLandroid/location/Geocoder$GeocodeListener;)V", False, False)])
    isPresent = JavaStaticMethod("()Z")

    class GeocodeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/Geocoder$GeocodeListener"
        onGeocode = JavaMethod("(Ljava/util/List;)V")
        onError = JavaMethod("(Ljava/lang/String;)V")