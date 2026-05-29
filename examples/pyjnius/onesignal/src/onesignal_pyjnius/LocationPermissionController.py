from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocationPermissionController"]

class LocationPermissionController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/LocationPermissionController"
    INSTANCE = JavaStaticField("Lcom/onesignal/LocationPermissionController;")
    prompt = JavaMethod("(ZLjava/lang/String;)V")
    onAccept = JavaMethod("()V")
    onReject = JavaMethod("(Z)V")