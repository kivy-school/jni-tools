from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeviceStateSensorOrientationMap"]

class DeviceStateSensorOrientationMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/DeviceStateSensorOrientationMap"
    FOLDED = JavaStaticField("J")
    NORMAL = JavaStaticField("J")
    getSensorOrientation = JavaMethod("(J)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/params/DeviceStateSensorOrientationMap/Builder"
        __javaconstructor__ = [("()V", False)]
        addOrientationForState = JavaMethod("(JJ)Landroid/hardware/camera2/params/DeviceStateSensorOrientationMap$Builder;")
        build = JavaMethod("()Landroid/hardware/camera2/params/DeviceStateSensorOrientationMap;")