from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RouteDiscoveryPreference"]

class RouteDiscoveryPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/RouteDiscoveryPreference"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPreferredFeatures = JavaMethod("()Ljava/util/List;")
    shouldPerformActiveScan = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RouteDiscoveryPreference$Builder"
        __javaconstructor__ = [("(Landroid/media/RouteDiscoveryPreference;)V", False), ("(Ljava/util/List;Z)V", False)]
        setPreferredFeatures = JavaMethod("(Ljava/util/List;)Landroid/media/RouteDiscoveryPreference$Builder;")
        setShouldPerformActiveScan = JavaMethod("(Z)Landroid/media/RouteDiscoveryPreference$Builder;")
        build = JavaMethod("()Landroid/media/RouteDiscoveryPreference;")