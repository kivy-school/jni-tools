from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Font"]

class Font(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/fonts/Font"
    getBuffer = JavaMethod("()Ljava/nio/ByteBuffer;")
    getFile = JavaMethod("()Ljava/io/File;")
    getStyle = JavaMethod("()Landroid/graphics/fonts/FontStyle;")
    getTtcIndex = JavaMethod("()I")
    getAxes = JavaMethod("()[Landroid/graphics/fonts/FontVariationAxis;")
    getLocaleList = JavaMethod("()Landroid/os/LocaleList;")
    getGlyphBounds = JavaMethod("(ILandroid/graphics/Paint;Landroid/graphics/RectF;)F")
    getMetrics = JavaMethod("(Landroid/graphics/Paint;Landroid/graphics/Paint$FontMetrics;)V")
    getSourceIdentifier = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/fonts/Font/Builder"
        __javaconstructor__ = [("(Ljava/nio/ByteBuffer;)V", False), ("(Ljava/io/File;)V", False), ("(Landroid/os/ParcelFileDescriptor;)V", False), ("(Landroid/os/ParcelFileDescriptor;JJ)V", False), ("(Landroid/content/res/AssetManager;Ljava/lang/String;)V", False), ("(Landroid/content/res/Resources;I)V", False), ("(Landroid/graphics/fonts/Font;)V", False)]
        setWeight = JavaMethod("(I)Landroid/graphics/fonts/Font$Builder;")
        setSlant = JavaMethod("(I)Landroid/graphics/fonts/Font$Builder;")
        setTtcIndex = JavaMethod("(I)Landroid/graphics/fonts/Font$Builder;")
        setFontVariationSettings = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/graphics/fonts/Font$Builder;", False, False), ("([Landroid/graphics/fonts/FontVariationAxis;)Landroid/graphics/fonts/Font$Builder;", False, False)])
        build = JavaMethod("()Landroid/graphics/fonts/Font;")