from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LightState"]

class LightState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/lights/LightState"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPlayerId = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getColor = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/lights/LightState$Builder"
        __javaconstructor__ = [("()V", False)]
        setPlayerId = JavaMethod("(I)Landroid/hardware/lights/LightState$Builder;")
        setColor = JavaMethod("(I)Landroid/hardware/lights/LightState$Builder;")
        build = JavaMethod("()Landroid/hardware/lights/LightState;")