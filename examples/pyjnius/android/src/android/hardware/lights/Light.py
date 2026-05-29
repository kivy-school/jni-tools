from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getOrdinal = JavaMethod("()I")
    hasBrightnessControl = JavaMethod("()Z")
    hasRgbControl = JavaMethod("()Z")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()I")
    getType = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")