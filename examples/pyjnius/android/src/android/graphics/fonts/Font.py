from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Font"]

class Font(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/fonts/Font"
    getMetrics = JavaMethod("(Landroid/graphics/Paint;Landroid/graphics/Paint$FontMetrics;)V")
    getBuffer = JavaMethod("()Ljava/nio/ByteBuffer;")
    getAxes = JavaMethod("()[Landroid/graphics/fonts/FontVariationAxis;")
    getTtcIndex = JavaMethod("()I")
    getGlyphBounds = JavaMethod("(ILandroid/graphics/Paint;Landroid/graphics/RectF;)F")
    getLocaleList = JavaMethod("()Landroid/os/LocaleList;")
    getSourceIdentifier = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getFile = JavaMethod("()Ljava/io/File;")
    getStyle = JavaMethod("()Landroid/graphics/fonts/FontStyle;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/fonts/Font$Builder"
        __javaconstructor__ = [("(Landroid/content/res/AssetManager;Ljava/lang/String;)V", False), ("(Ljava/nio/ByteBuffer;)V", False), ("(Ljava/io/File;)V", False), ("(Landroid/graphics/fonts/Font;)V", False), ("(Landroid/os/ParcelFileDescriptor;)V", False), ("(Landroid/content/res/Resources;I)V", False), ("(Landroid/os/ParcelFileDescriptor;JJ)V", False)]
        setTtcIndex = JavaMethod("(I)Landroid/graphics/fonts/Font$Builder;")
        setWeight = JavaMethod("(I)Landroid/graphics/fonts/Font$Builder;")
        setSlant = JavaMethod("(I)Landroid/graphics/fonts/Font$Builder;")
        build = JavaMethod("()Landroid/graphics/fonts/Font;")
        setFontVariationSettings = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/graphics/fonts/Font$Builder;", False, False), ("([Landroid/graphics/fonts/FontVariationAxis;)Landroid/graphics/fonts/Font$Builder;", False, False)])