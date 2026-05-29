from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Gainmap"]

class Gainmap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Gainmap"
    __javaconstructor__ = [("(Landroid/graphics/Gainmap;Landroid/graphics/Bitmap;)V", False), ("(Landroid/graphics/Bitmap;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    GAINMAP_DIRECTION_HDR_TO_SDR = JavaStaticField("I")
    GAINMAP_DIRECTION_SDR_TO_HDR = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    setEpsilonHdr = JavaMethod("(FFF)V")
    setGamma = JavaMethod("(FFF)V")
    setEpsilonSdr = JavaMethod("(FFF)V")
    getRatioMin = JavaMethod("()[F")
    setGainmapContents = JavaMethod("(Landroid/graphics/Bitmap;)V")
    getRatioMax = JavaMethod("()[F")
    getGainmapContents = JavaMethod("()Landroid/graphics/Bitmap;")
    getGamma = JavaMethod("()[F")
    getEpsilonSdr = JavaMethod("()[F")
    setRatioMin = JavaMethod("(FFF)V")
    setRatioMax = JavaMethod("(FFF)V")
    setDisplayRatioForFullHdr = JavaMethod("(F)V")
    setGainmapDirection = JavaMethod("(I)V")
    setMinDisplayRatioForHdrTransition = JavaMethod("(F)V")
    getEpsilonHdr = JavaMethod("()[F")
    getAlternativeImagePrimaries = JavaMethod("()Landroid/graphics/ColorSpace;")
    getDisplayRatioForFullHdr = JavaMethod("()F")
    getGainmapDirection = JavaMethod("()I")
    getMinDisplayRatioForHdrTransition = JavaMethod("()F")
    setAlternativeImagePrimaries = JavaMethod("(Landroid/graphics/ColorSpace;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")