from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnNmeaMessageListener"]

class OnNmeaMessageListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/OnNmeaMessageListener"
    onNmeaMessage = JavaMethod("(Ljava/lang/String;J)V")