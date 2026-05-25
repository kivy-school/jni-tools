from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInfluenceChannel"]

class OSInfluenceChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/influence/domain/OSInfluenceChannel"
    Companion = JavaStaticField("Lcom/onesignal/influence/domain/OSInfluenceChannel$Companion;")
    equalsName = JavaMethod("(Ljava/lang/String;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    values = JavaStaticMethod("()[Lcom/onesignal/influence/domain/OSInfluenceChannel;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/influence/domain/OSInfluenceChannel;")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/influence/domain/OSInfluenceChannel;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/influence/domain/OSInfluenceChannel/Companion"
        fromString = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/influence/domain/OSInfluenceChannel;")
    IAM = JavaStaticField("Lcom/onesignal/influence/domain/OSInfluenceChannel;")
    NOTIFICATION = JavaStaticField("Lcom/onesignal/influence/domain/OSInfluenceChannel;")