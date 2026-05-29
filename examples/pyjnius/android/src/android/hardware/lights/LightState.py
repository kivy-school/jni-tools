from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LightState"]

class LightState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/lights/LightState"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getColor = JavaMethod("()I")
    getPlayerId = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/lights/LightState/Builder"
        __javaconstructor__ = [("()V", False)]
        setColor = JavaMethod("(I)Landroid/hardware/lights/LightState$Builder;")
        setPlayerId = JavaMethod("(I)Landroid/hardware/lights/LightState$Builder;")
        build = JavaMethod("()Landroid/hardware/lights/LightState;")