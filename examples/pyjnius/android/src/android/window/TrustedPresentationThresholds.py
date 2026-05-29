from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrustedPresentationThresholds"]

class TrustedPresentationThresholds(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/TrustedPresentationThresholds"
    __javaconstructor__ = [("(FFI)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMinAlpha = JavaMethod("()F")
    getMinFractionRendered = JavaMethod("()F")
    getStabilityRequirementMillis = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")