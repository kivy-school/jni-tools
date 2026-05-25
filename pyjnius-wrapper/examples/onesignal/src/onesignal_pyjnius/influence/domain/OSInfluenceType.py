from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInfluenceType"]

class OSInfluenceType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/influence/domain/OSInfluenceType"
    Companion = JavaStaticField("Lcom/onesignal/influence/domain/OSInfluenceType$Companion;")
    isAttributed = JavaMethod("()Z")
    isDirect = JavaMethod("()Z")
    isIndirect = JavaMethod("()Z")
    isUnattributed = JavaMethod("()Z")
    isDisabled = JavaMethod("()Z")
    values = JavaStaticMethod("()[Lcom/onesignal/influence/domain/OSInfluenceType;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/influence/domain/OSInfluenceType;")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/influence/domain/OSInfluenceType;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/influence/domain/OSInfluenceType/Companion"
        fromString = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/influence/domain/OSInfluenceType;")
    DIRECT = JavaStaticField("Lcom/onesignal/influence/domain/OSInfluenceType;")
    INDIRECT = JavaStaticField("Lcom/onesignal/influence/domain/OSInfluenceType;")
    UNATTRIBUTED = JavaStaticField("Lcom/onesignal/influence/domain/OSInfluenceType;")
    DISABLED = JavaStaticField("Lcom/onesignal/influence/domain/OSInfluenceType;")