from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VirtualDisplayConfig"]

class VirtualDisplayConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/display/VirtualDisplayConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    getDimBrightness = JavaMethod("()F")
    getSurface = JavaMethod("()Landroid/view/Surface;")
    getDensityDpi = JavaMethod("()I")
    getDisplayCategories = JavaMethod("()Ljava/util/Set;")
    getRequestedRefreshRate = JavaMethod("()F")
    getDefaultBrightness = JavaMethod("()F")
    getFlags = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/display/VirtualDisplayConfig$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;III)V", False)]
        setSurface = JavaMethod("(Landroid/view/Surface;)Landroid/hardware/display/VirtualDisplayConfig$Builder;")
        setBrightnessListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/hardware/display/VirtualDisplayConfig$BrightnessListener;)Landroid/hardware/display/VirtualDisplayConfig$Builder;")
        setDefaultBrightness = JavaMethod("(F)Landroid/hardware/display/VirtualDisplayConfig$Builder;")
        setRequestedRefreshRate = JavaMethod("(F)Landroid/hardware/display/VirtualDisplayConfig$Builder;")
        addDisplayCategory = JavaMethod("(Ljava/lang/String;)Landroid/hardware/display/VirtualDisplayConfig$Builder;")
        setDimBrightness = JavaMethod("(F)Landroid/hardware/display/VirtualDisplayConfig$Builder;")
        setDisplayCategories = JavaMethod("(Ljava/util/Set;)Landroid/hardware/display/VirtualDisplayConfig$Builder;")
        setFlags = JavaMethod("(I)Landroid/hardware/display/VirtualDisplayConfig$Builder;")
        build = JavaMethod("()Landroid/hardware/display/VirtualDisplayConfig;")

    class BrightnessListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/display/VirtualDisplayConfig$BrightnessListener"
        onBrightnessChanged = JavaMethod("(F)V")