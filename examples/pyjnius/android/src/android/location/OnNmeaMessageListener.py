from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnNmeaMessageListener"]

class OnNmeaMessageListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/OnNmeaMessageListener"
    onNmeaMessage = JavaMethod("(Ljava/lang/String;J)V")