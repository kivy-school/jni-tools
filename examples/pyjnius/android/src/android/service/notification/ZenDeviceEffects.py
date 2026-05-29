from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZenDeviceEffects"]

class ZenDeviceEffects(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/notification/ZenDeviceEffects"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    shouldUseNightMode = JavaMethod("()Z")
    shouldDimWallpaper = JavaMethod("()Z")
    shouldDisplayGrayscale = JavaMethod("()Z")
    shouldSuppressAmbientDisplay = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/notification/ZenDeviceEffects$Builder"
        __javaconstructor__ = [("(Landroid/service/notification/ZenDeviceEffects;)V", False), ("()V", False)]
        setShouldDisplayGrayscale = JavaMethod("(Z)Landroid/service/notification/ZenDeviceEffects$Builder;")
        setShouldSuppressAmbientDisplay = JavaMethod("(Z)Landroid/service/notification/ZenDeviceEffects$Builder;")
        setShouldUseNightMode = JavaMethod("(Z)Landroid/service/notification/ZenDeviceEffects$Builder;")
        setShouldDimWallpaper = JavaMethod("(Z)Landroid/service/notification/ZenDeviceEffects$Builder;")
        build = JavaMethod("()Landroid/service/notification/ZenDeviceEffects;")