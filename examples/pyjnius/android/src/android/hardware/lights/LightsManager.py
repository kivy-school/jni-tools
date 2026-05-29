from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LightsManager"]

class LightsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/lights/LightsManager"
    getLights = JavaMethod("()Ljava/util/List;")
    getLightState = JavaMethod("(Landroid/hardware/lights/Light;)Landroid/hardware/lights/LightState;")
    openSession = JavaMethod("()Landroid/hardware/lights/LightsManager$LightsSession;")

    class LightsSession(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/lights/LightsManager/LightsSession"
        requestLights = JavaMethod("(Landroid/hardware/lights/LightsRequest;)V")
        close = JavaMethod("()V")