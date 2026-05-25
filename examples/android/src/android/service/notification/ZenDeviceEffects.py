from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZenDeviceEffects"]

class ZenDeviceEffects(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/notification/ZenDeviceEffects"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    shouldDisplayGrayscale = JavaMethod("()Z")
    shouldSuppressAmbientDisplay = JavaMethod("()Z")
    shouldDimWallpaper = JavaMethod("()Z")
    shouldUseNightMode = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/notification/ZenDeviceEffects/Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/service/notification/ZenDeviceEffects;)V", False)]
        setShouldDisplayGrayscale = JavaMethod("(Z)Landroid/service/notification/ZenDeviceEffects$Builder;")
        setShouldSuppressAmbientDisplay = JavaMethod("(Z)Landroid/service/notification/ZenDeviceEffects$Builder;")
        setShouldDimWallpaper = JavaMethod("(Z)Landroid/service/notification/ZenDeviceEffects$Builder;")
        setShouldUseNightMode = JavaMethod("(Z)Landroid/service/notification/ZenDeviceEffects$Builder;")
        build = JavaMethod("()Landroid/service/notification/ZenDeviceEffects;")