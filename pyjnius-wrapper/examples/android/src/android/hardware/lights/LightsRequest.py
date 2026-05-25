from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LightsRequest"]

class LightsRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/lights/LightsRequest"
    getLights = JavaMethod("()Ljava/util/List;")
    getLightStates = JavaMethod("()Ljava/util/List;")
    getLightsAndStates = JavaMethod("()Ljava/util/Map;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/lights/LightsRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        addLight = JavaMethod("(Landroid/hardware/lights/Light;Landroid/hardware/lights/LightState;)Landroid/hardware/lights/LightsRequest$Builder;")
        clearLight = JavaMethod("(Landroid/hardware/lights/Light;)Landroid/hardware/lights/LightsRequest$Builder;")
        build = JavaMethod("()Landroid/hardware/lights/LightsRequest;")