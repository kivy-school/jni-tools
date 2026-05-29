from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SurfaceControlInputReceiver"]

class SurfaceControlInputReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/SurfaceControlInputReceiver"
    onInputEvent = JavaMethod("(Landroid/view/InputEvent;)Z")