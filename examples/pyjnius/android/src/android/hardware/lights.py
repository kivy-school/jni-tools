from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LightsRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/lights/LightsRequest"
    getLights = JavaMethod("()Ljava/util/List;")
    getLightStates = JavaMethod("()Ljava/util/List;")
    getLightsAndStates = JavaMethod("()Ljava/util/Map;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/lights/LightsRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        addLight = JavaMethod("(Landroid/hardware/lights/Light;Landroid/hardware/lights/LightState;)Landroid/hardware/lights/LightsRequest$Builder;")
        clearLight = JavaMethod("(Landroid/hardware/lights/Light;)Landroid/hardware/lights/LightsRequest$Builder;")
        build = JavaMethod("()Landroid/hardware/lights/LightsRequest;")

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
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class LightsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/lights/LightsManager"
    getLights = JavaMethod("()Ljava/util/List;")
    getLightState = JavaMethod("(Landroid/hardware/lights/Light;)Landroid/hardware/lights/LightState;")
    openSession = JavaMethod("()Landroid/hardware/lights/LightsManager$LightsSession;")

    class LightsSession(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/lights/LightsManager$LightsSession"
        requestLights = JavaMethod("(Landroid/hardware/lights/LightsRequest;)V")
        close = JavaMethod("()V")

class LightState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/lights/LightState"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPlayerId = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getColor = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/lights/LightState$Builder"
        __javaconstructor__ = [("()V", False)]
        setPlayerId = JavaMethod("(I)Landroid/hardware/lights/LightState$Builder;")
        setColor = JavaMethod("(I)Landroid/hardware/lights/LightState$Builder;")
        build = JavaMethod("()Landroid/hardware/lights/LightState;")