from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ColorSpaceProfiles"]

class ColorSpaceProfiles(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/ColorSpaceProfiles"
    __javaconstructor__ = [("([J)V", False)]
    UNSPECIFIED = JavaStaticField("I")
    getSupportedColorSpaces = JavaMethod("(I)Ljava/util/Set;")
    getSupportedImageFormatsForColorSpace = JavaMethod("(Landroid/graphics/ColorSpace$Named;)Ljava/util/Set;")
    getSupportedDynamicRangeProfiles = JavaMethod("(Landroid/graphics/ColorSpace$Named;I)Ljava/util/Set;")
    getSupportedColorSpacesForDynamicRange = JavaMethod("(IJ)Ljava/util/Set;")