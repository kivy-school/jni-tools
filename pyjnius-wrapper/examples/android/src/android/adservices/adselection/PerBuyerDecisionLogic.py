from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PerBuyerDecisionLogic"]

class PerBuyerDecisionLogic(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/PerBuyerDecisionLogic"
    __javaconstructor__ = [("(Ljava/util/Map;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EMPTY = JavaStaticField("Landroid/adservices/adselection/PerBuyerDecisionLogic;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    getPerBuyerLogicMap = JavaMethod("()Ljava/util/Map;")