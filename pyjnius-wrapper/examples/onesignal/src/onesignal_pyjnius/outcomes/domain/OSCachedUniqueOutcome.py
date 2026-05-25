from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSCachedUniqueOutcome"]

class OSCachedUniqueOutcome(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/domain/OSCachedUniqueOutcome"
    __javaconstructor__ = [("(Ljava/lang/String;Lcom/onesignal/influence/domain/OSInfluenceChannel;)V", False)]
    getInfluenceId = JavaMethod("()Ljava/lang/String;")
    getChannel = JavaMethod("()Lcom/onesignal/influence/domain/OSInfluenceChannel;")