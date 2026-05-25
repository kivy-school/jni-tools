from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VirtualDisplayConfig"]

class VirtualDisplayConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/display/VirtualDisplayConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getName = JavaMethod("()Ljava/lang/String;")
    getWidth = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getDensityDpi = JavaMethod("()I")
    getFlags = JavaMethod("()I")
    getSurface = JavaMethod("()Landroid/view/Surface;")
    getDisplayCategories = JavaMethod("()Ljava/util/Set;")
    getRequestedRefreshRate = JavaMethod("()F")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/display/VirtualDisplayConfig/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;III)V", False)]
        setFlags = JavaMethod("(I)Landroid/hardware/display/VirtualDisplayConfig$Builder;")
        setSurface = JavaMethod("(Landroid/view/Surface;)Landroid/hardware/display/VirtualDisplayConfig$Builder;")
        setDisplayCategories = JavaMethod("(Ljava/util/Set;)Landroid/hardware/display/VirtualDisplayConfig$Builder;")
        addDisplayCategory = JavaMethod("(Ljava/lang/String;)Landroid/hardware/display/VirtualDisplayConfig$Builder;")
        setRequestedRefreshRate = JavaMethod("(F)Landroid/hardware/display/VirtualDisplayConfig$Builder;")
        build = JavaMethod("()Landroid/hardware/display/VirtualDisplayConfig;")