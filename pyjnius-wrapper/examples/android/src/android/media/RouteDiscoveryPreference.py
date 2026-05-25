from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RouteDiscoveryPreference"]

class RouteDiscoveryPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/RouteDiscoveryPreference"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPreferredFeatures = JavaMethod("()Ljava/util/List;")
    shouldPerformActiveScan = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RouteDiscoveryPreference/Builder"
        __javaconstructor__ = [("(Ljava/util/List;Z)V", False), ("(Landroid/media/RouteDiscoveryPreference;)V", False)]
        setPreferredFeatures = JavaMethod("(Ljava/util/List;)Landroid/media/RouteDiscoveryPreference$Builder;")
        setShouldPerformActiveScan = JavaMethod("(Z)Landroid/media/RouteDiscoveryPreference$Builder;")
        build = JavaMethod("()Landroid/media/RouteDiscoveryPreference;")