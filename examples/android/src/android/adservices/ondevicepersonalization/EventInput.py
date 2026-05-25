from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventInput"]

class EventInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/EventInput"
    getRequestLogRecord = JavaMethod("()Landroid/adservices/ondevicepersonalization/RequestLogRecord;")
    getParameters = JavaMethod("()Landroid/os/PersistableBundle;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")