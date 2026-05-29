from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PerBuyerDecisionLogic"]

class PerBuyerDecisionLogic(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/PerBuyerDecisionLogic"
    __javaconstructor__ = [("(Ljava/util/Map;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EMPTY = JavaStaticField("Landroid/adservices/adselection/PerBuyerDecisionLogic;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPerBuyerLogicMap = JavaMethod("()Ljava/util/Map;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")