from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SurfaceControlInputReceiver"]

class SurfaceControlInputReceiver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/SurfaceControlInputReceiver"
    onInputEvent = JavaMethod("(Landroid/view/InputEvent;)Z")