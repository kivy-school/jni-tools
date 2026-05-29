from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RewardItem"]

class RewardItem(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/rewarded/RewardItem"
    DEFAULT_REWARD = JavaStaticField("Lcom/google/android/gms/ads/rewarded/RewardItem;")
    getType = JavaMethod("()Ljava/lang/String;")
    getAmount = JavaMethod("()I")