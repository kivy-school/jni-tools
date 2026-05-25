from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Light"]

class Light(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/lights/Light"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    LIGHT_CAPABILITY_BRIGHTNESS = JavaStaticField("I")
    LIGHT_CAPABILITY_COLOR_RGB = JavaStaticField("I")
    LIGHT_CAPABILITY_RGB = JavaStaticField("I")
    LIGHT_TYPE_INPUT = JavaStaticField("I")
    LIGHT_TYPE_KEYBOARD_BACKLIGHT = JavaStaticField("I")
    LIGHT_TYPE_MICROPHONE = JavaStaticField("I")
    LIGHT_TYPE_PLAYER_ID = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    getOrdinal = JavaMethod("()I")
    getType = JavaMethod("()I")
    hasBrightnessControl = JavaMethod("()Z")
    hasRgbControl = JavaMethod("()Z")