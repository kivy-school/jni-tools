from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Device"]

class Device(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/Device"
    DEVICE_TYPE_CHEST_STRAP = JavaStaticField("I")
    DEVICE_TYPE_FITNESS_BAND = JavaStaticField("I")
    DEVICE_TYPE_HEAD_MOUNTED = JavaStaticField("I")
    DEVICE_TYPE_PHONE = JavaStaticField("I")
    DEVICE_TYPE_RING = JavaStaticField("I")
    DEVICE_TYPE_SCALE = JavaStaticField("I")
    DEVICE_TYPE_SMART_DISPLAY = JavaStaticField("I")
    DEVICE_TYPE_UNKNOWN = JavaStaticField("I")
    DEVICE_TYPE_WATCH = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getType = JavaMethod("()I")
    getManufacturer = JavaMethod("()Ljava/lang/String;")
    getModel = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/Device$Builder"
        __javaconstructor__ = [("()V", False)]
        setModel = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/datatypes/Device$Builder;")
        setManufacturer = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/datatypes/Device$Builder;")
        setType = JavaMethod("(I)Landroid/health/connect/datatypes/Device$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/Device;")